## Simple restaurant manager to work on OOP in Python

# Global variables
from curses.ascii import isdigit


yes_no = ['yes','no']
tables_list = []
guest_list=[]
times = ["17-19","19-21","21-23"]

class Restaurant: 
    ''' Restaurant class, basic info about restaurant '''
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"This is the {self.name} booking manager\nWelcome !\n")

    def tables(self):
        ''' Define a create list of tables '''
        result = input("How many tables in the restaurant ?: ")
        while result.isnumeric() is False and result not in range(1,20):
            print("Please provide a proper number !")
            result = input("How many tables in the restaurant ?: ")
        return list(range(1, int(result)+1))
        
    def seats(self):
        ''' Create a list of seats for each table'''
        result = []
        print("Please provide amount of seats for each table !")
        for s in range(len(tables)):
            table_seat = input(f"Table {s+1}: ")
            while table_seat.isdigit() is False:
                print('Please provide a correct number (1-10) !')
                table_seat = input(f"Table {s+1}: ")
            result.append(int(table_seat))

        return result
    
    def seats_to_tables(self):
        '''Create a dictionary with tables and seats accordingly'''
        result = dict(zip(tables, seats))
        return result

        
class Table(): 
    ''' Tables class, with name, seats, booking, prnting time slots itp.'''

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
        '''Printing timetable for table'''
        print(f"\nTable {self.name+1} time slots:")
        print(f"| {times[0]} | {times[1]} | {times[2]} |")
        for b in self.books:
            print("|{}| ".format("|".join(b)))
    
    def book_check(self):
        '''Checking if table booked, else returning a time slot avalible to book'''
        while True:
            choice = input('Please choose time slot: ')
            while choice not in times:
                choice = input('Please choose time slot: ')
            for t in times:
                if choice == t:
                    a = times.index(t)
            if self.books[0][a] == 'XXXXXXX':
                print("Table already booked !")
                return False
            else:
                return a
                    
    def fully_booked(self): 
        '''Fully book func'''
        booked = True
        for b in self.books[0]:
            if 'XXXXXXX' != b:
                booked = False
                break
            else:
                booked = True
        return booked

    def book_table(self, a):
        '''Actual booking func'''
        self.books[0][a] = 'XXXXXXX'
        print('Table booked !')


class Guest:
    '''Guest class with name,phone,guestes'''
    def __init__(self, name, phone, guests):
        self.name = name
        self.phone = phone 
        self.guests = guests

    def __str__(self):
        return f"{self.name}"
    
    def guest_creation(self):
        '''Printing if guest was created'''
        print(f"Guest {self.name} created !")

def new_guest():
    '''New guest creating func'''
    guest_name = input("Enter guest name: ")
    guest_phone = input("Enter guest phone number: ")
    while guest_phone.isnumeric() is False:
        print('Please provide correct phone number')
        guest_phone = input("Enter guest phone number: ")
    
    guest_guests = input("Enter the number of guest: ")
    while guest_guests.isnumeric() is False and int(guest_guests) > 10:
        print('Please provide a correct number !')
        guest_guests = input("Enter the number of guest: ")
    guest_new= Guest(guest_name,int(guest_phone),int(guest_guests))
    guest_new.guest_creation()
    return guest_new
            

def print_guest_list():
    '''Print guest list'''
    for i in range(len(guest_list)):
        print(f"{i+1}. {guest_list[i].name}")

def create_tables(): 
    '''Create tables and adding to a list!!!'''
    for i, val in enumerate(tables):
        tables_list.append(Table(i, [["       "] * len(times) for i in range(1)], s2t[i+1]))

##Creating new guest:

def guests(): 
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

####### Main logic

## Restaurant Main

rest1 = Restaurant(input("Please provide the name of the restaurant: "))
rest1.print_name()
tables = rest1.tables() ## How many tables
seats = rest1.seats() ## How many seates for each table
s2t = rest1.seats_to_tables() ## Seats together with tables
create_tables() ## Create tables
guests() ## Create guests


     
## Booking table
while True:
    choice = input('Would you like to booke a table ?: ')
    while choice not in yes_no:
        choice = input('Would you like to book a table ?: ')
    if choice.lower() == 'no':
        break
    else:
        fully_booked = True 
        for i, val in enumerate(tables_list): ## Check if fully booked
            if val.fully_booked() is not True:
                fully_booked = False
                break
            else:
                fully_booked = True
        if fully_booked is True:
            print('Sorry, restaurant is fully booked')
            break
        if len(guest_list) == 0:
            print('There are no guests !')
            break
        else:
            print_guest_list() 
            choice_guest = int(input('Please choose a guest: ')) - 1 ## Guest choice to make a booking
            while choice_guest not in range(len(guest_list)):
                choice_guest = int(input('Please choose a guest: ')) - 1
            else:
                no_seats = 0
                table_number = []
                for i,val in enumerate(tables_list): ## Checks if there is available tables for choosen amount of guests
                    if guest_list[choice_guest].guests > tables_list[i].seats:
                        no_seats += 1 ## For check if there are avalible tables
                    else:
                        table_number.append(i) ## Adding matching tables
                        tables_list[i].print_time_slots()
                if no_seats == len(tables_list): ## Check
                    print('There are no avalible tables for this guest !')
                    break
                else:
                    table_choice = int(input("Please choose a table number: ")) 
                    while table_choice - 1 not in table_number:
                        print("Please choose a valid number !")
                        table_choice = int(input("Please choose a table number: "))
                    else:
                        time_choice = tables_list[table_choice - 1].book_check()
                        tables_list[table_choice - 1].book_table(time_choice)
                        break
                
for i,val in enumerate(tables_list):
    tables_list[i].print_time_slots()

#### TO DO
## - MENU
## - create more functions out of main logic ! ! ! 

## What is working : can book a table, printing tables, creating restaurant

