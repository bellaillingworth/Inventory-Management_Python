# -*- coding: utf-8 -*-
"""
An interactive Python app that manages grocery inventory using a CSV file for storage.
Features include adding, updating, removing, searching, and displaying products 
with input validation and category value summaries.

"""

from utilities import safe_input

product_id = 1 #Initialize the productID 
inventory = {} #Initialize an empty dictionary which will have ProductID as the Key

#Advanced feature
#Load info from CSV file
f = open('inventory.csv', 'r')

for line in f: #Interate over the file 
    item = line.split(',')
    
    #Assign variable for each column
    ID = int(item[0])
    name = item[1]
    category = item[2]
    price = float(item[3])
    quantity = int(item[4])
    
    #Go through each ProductID in the file and add the info in the inventory dictionary
    if ID >= product_id:
        product_id = ID + 1
    inventory[ID] = {
        'name': name,
        'category': category,
        'price': price,
        'quantity': quantity
        }

f.close()

#Display the options
print("Welcome to Grocery Store Inventory Management!")

options = """1. (N) Add a new product
2. (R) Remove a product
3. (C) Clear all products
4. (D) Display a product's inventory
5. (U) Update a product
6. (A) Display all products
7. (V) Calculate total value per category
8. (S) Search for a product
9. (O) Display the options
10. (E) Exit"""

print(options)

while True: 
    #Display this input until the user wants to stop the loop
    choice = input('Enter your choice: ') 
    
# Use "safe_input" function for all numerical inputs such as productID, quantity, and price
    
    if choice == '1' or choice == 'N' or choice == "n":
        #Get the product information
        name = input('Name: ').title() #Capitalizes the first letter of each word
        category = input('Category: ').title() #Capitalizes the first letter of each word
        price = safe_input("Price: ", "ERROR: Price must be a positive numeric value.", float, 0, None)
        quantity = safe_input("Quantity: ", "ERROR: Quantity must be a positive integer value.", int, 0, None)
    
        #Load the inputs into dictionary
        inventory[product_id] = {'name': name,
                                 'category': category,
                                 'price': price,
                                 'quantity': quantity,
            }#Create the product's information dictionary within the inventory dictionary
       
        product_id += 1 #New productID for a new product
        
        #Display a message that lets the user know that the product has been added
        print('Item added successfully') 

    elif choice == '2' or choice == 'R' or choice == "r":
        productid = safe_input("Enter the ID of the product to remove: ", 
                               "ERROR: ProductID must be a positive integer value.", int, 0, None)
        
        #Display a message if the user enters the wrong ID
        if productid not in inventory: 
            print('No product with that ID found')
            continue
        
        else: #Remove the product according to the number of productID the user provided
            inventory.pop(productid)
            print("Item removed successfully!")
    
    elif choice == '3' or choice == 'C' or choice == "c":
        #Display a confirmation message
        confirm = input("Are you sure you want to clear all products? (Y/N): ").lower()
        
        #Process to clear all products
        if confirm == 'y':
            inventory.clear()
            print("All products has been cleared.")
        else: #Cancele the choice
            continue
        
    elif choice == '4' or choice == 'D' or choice == "d":
        productid = safe_input("Enter the ID of the product to display:  ", 
                               "ERROR: ID must be a positive integer value.", int, 0, None)
    
        if productid in inventory: #Pull the info from distionary using productid
            name = inventory[productid]['name']
            category = inventory[productid]['category']
            price = inventory[productid]['price']
            quantity = inventory[productid]['quantity']
            
            #Display the info
            print(f"ID: {productid}")
            print(f"Name: {name}")
            print(f"Category: {category}")
            print(f"Price($): {price:.2f}")
            print(f"Quantity: {quantity}")
            
        else: #Display a message if the user enters the wrong ID
            print('Item not found!')
            
    elif choice == '5' or choice == 'U' or choice == "u":
        productid = safe_input("Enter the ID of the product to update: ", 
                               "ERROR: ID must be a positive integer value.", int, 0, None)
        
        if productid in inventory: 
            new_price = safe_input(f"Enter the new price for '{inventory[productid]['name']}': $", 
                                   "ERROR: Price must be a positive numeric value.", float, 0, None)
            
            new_quan = safe_input(f"Enter the new quantity for '{inventory[productid]['name']}': ", 
                                  "ERROR: Quantity must be a positive integer value.", int, 0, None)
                
            #Update the new price and quantity of that productID
            inventory[productid]['price'] = new_price
            inventory[productid]['quantity'] = new_quan
            
            print('Item updated successfully!')
            
        else:
            #If the product ID has not existed, display an error message
            print('Item not found!')
    
    elif choice == '6' or choice == 'A' or choice == "a":
        #Header
        print("-" * 85)
        print(f"{'ID':<4} {'Name':<40} {'Category':<15} {'Price($)':<10} {'Quantity':>1}")
        print("-" * 85)
        
        for key in inventory: #Iterate over each item in dictionary
            #Extract details 
            name = inventory[key]['name']
            category = inventory[key]['category']
            price = inventory[key]['price']
            quantity = inventory[key]['quantity']
            
            #Print each row 
            print(f"{key:<4} {name:<40} {category:<15} {price:<10.2f} {quantity:>1}")
    
    elif choice == '7' or choice == 'V' or choice == "v":

         categories = {} #Create a new dictionary for categories
         
         for product_id in inventory:
             category = inventory[product_id]['category']
             price = inventory[product_id]['price']
             quantity = inventory[product_id]['quantity']
             
             #Check if the category is already in the dictionary
             #If so, add the new value to the previous value of that category
             #If not, that category is the key and price times quantity is the value
             if category not in categories:
                categories[category] = price * quantity
             else:
                categories[category] += (price * quantity)
                
         #Header
         print("-" * 25)
         print(f"{'Category':<15} {'Value':<10}")
         print("-" * 25)
         
         #Display the value for each category
         total = 0
         for category in categories:
             value = categories[category]
             total += value
             print(f"{category:<15} ${value:<10.2f}")
             
         #Display the total value of all products in the last row outside the loop
         print(f"{'All Products':<15} ${total:<10.2f}")
        
        
    elif choice == '8' or choice == 'S' or choice == "s":
        
        #Take the input that is case insensitive and allow partial matches
        product_name = input('Enter the name of the product to search: ').lower()
        
        for product_id, values in inventory.items(): #Iterate through products in inventory
            
            if product_name in values['name'].lower(): #Check for the match substring of the item's name
                #Extract details
                name = inventory[product_id]['name']
                category = inventory[product_id]['category']
                price = inventory[product_id]['price']
                quantity = inventory[product_id]['quantity']
                
                #Display the item info
                print(f"ID: {product_id}")
                print(f"Name: {name}")
                print(f"Category: {category}")
                print(f"Price: {price:.2f}")
                print(f"Quantity: {quantity}")
            
        
    elif choice == '9' or choice == 'O' or choice == "o":
        #Display the options
        print(options)
        
    elif choice == '10' or choice == 'E' or choice == 'e':
        #Stop the loop and display a 'Goodbye' message
        print("Goodbye!")
        break
    else:
        #Display an error message if the user enters an option that is not in the options
        print("Invalid option entered. Enter 9 or o to see the options.")

# Save updated inventory to csv file

#Empty the file
f = open('inventory.csv', 'w')
f.write('')
f.close()

#Adding the updated information to the empty file
f = open('inventory.csv', 'a')

#Loop through each item in the inventory dictionary
for item in inventory:
    #Extract value for each item(productID)
    #Separate each value by a comma
    entry = f"{item},{inventory[item]['name']},{inventory[item]['category']},{inventory[item]['price']},{inventory[item]['quantity']}\n"
    
    #Writing the info extracted from each item into the CSV file
    f.write(entry)
    
f.close()
