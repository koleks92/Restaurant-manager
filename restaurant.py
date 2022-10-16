## Simple restaurant manager to work on OOP in Python
from curses.ascii import isdigit

''' 
TO DO
-Print guest info next to the time table
-Make printing table more dynamic (fx if times changed, tables automaticly expands etc. !)
-Screen clear !
- Maybe GUI to practice ?
- 
'''

# Global variables

yes_no = ['yes', 'no', 'y', 'n']
tables_list = []
guest_list=[]
times = ["17-19","19-21","21-23"] ## Avaliable times to book a table


def main():
    global rest1
    global tables
    global table_seats
    global s2t
    rest1 = Restaurant(input("Please provide the name of the restaurant: "))
    tables = rest1.tables() ## How many tables
    table_seats = rest1.seats() ## How many seates for each table
    s2t = rest1.seats_to_tables() ## Seats together with tables
    create_tables() ## Create tables
    
## MENU 
    rest1.print_name()
    menu=Menu() ## Create Menu
    while True:
        menu.print_menu() ## Print Menu
        choice_5 = menu.menu_choice_5()
        if choice_5 == '5': ## Exit
            menu.exit()
        elif choice_5 == '4': ## Restaurant Menu
            while True:
                menu.restaurant()
                choice_3 = menu.menu_choice_3()
                if choice_3 == '3': ## Go back to main menu
                    break
                elif choice_3 == '2': ## Create a new restaurant
                    rest1 = Restaurant(input("Please provide the name of the restaurant: "))
                    tables = rest1.tables() ## How many tables
                    seats = rest1.seats() ## How many seates for each table
                    s2t = rest1.seats_to_tables() ## Seats together with tables
                    create_tables() ## Create tables
                    print('New restaurant created !')
                    input('Press ENTER to continue: ')
                    break
                elif choice_3 == '1': ## Restart restaurant
                    create_tables()
                    print('Restaurant restarted !')
                    input('Press ENTER to continue: ')
                    break

        elif choice_5 == '3': ## Print Time Table
            while True:
                menu.time_table()
                print(' ')
                input('Press ENTER to continue: ')
                break

        elif choice_5 == '2': ## Booking system
            while True:
                menu.booking()
                choice_3 = menu.menu_choice_3()
                if choice_3 == '3': ## Go back to main menu
                    break
                elif choice_3 == '2': ## Remove booking
                    remove_booking()
                    input('Press ENTER to continue !')
                elif choice_3 == '1': ## Book a table
                    booking()
                    input("Press ENTER to continue: ")

        elif choice_5 == '1': ## Guest managment
            while True:
                menu.guests()
                choice_3 = menu.menu_choice_3()
                if choice_3 == '3': ## Go back to main menu
                    break
                elif choice_3 == '2': ## Remove/edit guest
                    while True:
                        menu.guests_modify()
                        choice_3 = menu.menu_choice_3()
                        if choice_3 == '3': ## Go back to guest menu
                            break
                        elif choice_3 == '2': ## Remove a guest
                            if len(guest_list) == 0: ## Check if there a guests to remove
                                print('There are no guests !')
                                input('Press ENTER to continue !')
                                break
                            guest_remove()
                            input('Press ENTER to continue !')
                        elif choice_3 == '1': ## Edit a guest
                            if len(guest_list) == 0: ## Check if there a guests to remove
                                print('There are no guests !')
                                input('Press ENTER to continue !')
                                break
                            guest_edit()
                            input('Press ENTER to continue !')
                            
                elif choice_3 == '1': ## Add a guest
                    new_guest()
                    input('Press ENTER to continue: ')
                    break



class Menu:
    ''' Menu class'''
    def print_menu(self):
        '''Printing main menu'''
        print("1.Guests")
        print("2.Booking")
        print("3.Time table")
        print("4:Restaurant")
        print("5.Exit")
        print("")

    def menu_choice_5(self):
        '''Five choice menu'''
        menu_choice = input('Please choose a number: ')
        while menu_choice.isnumeric() is False and menu_choice not in '12345':
            print("Please provide a correct number (1-5) !")
            menu_choice = input('Please choose a number: ')
        return menu_choice

    def menu_choice_3(self):
        '''Three choice menu'''
        menu_choice = input('Please choose a number: ')
        while menu_choice.isnumeric() is False and menu_choice not in '123':
            print("Please provide a correct number (1-5) !")
            menu_choice = input('Please choose a number: ')
        return menu_choice
    
    def guests(self):
        '''Guests menu'''
        print("1.Add a new guest")
        print("2.Remove or edit a guest")
        print("3.Go back to Main Menu")
        print('')

    def guests_modify(self):
        '''Guest submenu - Edit or remove'''
        print("1.Edit a guest")
        print("2.Remove guest")
        print("3.Go back to Guest Menu")
        print('')


    def booking(self):
        '''Booking menu'''
        print("1.Make a new booking")
        print("2.Remove a booking")
        print("3.Go back to Main Menu")
        print('')

    def time_table(self):
        '''Printing Timetable'''
        for i,val in enumerate(tables_list):
            tables_list[i].print_time_slots()
        

    def restaurant(self):
        '''Restaurant menu'''
        print("1.Restart restaurant !")
        print("2.Create a new restaurant !")
        print("3.Go back to Main menu")
        print('')

    def exit(self):
        '''Exit program menu'''
        choice_exit = input("Are you sure you want to quit ?: ")
        while choice_exit.lower() not in yes_no:
            print("Please provide a valid answer(yes or no) !")
            choice_exit = input("Are you sure you want to quit ?: ")
        if choice_exit.lower() == 'yes' or 'y':
            quit()
        else:
            self.print_menu()
            


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
        result = dict(zip(tables, table_seats))
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
                print('Please provide a correct time slot !')
                choice = input('Please choose time slot: ')
            for t in times:
                if choice == t:
                    a = times.index(t)
            if self.books[0][a] == 'XXXXXXX':
                print("Time already booked !")
                return False
            else:
                return a
    
    def unbook_check(self):
        '''Checking if table booked, else returning a time slot avalible to book'''
        while True:
            choice = input('Please choose time slot: ')
            while choice not in times:
                print('Please provide a correct time slot !')
                choice = input('Please choose time slot: ')
            for t in times:
                if choice == t:
                    b = times.index(t)
            if self.books[0][b] == '       ':
                print("Time is not booked!")
                return False
            else:
                return b

                    
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

    def unbook_table(self, b):
        '''Remove booking func'''
        self.books[0][b] = '       '
        print('Booking removed !')


class Guest:
    '''Guest class with name,phone,guestes'''
    def __init__(self, name, phone, guests, b_table = -1, b_time = -1):
        self.name = name
        self.phone = phone 
        self.guests = guests
        self.b_table = b_table ## Booked table
        self.b_time = b_time ## Booked time

    def __str__(self):
        print(self.b_table)
        print(self.b_time)
        return f"{self.name}"
           
    def guest_creation(self):
        '''Printing if guest was created'''
        print(f"Guest {self.name} created !")

    def book_check(self):
        if self.b_table != -1 and self.b_time != -1:
            return True
        else:
            return False
    
    

def new_guest():
    '''New guest creating func'''
    guest_name = input("Enter guest name: ") ## Name
    guest_phone = input("Enter guest phone number: ")
    while guest_phone.isnumeric() is False: ## Phone number
        print('Please provide correct phone number')
        guest_phone = input("Enter guest phone number: ")
    guest_guests = input("Enter the number of guests: ")
    while guest_guests.isnumeric() is False: ## Number of guests
        print('Please provide a correct number !')
        guest_guests = input("Enter the number of guests: ")
    while int(guest_guests) > 10: ## Check for maximum number of guestes
        print('Maximum number of guests is 10 !')
        guest_guests = input("Enter the number of guest: ")
    guest_new = Guest(guest_name,int(guest_phone),int(guest_guests)) ## Create a guest
    guest_list.append(guest_new)
    guest_new.guest_creation() ## Print info

def guest_remove():
    '''Guest removal function'''
    print_guest_list()
    choice_guest = input('Please choose a guest: ') ## Guest choice to remove
    while choice_guest.isnumeric() is False and choice_guest not in range(len(guest_list)):
        choice_guest = input('Please choose a guest: ')
    remove_choice = input(f"Do want to remove {guest_list[int(choice_guest) - 1].name} ?: ") ## Confirmation
    while remove_choice not in yes_no:
        remove_choice = input(f"Do want to remove {guest_list[int(choice_guest) - 1].name} ?: ")
    if remove_choice.lower() == 'yes' or 'y':
        guest_list.remove(guest_list[int(choice_guest) - 1]) ## Remove a gust from a list
        print("Guest removed !")
    else:
        print('Guest not removed !')

def guest_edit():
    '''Guest edit function'''
    print_guest_list()
    choice_guest = input('Please choose a guest: ') ## Guest choice to edit
    while choice_guest.isnumeric() is False and choice_guest not in range(len(guest_list)):
        choice_guest = input('Please choose a guest: ')
    guest_name = input("Enter new guest name (ENTER to skip): ") ## Name
    if guest_name == '':
        guest_name = guest_list[int(choice_guest) - 1].name
    guest_phone = input("Enter guest new phone number (ENTER to skip): ")
    if guest_phone == '':
        guest_phone = guest_list[int(choice_guest) - 1].phone
    else:
        while guest_phone.isnumeric() is False: ## Phone number
            print('Please provide correct phone number')
            guest_phone = input("Enter guest phone number: ")
    guest_guests = input("Enter the new number of guests (ENTER to skip): ")
    if guest_guests == '':
        guest_guests = guest_list[int(choice_guest) - 1].guests
    else:
        while guest_guests.isnumeric() is False: ## Number of guests
            print('Please provide a correct number !')
            guest_guests = input("Enter the number of guests: ")
        while int(guest_guests) > 10: ## Check for maximum number of guestes
            print('Maximum number of guests is 10 !')
            guest_guests = input("Enter the number of guest: ")
    guest_list[int(choice_guest) - 1] = Guest(guest_name,int(guest_phone),int(guest_guests)) ## Create a guest
    print('Guest edited !')    
     
def print_guest_list():
    '''Print guest list'''
    for i in range(len(guest_list)):
        print(f"{i+1}. {guest_list[i].name}")

def create_tables(): 
    '''Create tables and adding to a list!!!'''
    for i, val in enumerate(tables):
        tables_list.append(Table(i, [["       "] * len(times) for i in range(1)], s2t[i+1]))

def booking():
    '''Booking table function'''
    while True:
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
            choice_guest = input('Please choose a guest: ')## Guest choice to make a booking
            while int(choice_guest) - 1 not in range(len(guest_list)):
                choice_guest = input('Please choose a guest: ')
            while guest_list[int(choice_guest) - 1].book_check() is True:
                print('Guest has already booked a table !')
                print('Please remove the booking, if you want to book another table')
                return 1
            else:
                no_seats = 0
                table_number = []
                for i,val in enumerate(tables_list): ## Checks if there is available tables for choosen amount of guests
                    if guest_list[int(choice_guest) - 1].guests > tables_list[i].seats:
                        no_seats += 1 ## For check if there are avalible tables
                    else:
                        table_number.append(i) ## Adding matching tables
                        tables_list[i].print_time_slots()
                if no_seats == len(tables_list): ## Check
                    print('There are no avalible tables for this guest !')
                    break
                else:
                    table_choice = input("Please choose a table number: ") ## Choose a table
                    while table_choice.isnumeric() is False or int(table_choice) - 1 not in table_number:
                        print("Please choose a valid number !")
                        table_choice = input("Please choose a table number: ")
                    else:
                        time_choice = tables_list[int(table_choice) - 1].book_check() ## Time choice with book check
                        tables_list[int(table_choice) - 1].book_table(time_choice) ## Actual booking a time
                        guest_list[int(choice_guest) - 1].b_table = int(table_choice) - 1 ## Assiging booking to the guest (table)
                        guest_list[int(choice_guest) - 1].b_time = time_choice ## Assigning bookint to the guest (time)
                        break

def remove_booking():
    '''Remove a booking function'''
    while True:
        table_number = []
        for i,val in enumerate(tables_list): ## Print time slots
            table_number.append(i) ## Add tables to the list
            tables_list[i].print_time_slots()
        table_choice = input("Please choose a table number: ") ## Table choice and check if booked
        while int(table_choice) - 1 not in table_number or table_choice.isnumeric() is False:
            print("Please choose a valid number !")
            table_choice = input("Please choose a table number: ")
        time_choice = tables_list[int(table_choice) - 1].unbook_check() ## Choosing a time
        if time_choice is False:
            break
        else:
            tables_list[int(table_choice) - 1].unbook_table(time_choice) ## Removing the booking
            for guest in guest_list:
                if guest.b_table == int(table_choice) - 1 and guest.b_time == time_choice:
                    choice_guest = guest_list.index(guest) 
            guest_list[choice_guest].b_table = -1 ## Assiging booking to the guest (table)
            guest_list[choice_guest].b_time = -1 ## Assigning bookint to the guest (time)

            break
    
          

main()


                
            

