# =========== Import Libraries =============
# Yessir

from tabulate import tabulate

# ======== The beginning of the class ==========


class Shoe:
    '''
    Create a class called Shoe.
    '''
    # Create constructor method for the Shoe class.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        This method returns the cost of the shoes.
        '''
        print(f"The cost of {self.product} is R{self.cost:,}.")

    def get_quantity(self):
        '''
        This method returns the quantity of the shoes.
        '''
        print(f"The quantity of {self.product} is R{self.quantity:,}.")

    def __str__(self):
        '''
        This method returns a string representation of a class.
        '''
        return (
            f"\n====== Shoe data ======"
            f"\nCountry:  {self.country} \nCode:     {self.code}"
            f"\nProduct:  {self.product} \nCost:     {self.cost}"
            f"\nQuantity: {self.quantity}"
                )

    def enlist(self):
        '''
        This method will return the attributes of an object in a list
        format.
        '''
        return [
            self.country, self.code, self.product, self.cost, self.quantity
                ]


# ============== Functions outside the class ===============


def read_shoes_data():
    '''
    This method reads data from the inventory text files, and appends
    the objects in the file to the shoe_list.

    :param file inventory.txt:  Text file which contains shoe data.

    :returns: attributes for Shoe in a list.

    :return type: object
    '''
    try:
        # Open the inventory file which contains shoe data.
        with open("inventory.txt", "r", encoding="utf-8") as file:
            # Skip the 1st line
            next(file)

            # Create empty shoe list, to append latest data.
            shoe_list = []

            # Loop through each line in the file and store the attributes
            # of each object in a list. Use 1 index to skip the 1st line.   
            for line in file:
                shoe_data = line.strip()
                shoe_data = shoe_data.split(",")

                # Append each object/line to the shoe_list.                               
                shoe_list.append(
                    Shoe(shoe_data[0], shoe_data[1], shoe_data[2],
                         shoe_data[3], shoe_data[4])
                    )

            return shoe_list

    except FileNotFoundError:
        print("Please ensure the file is saved before accessing it!")


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.

    :param str country_input: Location of the shoe.
    :param str code_input:  Product code of the shoe.
    :param str product: Product description.
    :param int cost:    Cost of the shoe.
    :param int quantity:    Quantity of the shoe.

    :returns:   An object in a list and text file.
    :return type:   Object.
    '''
    # Prompt user to enter the attributes of Shoe.
    country_input = input("Please enter country:    ")
    code_input = input("Please enter shoe code: ")
    product_input = input("Please enter the shoe product:   ")
    cost_input = int(input("Please enter the cost of the shoe:  "))
    quantity_input = int(input("Please enter the quantity:  "))

    # Add the attributes to inventory file
    with open("inventory.txt", "a", encoding="utf-8") as file:
        file.write(
            f"\n{country_input},{code_input},{product_input},"
            f"{cost_input},{quantity_input}"
            )

    print("\nShoe captured successfully!")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # Read the shoes data from the text file
    shoe_list = read_shoes_data()

    # Create an iterable shoe list(2D List).
    shoes_data = [shoe.enlist() for shoe in shoe_list]

    # Create headers since the 1st row in removed from the read_shoes_data
    # function.
    shoe_headers = ["Country", "Code", "Product", "Cost", "Quantity"]

    # Print the data in a table.
    shoe_presentation = tabulate(
                shoes_data, headers=shoe_headers, tablefmt="grid"
                    )
    print(shoe_presentation)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.

    :param list shoe_list:  List of shoe objects.

    :returns:   Update shoe quantity.

    :return type:   Integer.
    '''
    # Read the shoes data from the text file
    shoe_list = read_shoes_data()

    # Empty list for quantities.
    shoe_quantities = []

    for shoe in shoe_list:
        # Cast shoe quantity as integer since it comes as a string from
        # the text file.
        shoe_quantities.append(int(shoe.quantity))

    # Determine the product with the lowest quantity.
    min_quantity = min(shoe_quantities)

    # Loop through the quantity list and return product with lowest quantity.
    for shoe in shoe_list:
        if int(shoe.quantity) == min_quantity:
            print(f"{shoe.product} has the lowest quantity ({min_quantity}).")

            # Update the lowest quantity.
            re_stock = int(input(
                    "Please enter the quantity to be purchased: "
                        ))
            new_stock = int(shoe.quantity) + re_stock
            shoe.quantity = new_stock

            try:
                with open("inventory.txt", "w", encoding="utf-8") as file:
                    # Insert headers since they were removed in the shoe_list.
                    file.write("Country,Code,Product,Cost,Quantity")

                    # Iterate through the show list and overwrite existing data
                    # in the inventory.txt file with the updated data.
                    for i, shoe in enumerate(shoe_list):
                        file.write(f"\n{shoe.country},{shoe.code},"
                            f"{shoe.product},"
                            f"{shoe.cost},{shoe.quantity}"
                                )
            except StopIteration:
                print("File corrupted, please contact Administrator!")

            print("Quantity updated successfully!\n")

    return shoe_quantities


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.

     :param str code:   Shoe code.

     :returns:  Attributes of the shoe object using the code.

     return type:   str
    '''
    # Read the shoes data from the text file.
    shoe_list = read_shoes_data()

    # Empty list where codes will be appended.
    codes = []

    # Loop through shoe_list and append codes to the codes list.
    for shoe in shoe_list:
        shoe_code = shoe.code
        codes.append(shoe_code)

    # Check if code exists.
    while True:

        # Prompt user to enter shoe code.
        shoe_code_input = input("Please enter shoe code:    ").upper()

        if shoe_code_input in codes:
            # If code exists, print the object as a string.
            for shoe in shoe_list:
                if shoe_code_input == shoe.code:
                    print(shoe)
            break

        else:
            print("The code does not exist!\n")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.

    :param int cost:        The shoe cost.
    :param int quantity:    The shoe quantity.

    :returns:               The value of a shoe.

    :return type:           Integers.
    '''
    # Read the shoes data from the text file.
    shoe_list = read_shoes_data()

    # Create empty list where I will append the product and value for
    # each item.
    values = []

    values_headers = ["No", "Product", "Value"]

    # Loop through the shoe_list.
    for i, shoe in enumerate(shoe_list, start=1):
        value_pu = int(shoe.cost) * int(shoe.quantity)
        values.append([f"{i}", f"{shoe.product}", f"{value_pu:,}"])

    # Create table.
    value_presentation = tabulate(
                        values, headers=values_headers, tablefmt="grid"
                )
    return value_presentation


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Read the shoes data from the text file
    shoe_list = read_shoes_data()

    # Empty list for quantities.
    shoe_quantities = []

    for shoe in shoe_list:
        # Cast shoe quantity as integer since it comes as a string from
        # the text file.
        shoe_quantities.append(int(shoe.quantity))

    # Determine the product with the highest quantity.
    max_quantity = max(shoe_quantities)

    # Loop through the quantity list and return product with lowest quantity.
    for shoe in shoe_list:
        if int(shoe.quantity) == max_quantity:
            print(f"{shoe.product} is on SALE!!!!\n")


# ==========Main Menu=============

while True:
    print(
        "Welcome to the Inventory Management Application!"
        "\n 1   -   Capture new inventory."
        "\n 2   -   View all inventory on hand."
        "\n 3   -   Order stock with lowest quantity."
        "\n 4   -   Search for stock."
        "\n 5   -   Display stock values."
        "\n 6   -   Place overstocked inventory on sale."
        "\n 7   -   Close application."
        )

    option = input("\nPlease select an option from the menu (1 to 7):   ")

    if option == "1":
        capture_shoes()
        print()

    elif option == "2":
        view_all()
        print()

    elif option == "3":
        re_stock()
        print()

    elif option == "4":
        search_shoe()
        print()

    elif option == "5":
        print(value_per_item())
        print()

    elif option == "6":
        highest_qty()
        print()

    elif option == "7":
        exit()
        print()

    else:

        print("\nOption does not exist. Please select an option from the menu!")
        print()
