import csv
import os
import pickle
import tkinter as tk
from datetime import datetime as dtm
from io import BytesIO
from time import sleep
from tkinter import ttk
from tkinter import messagebox

import requests
from PIL import Image, ImageTk

from igmapper import (
    bold_str,
    extract_cookies,
    friendships_followers,
    friendships_following,
    italic_str,
    save_to_csv,
    start_browser,
    web_profile_info,
)

# Define paths for source and logs
CWD = os.getcwd()  # current working directory
SRC, LOG = f"{CWD}/src", f"{CWD}/logs"
PKL = f"{SRC}/cookies.pkl"

CHROMEDRIVER = f"{CWD}/chromedriver"
URL = "https://instagram.com/"

# fmt: off
cookie_valid, retry = False, 1
while not cookie_valid and retry <= 3:
    retry += 1
    try:
        cookie = pickle.load(open(PKL, "rb"))
        print("Cookie file found...")

        for i in cookie:
            if "csrftoken" in i["name"]:
                csrftoken = i["value"]
            if "sessionid" in i["name"]:
                sessionid, expiry = i["value"], i["expiry"]

        expiry, now = dtm.fromtimestamp(expiry), dtm.now()
        if now > expiry:
            raise Exception("Cookie expired.")
        cookie_valid = True
    except Exception:
        print(f"{bold_str('Login • Instagram')}\n{italic_str('You need to login to continue')}")
        driver = start_browser(URL, CHROMEDRIVER, False, True)
        sleep(60)
        extract_cookies(driver, SRC)


# Função para criar a janela principal
def create_interface():
    root = tk.Tk()
    root.title("IG Mapper API")
    root.geometry("600x800")

    # Tornar a janela responsiva
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    # Frame principal
    main_frame = ttk.Frame(root)
    main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def on_search_click():
        usr = search_entry.get()
        if not usr:
            messagebox.showwarning("Entrada inválida", "Por favor, insira o nome do usuário.")
            return

        try:
            acc = web_profile_info(usr, csrftoken)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar informações: {e}")
            return

        open(f"{LOG}/{usr}-profile_info.json", "w").write(str(acc))

        user = acc["data"]["user"]
        user_id = user["id"]

        search_frame.pack_forget()
        show_info(user, user_id)

    def show_info(user, user_id):
        bio = user["biography"]
        bio_links = user["bio_links"]
        category_name = user["category_name"]
        follow = user["edge_follow"]["count"]
        followed = user["edge_followed_by"]["count"]
        full_name = user["full_name"]
        is_private = user["is_private"]
        is_verified = user["is_verified"]
        posts_count = user["edge_owner_to_timeline_media"]["count"]
        profile_pic_url_hd = user["profile_pic_url_hd"]

        img_tk = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(profile_pic_url_hd).content)).resize((100, 100)))
        img_label = ttk.Label(main_frame, image=img_tk)
        img_label.image = img_tk
        img_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky="nw")

        user_name = ttk.Label(main_frame, text=user, font=("Helvetica", 20, "bold"))
        user_name.grid(row=0, column=1, sticky="w", padx=10, pady=5)

        chip_frame = ttk.Frame(main_frame)
        chip_frame.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        posts_chip = ttk.Label(chip_frame, text=f"{posts_count} posts", relief="solid", padding=5, width=10)
        posts_chip.grid(row=0, column=0, padx=5, pady=5)

        followers_chip = ttk.Label(chip_frame, text=f"{followed} followers", relief="solid", padding=5, width=10)
        followers_chip.grid(row=0, column=1, padx=5, pady=5)

        following_chip = ttk.Label(chip_frame, text=f"{follow} following", relief="solid", padding=5, width=15)
        following_chip.grid(row=0, column=2, padx=5, pady=5)

        full_name_chip = ttk.Label(chip_frame, text=full_name , relief="solid", padding=5, width=10)
        full_name_chip.grid(row=1, column=0, padx=5, pady=5)

        category_chip = ttk.Label(chip_frame, text=category_name if category_name else "No category", relief="solid", padding=5, width=10)
        category_chip.grid(row=1, column=0, padx=5, pady=5)

        is_private_chip = ttk.Label(chip_frame, text="Private" if is_private else "Public", relief="solid", padding=5, width=10)
        is_private_chip.grid(row=1, column=1, padx=5, pady=5)

        is_verified_chip = ttk.Label(chip_frame, text="Verified" if is_verified else "Not Verified", relief="solid", padding=5, width=15)
        is_verified_chip.grid(row=1, column=2, padx=5, pady=5)

        bio_frame = ttk.Frame(main_frame)
        bio_frame.grid(row=4, column=1, sticky="w", padx=10, pady=20)

        bio_label = ttk.Label(bio_frame, text=bio if bio else "No bio", font=("Helvetica", 10, "italic"))
        bio_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        bio_links_label = ttk.Label(bio_frame, text=f'{[i["url"] for i in bio_links]}' if bio_links else "No bio links", font=("Helvetica", 10, "italic"))
        bio_links_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        # ~~~~~~~~~~~~
        # ~~~ TABS ~~~
        tab_control = ttk.Notebook(main_frame)
        followers_tab = ttk.Frame(tab_control)
        following_tab = ttk.Frame(tab_control)
        not_sdv_tab = ttk.Frame(tab_control)
        posts_tab = ttk.Frame(tab_control)

        tab_control.add(followers_tab, text="Followers")
        tab_control.add(following_tab, text="Following")
        tab_control.add(not_sdv_tab, text="Don't follow back")

        tab_control.grid(row=6, column=1, pady=10, sticky="nsew")

        ttk.Label(followers_tab, text="Lista de seguidores", font=("Helvetica", 12)).pack(pady=20)
        ttk.Label(following_tab, text="Lista de seguindo", font=("Helvetica", 12)).pack(pady=20)
        ttk.Label(not_sdv_tab, text="Lista de não SDV", font=("Helvetica", 12)).pack(pady=20)

        # Retrieve the user's followers and following lists using the user ID
        try:
            print("Get followers...")
            acc_followers = friendships_followers(user_id, csrftoken, sessionid)
            print("Get following...")
            acc_following = friendships_following(user_id, csrftoken, sessionid)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar seguidores/seguindo: {e}")
            return

        # Create dictionaries to store 'following' and 'followers' details
        following_dict, followers_dict = {}, {}

        # Populate the 'following' dictionary with usernames and full names
        print("Building following dictionary...")
        for i in acc_following:
            usr = i.get("username")
            following_dict[usr] = i.get("full_name")

        # Populate the 'followers' dictionary with usernames and full names
        print("Building followers dictionary...")
        for i in acc_followers:
            usr = i.get("username")
            followers_dict[usr] = i.get("full_name")

        # Find users that are in 'following' but not in 'followers' (people who don't follow back)
        print("Get non followers...")
        non_followers = [i for i in following_dict if i not in followers_dict]

        # Display non-followers in the "Don't follow back" tab
        non_followers_list_frame = ttk.Frame(not_sdv_tab)
        non_followers_list_frame.pack(pady=20)

        if non_followers:
            for i, user in enumerate(non_followers):
                ttk.Label(non_followers_list_frame, text=user, font=("Helvetica", 10)).grid(row=i, column=0, sticky="w", padx=5, pady=5)
        else:
            ttk.Label(non_followers_list_frame, text="No non-followers found", font=("Helvetica", 10)).grid(row=0, column=0, padx=5, pady=5)

        # Add the back button
        back_button = ttk.Button(main_frame, text="Voltar à Busca", command=show_search)
        back_button.grid(row=7, column=1, pady=20)


    def show_search():
        for widget in main_frame.winfo_children():
            widget.grid_forget()
        search_frame.pack(pady=20)

    search_frame = ttk.Frame(main_frame)
    search_frame.pack(pady=10)

    search_label = ttk.Label(search_frame, text="Digite o '@' do perfil")
    search_label.grid(row=0, column=0, padx=10, pady=5)

    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    search_button = ttk.Button(search_frame, text="Buscar", command=on_search_click)
    search_button.grid(row=0, column=2, padx=10, pady=5)

    root.mainloop()


# Chama a função para criar a interface
create_interface()
