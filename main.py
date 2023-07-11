import Product as pro
from data import info

# user_data = ["User1", "User2", "User3", "User4"]
# password_data = ["password1", "password2", "password3", "password4"]


class Account:
    def register(self):
        new_user = input("Enter new username : ")
        new_password = input("Enter your password : ")
        if new_user not in info["Name"]:
            info["Name"].append(new_user)
            info["Password"].append(new_password)
            continue_to_login = input("\nYou have been registered successfully. Press 1 to continue to login screen.\n")

            if continue_to_login == "1":
                obj1.login()

    login_attempts = 3

    def login(self):
        user_login = input("Enter your username : ")
        password_login = input("Enter your password : ")

        if user_login in info["Name"]:
            position = info["Name"].index(user_login)

        if (user_login in info["Name"]) and (password_login == info["Password"][position]):
            print("\nWelcome to the system.")
            product = pro.Product()
            product.show_product()

            buy_choice = input("Press 1 to buy a product : ")
            if buy_choice == "1":
                product.add_to_cart()
            else:
                print("Invalid choice.")
            # after_login_function()
        else:
            print("Username or password incorrect.")
            self.login_attempts = self.login_attempts - 1
            print(f"Login attempts left = {self.login_attempts}\n")
            if self.login_attempts > 0:
                self.login()


obj1 = Account()
choice = input("Press 1 to register and 2 to login : ")
if choice == "1":
    obj1.register()
elif choice == "2":
    obj1.login()
else:
    print("invalid Choice.")
