# ENDG 233 F21 - Term Test #2 Written Response (5 marks)
# Omar Ahmed


# INSTRUCTIONS:
# The following program should allow you to filter a dictionary based on given parameters.
# The main code is already implemented. 
# You must complete the function filter_distances without changing the function definition.
# You must use a list or dictionary comprehension to do the filtering.
# A screenshot of example input/output has been provided.
# You may not modify any of the given code or add code outside of the filter_distances function.


def filter_distances(closest, furthest, stores):
    """This function filters a given dictionary based on the provided upper and lower bounds.

    Args:
        closest (int): Smallest distance
        furthest (int): Furthest distance
        stores (dict): A dictionary that maps stores to their proximity (kms).

    Returns:
        dict: Returns a dictionary that only contains key-value pairs where the value is within or equal to the specified bounds.
    """

    return {store: distance for store, distance in stores.items() if closest <= distance <= furthest}

# Main code begins here
print('ENDG 233 Term Test #2\n')

# Stores and their distances from your location
store_distances = {'Walmart North':4,'Shoppers Drug Mart':8,'Staples':10,'Grand & Toy':20,'Walmart South':31,'Dollarama':15,'Winners':6,'Canadian Tire':23,'London Drugs':14}

# Returned dictionary should include all key:value pairs where the value is within or equal to the given limits.
furthest = 25
closest = 5

# Function call
print(filter_distances(closest, furthest, store_distances))
