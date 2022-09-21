from unicodedata import name


## Simple restaurant manager to work on OOP in Python

class Restaurant:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"This is the {self.name} bookin manager\n Welcome !\n")

    def tables(self):
        tables = input("How many tables in the restaurant ?: ")
        while tables not in '1234567890':
            print("Please provide a proper number !")
            tables = input("How many tables in the restaurant ?: ")
        print("Tables saved in the system !")
        return int(tables)

    def guests(self):
        seats = []
        print("Please provide amount of seats for each table !")
        for i in range(int(tables)):
            seats.append(int(input(f"Table {i+1}: ")))
        return sum(seats)

    
azur = Restaurant("Coolio")
azur.print_name()
tables = azur.tables()
print(f"There are {tables} tables in the restaurant")
seats = azur.guests()
print(f"There are {seats} seats available at {tables} tables.")
