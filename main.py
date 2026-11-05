import json
from pydantic_classes import Material, Recipe, Product, WorkOrder


#GLOBALS
FILEPATHS = ["materials.json", "products.json", "recipes.json", "work_orders.json"]

#Main Loop for object intialization
#For every JSON file, create a corresponding class and initialize the objects as a list
#Name it after the file name minus the .json affix

for file in FILEPATHS:
    name = file.split(".")[0]
    with open(file, "r") as data:
        raw_data = json.load(data)
        #List comprehension replaces a complicated for loop here
        #This is slightly awkward due to trying to loop into a Class constructor with differing 
        #names
        if name == "materials":
            materials = [Material(**item) for item in raw_data]
        elif name == "products":
            products = [Product(**item) for item in raw_data]
        elif name == "recipes":
            recipes = [Recipe(**item) for item in raw_data]
        elif name == "work_orders":
            work_orders = [WorkOrder(**item) for item in raw_data]
        else:
            print("Error: Invalid file name")
            exit
        #Since were looping over all the filenames, all these elifs will be hit.

# Because we have used pydantic to create these classes, the objects have been validated 
# There are no missing feilds, and all types have been validated on object creation. There 
# should be no type mis matching further down the code.

