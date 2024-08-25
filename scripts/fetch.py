from main.instagram.api.Instagram import Instagram
# from main.instagram.mapper import InstagramProfileMapper

def get_input(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            else:
                print("Invalid input. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()

if __name__ == "__main__":
    try:
        username = get_input("Username [Ex: @cocacola]: ").replace("@", "")
        csrftoken = get_input("CSRF Token [Ex: 4CsiolqsKtMa88jqyqRq8Tc3KsGH0NG8]: ")

        # mapper = InstagramProfileMapper(api)
        # profile = mapper.map_profile(user_id)
        # print(profile)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit()

