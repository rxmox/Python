# ENDG 233 Fall 2021
# Demonstration of classes and objects

class Horse:
    """A class used to create Horse object.

        Attributes:
            name (str): String that represents the horse's name
            age (int): Integer that represents the horse's age
            colour (str): String that represents the horse's colour
            breed (str): String that represents the horse's breed
            ***Note that self is implicit and is not included!
    """

    sci_name = "Equus caballus"
    """sci_name (str): Class variable with default string value of "Equus caballus"
    """

    def __init__(self, name, age, colour, breed):
        self.name = name 
        self.age = age
        self.colour = colour
        self.breed = breed

    def set_age(self, new_val):
        if new_val <= 0:
            print("Age must be greater than 0.")
        else:
            self.age = new_val
            print("Happy birthday!")

    def print_all_stats(self):
        print("""{0} stats: Age = {1}, Colour = {2}, Breed = {3}.""".format(self.name, self.age, self.colour, self.breed))


class Rider:
    """A class used to create Rider object.

        Attributes:
            name (str): String that represents the rider's name
            age (int): Integer that represents the rider's age
            horse (Horse): Horse object that represents the data for the rider's assigned horse
    """
    
    def __init__(self, name, age, horse):
        self.name = name
        self.age = age
        self.horse = horse

    def print_all_stats(self):
        print("""{0} stats: Age = {1}, Horse Age = {2}, Horse Colour = {3}, Horse Breed = {4}."""
        .format(self.name, str(self.age), str(self.horse.age), self.horse.colour, self.horse.breed))        


def main():
    print("\n***Horse and Rider Program***\n")

    # Class variable and method demo
    print("Sci name = " + Horse.sci_name)

    horse_demo1 = Horse("Blaze", 14, "bay", "Morgan")
    horse_demo2 = Horse("Socks", 14, "bay", "Morgan")

    print("Sci name = " + horse_demo1.sci_name)
    print("Sci name = " + horse_demo2.sci_name)

    Horse.sci_name = "Something else!"

    print("Sci name = " + horse_demo1.sci_name)
    print("Sci name = " + horse_demo2.sci_name)

    horse_demo1.sci_name = "Different value"

    print("Sci name = " + horse_demo1.sci_name)
    print("Sci name = " + horse_demo2.sci_name)

    Horse.sci_name = "Change again!"

    print("Sci name = " + horse_demo1.sci_name)
    print("Sci name = " + horse_demo2.sci_name)

    # Create five horses and five riders.
    horse1 = Horse("Blaze", 14, "bay", "Morgan")
    horse2 = Horse("Socks", 9, "grey", "Arabian")
    horse3 = Horse("Thunder", 20, "black", "Friesian")
    horse4 = Horse("Lightning", 14, "brown", "Quarter Horse")
    horse5 = Horse("Harry", 11, "grey", "Quarter Horse")

    rider1 = Rider("Alex", 34, horse1)
    rider2 = Rider("Jordan", 45, horse2)
    rider3 = Rider("Ali", 28, horse3)
    rider4 = Rider("Page", 20, horse4)
    rider5 = Rider("Jay", 14, horse5)

    # Test out the instance methods and see the impact
    horse1.set_age(15)
    print(horse1.age)

    horse1.print_all_stats()
    horse2.print_all_stats()

    rider5.print_all_stats()


if __name__ == '__main__':  # optional in Python 3, but recommended
    main()




