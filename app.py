import os
import pickle
from datetime import datetime as dtm
from io import BytesIO
from subprocess import run
from time import sleep

import requests
from flask import Flask, flash, redirect, render_template, request, send_file, url_for
from PIL import Image

from igmapper import (
    extract_cookies,
    friendships_followers,
    friendships_following,
    start_browser,
    web_profile_info,
)

CWD = os.getcwd()
SRC, LOG = f"{CWD}/src", f"{CWD}/logs"
PKL = f"{SRC}/cookies.pkl"
CHROMEDRIVER = f"{CWD}/chromedriver"
URL = "https://instagram.com/"

app = Flask(__name__)
app.secret_key = "8Aw0oUR0P8Ue7rBPh9n2ud5wTgvTI6j9RwK4pOnBYPy3itdWd3"  # Use a strong key in production

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
        print("You need to login to continue.")
        driver = start_browser(URL, CHROMEDRIVER, False, True)
        sleep(60)
        extract_cookies(driver, SRC)


# Rota para download de arquivo
@app.route("/profile")
def download_file():
    # Caminho do arquivo a ser enviado para o download
    path = "/home/lucas/Downloads/teste.txt"  # Defina o caminho correto do arquivo

    # Envia o arquivo para o cliente para download
    return send_file(path, as_attachment=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            flash("Please enter a username.", "warning")
            return redirect(url_for("index"))

        try:
            acc = web_profile_info(username, csrftoken)
            user = acc["data"]["user"]
            user_id = user["id"]
            user_pic = user["profile_pic_url_hd"]

            filename = f"{LOG}/{username}"
            open(f"{filename}.json", "w").write(str(acc))
            open(f"{CWD}/static/images/profile.png", "wb").write(
                requests.get(user_pic).content
            )

            # Verificar se a checkbox foi marcada
            if "calculate_non_followers" in request.form:
                # Retrieve followers and following
                followers = friendships_followers(user_id, csrftoken, sessionid)
                following = friendships_following(user_id, csrftoken, sessionid)

                # Non-followers
                following_usernames = {user["username"] for user in following}
                followers_usernames = {user["username"] for user in followers}
                non_followers = sorted(list(following_usernames - followers_usernames))

                return render_template(
                    "profile.html",
                    user=user,
                    non_followers=non_followers,
                    user_picture=user_pic,
                )

            return render_template(
                "profile.html",
                user=user,
                user_picture=user_pic,
            )

        except Exception as e:
            flash(f"Error: {e}", "danger")
            return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
