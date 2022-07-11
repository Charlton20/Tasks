# Import the necessary modules
from __future__ import annotations
from os import path
from typing import List, Dict, Optional, Union
from tabulate import tabulate

Shoe_Dict = Dict[str, Union[int, float, str]]

# Allow the program to be run correctly from any working directory
inventory_txt = 'inventory.txt'
inventory_path = path.join(path.dirname(__file__), inventory_txt)


# Create a class called Shoe with the following attributes:
#     country: str    The shoe's country of origin
#     code: str       The shoe's SKU code
#     product: str    The shoe's product name
#     cost: int       The cost of the shoe
#     quantity: int   The quantity of the shoe in stock
class Shoe(object):

    country: str
    code: str
    product: str
    cost: Union[int, float]
    quantity: int

    # assign attributes & in it the details and list of strings
    def __init__(self, details: List[str]):

        self.country = details[0]
        self.code = details[1]
        self.product = details[2]
        self.cost = int(details[3])
        self.quantity = int(details[4])

    # Create a function called get_cost that gets the cost of a Shoe instance
    def get_cost(self):
        return self.cost

    # Create a function called get_quantity that gets the quantity of a Shoe instance
    def get_quantity(self):
        return self.quantity

    # Create a function called dict that returns a dictionary of the attributes details
    def dict(self):

        return {
            "Country": self.country,
            "Code": self.code,
            "Product": self.product,
            "Cost": self.cost,
            "Quantity": self.quantity,
        }

    # Create a method that converts an instance of Shoe into a string
    def __str__(self):
        value_list = self.dict().values()
        return ','.join(str(val) for val in value_list)


# Create an empty list that will be used to store a list of shoe objects
shoes: List[Shoe] = []


# Create a function called read_shoes_data that opens the inventory.txt file and reads the data, creates shoe object and
# appends this object into the shoe list
# Use try except for error handling in this function
# Create a count that counts the current shoe datat and adds that to the list
def read_shoes_data():
    try:
        shoes.clear()
        with open(inventory_path, 'r') as inventory:
            shoe_list: List[List[str]] = []
            count = 0
            for line in inventory:
                if count > 0:
                    current_shoe = line.strip().split(',')
                    shoe_list.append(current_shoe)

                count += 1

            if len(shoe_list) == 1:
                raise Exception(f"{inventory_txt} is empty!")
            elif len(shoe_list) == 0:
                raise Exception(f"There are no products in {inventory_txt}")

            capture_shoes(shoe_list)

    except OSError as error:
        print(error)
        raise Exception("Something went wrong while reading the file inventory.txt")


# Create a function called capture_shoes that allows te user to capture data about a shoe and use this datat to create a
# shoe object & append this object inside the shoe list
# I used try except error handling to avoid a logical error where .append() filled `shoes` with the most current item
def capture_shoes(shoe_list: List[List[str]]):

    for line, shoe in enumerate(shoe_list[:]):
        if len(shoe) != 5:
            raise Exception(f"{inventory_txt} is not in the correct format.")
        try:
            shoes.append(Shoe(shoe))
        except ValueError:
            print(f"Shoe data at line {line + 1} is incorrectly formed.")


# Create a function called view_all that iterates over all the shoes list and prints the details of the shoes
# Use the tabulate function to create a neat table of the data
def view_all():

    # Copy the values in shoes[]
    shoe_list = shoes[:]
    shoe_details: List[Dict[str, Union[int, float, str]]] = []

    for shoe in shoe_list:
        shoe_details.append(shoe.dict())
    print(tabulate(shoe_details, headers="keys"))


# I decided to create a function called positive_int that forces the user to enter a positive number
# This function will be used(called) under the re_stock & highest_qty functions
# Use Exception for error handling
# Got this idea from GitHub
def positive_num(value: Union[str, int]) -> int:

    new_value = int(value)
    if new_value < 0:
        raise Exception("Only a positive number is allowed here")
    return new_value


# Create a function called re_stock that will find the shoe object with the lowest quantity, which will be restocked
# Ask the user if they want to add the quantity of the shoes and then update it
def re_stock():

    lowest_index = 0

    # Copy the values in shoes[]
    shoes_ref = shoes[:]

    for i, shoe in enumerate(shoes_ref):
        if shoe.get_quantity() < shoes_ref[lowest_index].get_quantity():
            lowest_index = i

    shoe_with_lowest = shoes_ref[lowest_index]

    # Inform the user of the product with low stock (and its quantity)
    display_shoe(shoe_with_lowest, "Product with lowest quantity: ")

    # Add a new quantity to current stock
    shoes_ref[lowest_index].quantity += positive_num(input("How many shoes should be added to the current stock?: "))

    # Display the updated quantity with a confirmation message
    display_shoe(shoe_with_lowest, "Item updated: ")

    with open(inventory_path, 'r') as inventory:
        new_inv: List[str] = []

        # Start at -1 as the header line is not in the shoes list.
        for line, data in enumerate(inventory, start=-1):
            if line != lowest_index:
                new_inv.append(data.strip())
                continue
            else:
                new_inv.append(shoe_with_lowest.__str__())

    with open(inventory_path, 'w') as inventory:
        inventory.write('\n'.join(new_inv))
    read_shoes_data()


# Create a function that searches for a specific shoe using the shoe code and returns the object
def search_shoe():

    # Allow the user to only enter the number of the code
    code: str = input("SKU: ").strip()

    # If the code matches any one of the codes in 'code',then display the shoe with a confirmation message
    for shoe in shoes:
        if shoe.code == code:
            display_shoe(shoe, "Product found:")

            # Get out of the function
            return

    # Otherwise, print an error message
    print("No items with the SKU provided were found.")


# Create a function called value_per_item that calculates the total value of each item
# use the value formula (value = cost X quantity)
# Print the data in an easy-to-read format using the tabulate function
def value_per_item():

    shoe_data: List[Shoe] = shoes[:]
    new_data: List[Shoe_Dict] = []

    for i, shoe in enumerate(shoe_data):
        curr_shoe = shoe.dict()
        curr_shoe["Value"] = shoe.get_cost() * shoe.get_quantity()
        new_data.append(curr_shoe)

    print(tabulate(new_data, headers="keys"))


# Create a function called highest_qty that determines the product with the highest quantity & prints the shoe for sale
def highest_qty():

    shoes_ref = shoes[:]
    index_of_highest = 0
    quantity = 0

    for i, shoe in enumerate(shoes_ref):
        if shoe.get_quantity() > quantity:
            index_of_highest = i
            quantity = shoe.get_quantity()

    # Select the shoe with the highest quantity
    highest_qty_shoe = shoes[index_of_highest]
    display_shoe(highest_qty_shoe)

    # Allow for the user to enter their discount %
    discount_percent: int = positive_num(input("Discount percentage: "))

    # Calculate the percentage from the price and discount amount entered from the user
    highest_qty_shoe.cost *= +(1 - discount_percent / 100)

    # Display a message for the discount amount
    display_shoe(highest_qty_shoe, f"{discount_percent}% discount sale!!: ")


# Create a template for the output
item_template = '''
=====================
Product:    {Product}
Price:      R{Cost:.2f}
Country:    {Country}
Quantity:   {Quantity}
Code:       {Code}
=====================\
'''


# Create a function that displays details of a single shoe
def display_shoe(shoe: Shoe, message: Optional[str] = None):

    curr_shoe = shoe.dict()
    if message:
        print(message)
    print(item_template.format_map(curr_shoe))


# Call the functions according to the menu created below from a dictionary
# and assign these values(functions called) with keys of numbers
menu_dict = {
    '1': view_all,
    '2': re_stock,
    '3': search_shoe,
    '4': highest_qty,
    '5': value_per_item,
    '6': exit
}


# Create a user menu that compliments the dictionary above
menu = '''
What would you like to do?
1 - View all shoes
2 - Restock shoe with lowest quantity
3 - Search shoe by SKU
4 - Find shoe with highest quantity
5 - Assign a value to each item
6 - Exit the program '''

# Read inventory.txt contents to memory before the program starts.
read_shoes_data()


# If the option selected by the user is within the dictionary(menu_dict), then the program should print the menu
# Otherwise, the program should print an error message and allow the user to try again
while True:
    print(menu)
    option = input(": ")

    if option in menu_dict:
        menu_dict[option]()

    else:
        print("Incorrect option provided. Please try again")
