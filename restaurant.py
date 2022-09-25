## Simple restaurant manager to work on OOP in Python

# Global variables
yes_no = ['yes','no']
tables_list = []

class Restaurant:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"This is the {self.name} booking manager\nWelcome !\n")

    def tables(self):
        result = int(input("How many tables in the restaurant ?: "))
        while result not in range(1,20):
            print("Please provide a proper number !")
            result = int(input("How many tables in the restaurant ?: "))
        return list(range(1, int(result)+1))
        
    def seats(self):
        result = []
        print("Please provide amount of seats for each table !")
        for s in range(len(tables)):
            result.append(int(input(f"Table {s+1}: ")))
        return result
    
    def seats_to_tables(self):
        result = dict(zip(tables, seats))
        return result

        
class Table():

    time_slots = {}
    times = ["17-19","19-21","21-23"]

    def __init__(self, name, books, seats):
        self.name = name
        self.books = books
        self.seats = seats

    def __str__(self):
        return f"Seats number {self.seats}"
        
    # def time_slots(self): ## not sure if needed
    #     time_slots = {}
    #     times = ["17-19","19-21","21-23"]
    #     for number in tables:
    #         time_slots[number] = times
    #     return time_slots

    def print_time_slots(self):
        print(f"\nTable {self.name+1} time slots:")
        print(f"| {self.times[0]} | {self.times[1]} | {self.times[2]} |")
        for b in self.books:
            print("|{}| ".format("|".join(b)))
    
    def book_check(self):
        while True:
            choice = input('Please choose time slot: ')
            while choice not in self.times:
                choice = input('Please choose time slot: ')
            for t in self.times:
                if choice == t:
                    a = self.times.index(t)
            if self.books[0][a] == 'XXXXXXX':
                print("Table already booked !")
                return False
            else:
                return a
                    
    def fully_booked(self):
        booked = True
        for b in self.books[0]:
            if 'XXXXXXX' != b:
                booked = False
                break
            else:
                booked = True
        return booked

    def book_table(self, a):
        self.books[0][a] = 'XXXXXXX'
        print('Table booked !')


class Guest:
    def __init__(self, name, phone, guests):
        self.name = name
        self.phone = phone 
        self.guests = guests

    def __str__(self):
        return f"{self.name}"
    
    def guest_creation(self):
        print(f"Guest {self.name} created !")

def new_guest():
    guest_name = input("Enter guest name: ")
    guest_phone = input("Enter guest phone number: ")
    guest_guests = input("Enter the number of guest: ")
    guest_new= Guest(guest_name,guest_phone,guest_guests)
    guest_new.guest_creation()
    return guest_new

def print_guest_list():
    for i in range(len(guest_list)):
        print(f"{i+1}. {guest_list[i].name}")

def create_tables():
    for i, val in enumerate(tables):
        tables_list.append(Table(i, [["       "] * len(tables) for i in range(1)], s2t[i+1]))


# def table_book():


####### Main logic

## Restaurant Main

rest1 = Restaurant(input("Please provide the name of the restaurant: "))
rest1.print_name()
tables = rest1.tables()
seats = rest1.seats()
s2t = rest1.seats_to_tables()
create_tables()





##Creating new guest:
guest_list=[]

while True:
    
    choice = input('Would you like to add a new guest ?: ')
    while choice not in yes_no:
        choice = input('Would you like to add a new guest ?: ')
    if choice.lower() == 'no':
        break
    else:
        for i in range(1):
            new=new_guest()
            guest_list.append(new)
            
## Booking table
while True:
    choice = input('Would you like to booke a table ?: ')
    while choice not in yes_no:
        choice = input('Would you like to booke a table ?: ')
    if choice.lower() == 'no':
        break
    else:
        fully_booked = True
        for i, val in enumerate(tables_list):
            if val.fully_booked() != True:
                fully_booked = False
                break
            else:
                fully_booked = True
        if fully_booked == True:
            print('Sorry, restaurant is fully booked')
            break
        else:
            print_guest_list()
            choice_guest = int(input('Please choose a guest: ')) - 1
            while choice_guest not in range(len(guest_list)):
                choice_guest = int(input('Please choose a guest: ')) - 1
            else:

                # for i,val in enumerate(tables_list):
                    # if guest_list[choice_guest - 1].guests <= tables_list[i].
                break

        



## Printing time table


for i, val in enumerate(tables_list):
    if val.fully_booked() is True:
        pass
    else:
        val.print_time_slots()

## work here, making a booking
## it should containn guest, avalible time, avalible seats(acording to guest amount), 
table_choice = objs[1].book_check()

for i, val in enumerate(tables_list):
    if val.fully_booked()==True:
        pass
    else:
        val.print_time_slots()

