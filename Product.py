import keyboard
from data import info


class Product:
    def show_product(self):
        print("Product Name           Quantity            Price")
        for x in range(len(info["Product"])):
            print(f"{info['Product'][x]}                  {info['Quantity'][x]}                {info['Rate'][x]}")

    amount = 0

    def add_to_cart(self):

        def complete_purchase():
            print("Product            Quantity            Rate")
            for i in info["cart"]:
                print(f"{i['Product']}            {i['Quantity']}                {i['Rate']}")
            print(f"You have to pay a total amount of {self.amount}.")

            finish_payment = input("Press 1 to complete the payment or 2 to cancel your purchase : ")
            if finish_payment == "1":
                print("\nYour Purchase has been completed.")
                info["order"] = info["cart"].copy()
                info["cart"].clear()
                continue_purchase = input("Enter 1 to continue buying products, 2 to show the order receipt"
                                          " or enter any other key to finish the process.\n")
                if continue_purchase == "1":
                    self.show_product()
                    self.add_to_cart()
                elif continue_purchase == "2":
                    print("\nDetails of items purchased-")
                    print("Product            Quantity            Rate")
                    for i in info["order"]:
                        print(f"{i['Product']}            {i['Quantity']}                {i['Rate']}")
                    print(f"Total Amount Paid = {self.amount}")
                else:
                    print("Thanks for shopping with us!")
            elif finish_payment == "2":
                for x in info["cart"]:
                    pos = info["Product"].index(x["Product"])
                    info["Quantity"][pos] = info["Quantity"][pos] + x["Quantity"]
                purchase_again = input("\nEnter 1 to buy again or any other key to finish the process : ")
                if purchase_again == "1":
                    self.show_product()
                    self.add_to_cart()
                else:
                    print("Thanks for coming!")
            else:
                print("Invalid Choice")

        choose_product = input("\nChoose your product : ")
        if choose_product in info["Product"]:
            position = info["Product"].index(choose_product)

        if choose_product in info["Product"] and (info["Quantity"][position] != 0) :
            quantity = int(input("How many would you like : "))
            if info["Quantity"][position] - quantity >= 0:
                rate = info["Rate"][position] * quantity
                print(f"\nYour selected quantity is available and would cost you the total of "
                      f"{rate}.\n")

                choice = input("Press 1 to add your product to cart or 2 to choose again\n")
                if choice == "1":
                    self.amount = self.amount + rate
                    info["cart"].append({"Product": choose_product, "Quantity": quantity, "Rate": rate,
                                         "Amount": self.amount})
                    print("Your product has been successfully added to cart")
                    info["Quantity"][position] = info["Quantity"][position] - quantity

                    def update_cart():
                        continue_update = True
                        while continue_update:
                            print("\n")
                            update_choice = input("Enter 1 to change the quantity of products in cart, 2 to delete"
                                                  " products, 3 to empty the cart or any other key to finish update : ")

                            if update_choice == "1":
                                continue_update_quantity = True
                                while continue_update_quantity:
                                    print("Product            Quantity            Rate")
                                    for i in info["cart"]:
                                        print(f"{i['Product']}            {i['Quantity']}                {i['Rate']}")
                                    change = input("For which product you want to change the quantity : ")
                                    # Here change is product to be changed
                                    i = False
                                    for x in info["cart"]:
                                        if change == x["Product"]:
                                            i = True # Here i represents if the product selected is available or not
                                            operation = input("\nEnter 'add' to add "
                                                              "product or 'sub' to remove products : ")
                                            quantity_change = int(input("Enter the change you want : "))
                                            position1 = info["Product"].index(change)
                                            if operation == "add":
                                                if quantity_change <= info["Quantity"][position1]:
                                                    x["Quantity"] = x["Quantity"] + quantity_change
                                                    info["Quantity"][position1] = \
                                                        info["Quantity"][position1] - quantity_change
                                                    print("Product quantity has been added to cart\n")
                                                else:
                                                    print(f"Product Quantity not available.\nAvailable quantity = "
                                                          f"{info['Quantity'][position1]}")
                                                    print("Press Enter to proceed again.")
                                                    keyboard.wait("Enter")
                                                    break

                                            elif operation == "sub":
                                                if quantity_change <= x["Quantity"]:
                                                    x["Quantity"] = x["Quantity"] - quantity_change
                                                    info["Quantity"][position1] = \
                                                        info["Quantity"][position1] + quantity_change
                                                    print("Selected quantity of product is removed from cart.")
                                                else:
                                                    print("Entered value exceeded from the value available in cart.")
                                                    print(f"Available Quantity in cart = {x['Quantity']}")
                                                    print("Press Enter to proceed again.")
                                                    keyboard.wait("Enter")
                                                    break

                                            else:
                                                print("Invalid Input")
                                                break

                                            cont_update = input("Enter 1 to update quantity of more products,"
                                                                " 2 to update cart or 3 to exit update :  ")
                                            if cont_update == "1":
                                                i = True
                                                continue_update_quantity = True
                                                break
                                            elif cont_update == "2":
                                                continue_update_quantity = False
                                                break
                                            elif cont_update == "3":
                                                continue_update_quantity = False
                                                continue_update = False
                                                show_cart()
                                                break
                                            else:
                                                print("Invalid Choice. Returning to update cart")
                                                continue_update_quantity = False
                                                break

                                    if not i:
                                        print("Product not found in cart")
                                        ch = input("Enter 1 to choose from other update option or any other key to "
                                                   "proceed again : ")
                                        if ch == "1":
                                            continue_update_quantity = False

                            elif update_choice == "2":
                                continue_delete = True
                                while continue_delete:
                                    delete_choice = input("\nWhich product you want to delete from your cart: ")
                                    index = 0
                                    position1 = info["Product"].index(delete_choice)
                                    i = False  # i is to check whether the product is available in cart or not
                                    for x in info["cart"]:
                                        if delete_choice == x["Product"]:
                                            i = True
                                            info["Quantity"][position1] = info["Quantity"][position1] + x["Quantity"]
                                            info["cart"].pop(index)
                                            break

                                    if i:
                                        print("Selected product has been removed from the cart.")
                                        continue_delete_choice = input("Enter 1 to continue deleting products "
                                                                       "from carts, 2 to continue updating cart or "
                                                                       "3 to exit update: ")
                                        if continue_delete_choice == "1":
                                            continue_delete = True
                                        elif continue_delete_choice == "2":
                                            continue_delete = False
                                        elif continue_delete_choice == "3":
                                            continue_delete = False
                                            continue_update = False
                                            show_cart()
                                        else:
                                            print("Invalid Choice! Returning to update cart again.")
                                            continue_delete = False

                                    elif not i:
                                        print("Product Not available in the cart.")
                                        continue_delete_choice = input("Enter 1 return to update screen or any other "
                                                                       "key to delete another product : ")
                                        if continue_delete_choice == "1":
                                            continue_delete = False
                                        else:
                                            continue_delete = True

                            elif update_choice == "3":
                                # First adding all the quantities of cart back to product list
                                for x in info["cart"]:
                                    position2 = info["Product"].index(x["Product"])
                                    info["Quantity"][position2] = info["Quantity"][position2] + x["Quantity"]
                                info["cart"].clear()
                                print("Your cart has been emptied")
                                proceed_choice = input("Enter 1 to return to update screen or 2 to finish update : ")
                                if proceed_choice == "1":
                                    print("Returning to cart update screen!")
                                    continue_update = True
                                elif proceed_choice == "2":
                                    print("Exiting from update cart.")
                                    show_cart()
                                else:
                                    print("Invalid choice! Returning to cart update screen.")
                                    continue_update = True

                            else:
                                print("Exiting from update cart screen!")
                                continue_update = False
                                show_cart()

                    def show_cart():
                        print("Product            Quantity            Rate")
                        for i in info["cart"]:
                            print(f"{i['Product']}            {i['Quantity']}                {i['Rate']}")

                        choice1 = input("Enter 1 to update cart, 2 to continue buying or 3 to complete purchase : \n")
                        if choice1 == "1":
                            update_cart()
                        elif choice1 == "2":
                            self.show_product()
                            self.add_to_cart()
                        elif choice1 == "3":
                            complete_purchase()
                        else:
                            print("Invalid Choice")

                    choice2 = input("Press 1 to continue buying, 2 to show your cart or 3 to complete your purchase: ")
                    print("\n")
                    if choice2 == "1":
                        self.show_product()
                        self.add_to_cart()
                    elif choice2 == "2":
                        show_cart()
                    elif choice2 == "3":
                        complete_purchase()
                    else:
                        print("Invalid Choice.")

                elif choice == "2":
                    self.add_to_cart()
                else:
                    print("Invalid choice.")

            else:
                print("Product Quantity not available. Choose a valid amount.")
                self.add_to_cart()

        else:
            print("Product not in stock. Please choose another one.")
            self.show_product()
            self.add_to_cart()
