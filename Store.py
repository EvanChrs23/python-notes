import random
import time
import string

products = []
cart = []

def generate_unique_ID():
    while True:
        uniqueID = ''.join(random.choice(string.ascii_letters, k=3)) + ''.join(str(random.randint(0,9)) for i in range(3))

        existing_id = {p["id"] for p in products}
        if uniqueID not in existing_id:
            return uniqueID 

def listProducts():
    print(f"\nList of products\n-------------------\n{'No':<4}{'ID':<10}{'Name':<12}{'Price':<10}{'Stock'}")
    for i,product in enumerate(products,1):
        print(f'{i}{".":<3}{product["id"]:<10}{product["name"]:<12}${product["price"]:<9.2f}{product["stock"]}')
    print('\n')

def confirmation():
    while True:
        option = input("Confirmation (y/n): ").strip().lower()
        if option == "y":
            return True
        elif option == "n":
            return False
        else:
            print("Invalid command")

def addProducts():
    productid = generate_unique_ID()

    while True:
        productname = input("Enter the product name: ").strip()
        existingNames = {p["name"].lower() for p in products}
        if productname.lower() in existingNames:
            print("The product you tried to input exists within the catalog")
        else:
            break
        
    while True:
        try:
            productprice = float(input("Enter the price: $"))
            if productprice <= 0:
                print("Price must be above 0")
            else:
                break
        except ValueError:
            print("Please input a valid price")

    while True:
        try:
            productstock = int(input("Enter the stock: "))
            if productstock <= 0:
                print("Stock must be above 0")
            else:
                break
        except ValueError:
            print("Please input a valid stock")

    print(f"Name = {productname:<12}Price = ${productprice:<9.2f}Stock = {productstock}")
    if confirmation():
        products.append({
        "id" : productid,
        "name" : productname,
        "price" : productprice,
        "stock" : productstock
        })
    else:
        print("Cancelling...")
        time.sleep(1)
        return
        
    print(f"{productname} has been added into the store")

def viewProducts():
    if not products:
        print("No products available")
        return
    listProducts()

def editProducts():
    if not products:
        print("No products available")
        return
    listProducts()
    
    editproduct = input("Please input the product ID you want to edit: ").strip()
    for product in products:
        if editproduct == product["id"]:
            editDetails = input("Which part do you want to edit?(name,price,stock): ").strip().lower()

            if editDetails == "name":
                newName = input("Enter the new name product: ").strip()
                existingNames = {p["name"].lower() for p in products if p != product}
                if newName.lower() in existingNames:
                    print("That name is already taken by another product (case-insensitive).")
                else:
                    if confirmation():
                        product["name"] = newName
                        print("Name updated successfully.")
                    else:
                        print("Cancelling...")
                        time.sleep(1)
                        return
            elif editDetails == "price":
                try:
                    newPrice = float(input("Enter the new price: $"))
                    confirmation()
                    product["price"] = newPrice
                    print("Price updated successfully.")
                except ValueError:
                    print("Please enter a number")
            elif editDetails == "stock":
                try:
                    newStock = int(input("Enter the new stock: "))
                    confirmation()
                    product["stock"] = newStock
                    print("Stock updated successfully.")
                except ValueError:
                    print("Please enter a number")
            else:
                print("Invalid command")

            break
    else:
        print("Invalid product ID")

def removeProducts():
    if not products:
        print("No products available")
        return
    listProducts()

    while True:
        removeproduct = input("Please input the product ID you want to remove: ").strip()
        for index,product in enumerate(products):
            if removeproduct == product["id"]:
                while True:
                    confirm = input("Are you sure? (Y/N): ").strip().lower()
                    if confirm == "y":
                        products.pop(index)
                        print(f"{product["name"]} has been removed")
                        return
                    elif confirm == "n":
                        print("Canceling...")
                        time.sleep(1)
                        return
                    else:
                        print("Invalid command")
        else:
            print("Invalid ID")

def addCart():
    if not products:
        print("No products available")
        return
    listProducts()

    while True:
        addProduct = input("Choose the ID of product to add into cart: ")
        for product in products:
            if addProduct == product["id"]: 
                while True:
                    try:
                        while True:
                            quantity = int(input(f"How many {product["name"]}s would you like? "))
                            if quantity <= 0:
                                print("Quantity must be over 0")
                            elif quantity > product["stock"]:
                                print(f"Not enough stock. Only {product['stock']} left.")
                            else:
                                break

                        if confirmation():
                            product["stock"] -= quantity
                            for item in cart:
                                if product["id"] == item["id"]:
                                    item["quantity"] += quantity
                                    break

                            else:
                                cart.append({
                                    "id" : product["id"],
                                    "name" : product["name"],
                                    "price" : product["price"],
                                    "quantity" : quantity}
                                    )
                                
                            print(f"{quantity} {product['name']}(s) added into your cart")
                            return
                        else:
                            print("Cancelling...")
                            time.sleep(1)
                            return

                    except ValueError:
                        print("Please enter a number")
        else:
            print("Invalid ID")

def viewCart():
    if not cart:
        print("Cart is empty")
        return 
    print(f"\nCart list\n-------------------\n{'No':<4}{'ID':<10}{'Name':<12}{'Price':<10}{'Quantity'}")
    for i, item in enumerate(cart,1):
        print(f'{i}{".":<3}{item["id"]:<10}{item["name"]:<12}${item["price"]:<9.2f}{item["quantity"]}')
    print()

def removeCart():
    if not cart:
        print("Cart is empty")
        return
    viewCart()

    while True:
        removeItem = input("Enter the item ID you want to remove: ").strip()
        for i,item in enumerate(cart):
            if removeItem == item["id"]:
                break
        else:
            print("Invalid ID")
            continue
    
        while True:
            try:
                quantity = int(input(f"How many {item["name"]}s do you want to remove? "))
                if quantity <= 0:
                    print("Quantity must be over 0")
                elif quantity > item["quantity"]:
                    print(f"You only have {item['quantity']} {item['name']} in your cart.")
                else:
                    break
            except ValueError:
                print("Please enter a number")
                
        if confirmation():
            for p in products:
                if p["id"] == item["id"]:
                    p["stock"] += quantity
                    break

            item["quantity"] -= quantity
            if item["quantity"] == 0:
                cart.pop(i)
                print(f"All of {item['name']} has been removed from your cart.")
            else:
                print(f"{quantity} {item['name']}(s) removed. {item['quantity']} left in cart.")
        else:
            print("Cancelling...")
            time.sleep(1)
        return

def checkout():
    if not cart:
        print("Your cart is empty")
        return

    print(f"\nCheckout Summary \n-------------------\n{'No':<4}{'Name':<12}{'Price':<10}{'Quantity':<10}{'Subtotal'}")
    grandtotal = 0
    for i, item in enumerate(cart,1):
        subtotal = item["price"] * item["quantity"]
        print(f'{i}{".":<3}{item["name"]:<12}${item["price"]:<9.2f}{item["quantity"]:<10}${subtotal:.2f}')
        
    grandtotal = sum(item["price"] * item["quantity"] for item in cart)
    print(f"-------------------\nTotal Price = ${grandtotal:.2f}\n")

    if confirmation():
        print("Processing payment...")
        time.sleep(1)
        cart.clear()
        print("Checkout complete! Cart has been cleared.\n")
    else:
        print("Checkout canceled.\n")
        time.sleep(1)

cmdbuyer = {
    "view" : viewProducts,
    "add" : addCart,
    "cart" : viewCart,
    "checkout" : checkout,
    "remove" : removeCart
}

cmdsell = {
    "view" : viewProducts,
    "add" : addProducts,
    "edit" : editProducts,
    "remove" : removeProducts
}

def buyer():
    while True:
        command = input("Enter a command (view,add,cart,checkout,remove,exit): ").strip().lower()
        print()
        if command == "exit":
            print("Exiting...")
            time.sleep(1)
            return
        elif command in cmdbuyer:
            cmdbuyer[command]()
        else:
            print("Invalid command")

def seller():
    while True:
        command = input("Enter a command (view,add,edit,remove,exit): ")
        if command == "exit":
            print("Exiting...")
            time.sleep(1)
            return
        elif command in cmdsell:
            cmdsell[command]()
        else:
            print("Invalid command")

cmdlist = {
    "seller" : seller,
    "buyer" : buyer,
}

def main():
    while True:
        user = input("What do you want to do? (Seller/Buyer/Exit): ").strip().lower()
        if user == "exit":
            print("Goodbye!!")
            time.sleep(0.5)
            return
        elif user in cmdlist:
            cmdlist[user]()
        else:
            print("Bruh")

main()