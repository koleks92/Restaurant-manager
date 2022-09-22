## Simple restaurant manager to work on OOP in Python


class Restaurant:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"This is the {self.name} booking manager\nWelcome !\n")

    def tables(self):
        tables = int(input("How many tables in the restaurant ?: "))
        while tables not in range(1,20):
            print("Please provide a proper number !")
            tables = int(input("How many tables in the restaurant ?: "))
        return list(range(1, int(tables)+1))
        
    def seats(self):
        seats = []
        print("Please provide amount of seats for each table !")
        for i in range(len(tables)):
            seats.append(int(input(f"Table {i+1}: ")))
        return seats
    
    def seats_to_tables(self):
        s2t = dict(zip(tables, seats))
        return s2t
    
class Table():

    time_slots = {}
    times = ["17-19","19-21","21-23"]

    def __init__(self, name, books):
        self.name = name
        self.books = books
        
    def time_slots(self): ## not sure if needed
        time_slots = {}
        times = ["17-19","19-21","21-23"]
        for number in tables:
            time_slots[number] = times
        return time_slots

    def print_time_slots(self):
        print(f"\nTable {self.name+1} timeslots:")
        print("| 17-19 | 19-21 | 21-23 |")
        for b in self.books:
            print("|%s| " % ("|".join(b)))
    
    def book_time(self):
        while True:
            choice = input('Please choose time slot: ')
            while choice not in self.times:
                choice = input('Please choose time slot: ')
            for i in self.times:
                if choice == i:
                    a = self.times.index(i)
            while self.books[0][a] == 'XXXXXXX':
                print("Table already booked !")
                break
            self.books[0][a] = 'XXXXXXX'
            return True
    
    def fully_booked(self):
        booked=True
        for i in self.books[0]:
            if 'XXXXXXX' != i:
                booked = False
                break
            else:
                booked = True
        return booked


# class Guest()
            

                        
rest1 = Restaurant(input("Please provide the name of the restaurant: "))
rest1.print_name()
tables = rest1.tables()
seats = rest1.seats()
s2t = rest1.seats_to_tables()

objs = []

for i in range(len(tables)):
    objs.append(Table(i, [["       "] * 3 for i in range(1)]))
    
for i in range(len(objs)):
    if objs[i].fully_booked()==True:
        pass
    else:
        objs[i].print_time_slots()

## work here
objs[1].book_time()

for i in range(len(objs)):
    if objs[i].fully_booked()==True:
        pass
    else:
        objs[i].print_time_slots()



