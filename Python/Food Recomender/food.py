import csv
import random 
import os

# in add function
## check if name is already in the list, then ask if you are sure that you wanna add this dish

ver=0.9

cousines_list_ta=[]
cousines_list_ma=[]

os.system('cls')

def welcome(): # WELCOME/FIRST SCREEN, TWO CHOICES 
    os.system('cls')
    print(f'Welcome to food recommender {ver}')
    while True:
        choice_1=input('Do you want to add a new dish to your database or use the food recommender ("add" or "use") ?: ')
        if choice_1.lower()=='use' or choice_1.lower()=='add':
            break
        else:
            os.system('cls')
            print('Please enter a valid answer ("add" or "use") !') 
    
    return choice_1.lower()
    


def csv_opener(): # OPEN DATA BASE OF MEALS 
    global data_lines
    data=open('food.csv',encoding='utf-8',mode='r')
    csv_data=csv.reader(data)   
    data_lines=list(csv_data)
    data.close()

def csv_saver():
    while True:
        data=open('food.csv',mode='a',newline='')
        csv_writer=csv.writer(data)
        os.system('cls')
        name=input("Write the name of the dish: ")
        os.system('cls')
        while True:
            takeaway=input('Is it takeaway ("yes" or "no") ?: ')
            if takeaway.lower()=='yes' or takeaway.lower()=='no':
                break
            else:
                os.system('cls')
                print('Please enter a valid answer ("yes" or "no") !')
        if takeaway=='yes':
            os.system('cls')
            restaurant=input('Write the name of the restaurant: ')
        else:
            restaurant='No Restaurant'
        os.system('cls')
        while True:
            make=input('Can you make it at home ("yes" or "no") ?: ')
            if make.lower()=='yes' or make.lower()=='no':
                break
            else:
                os.system('cls')
                print('Please enter a valid answer ("yes" or "no") !')
        os.system('cls')
        cousine_name=input('Write cousine: ')
        csv_writer.writerow([name,takaway,make,restaurant,cousine_name])
        os.system('cls')
        print('New dish added !')
        data.close()
        while True:
            again=input('Do you want to add someting else or not ("yes" or "no") ?: ')
            if again.lower()=='yes' or again.lower()=='no':
                break
            else:
                os.system('cls')
                print('Please enter a valid answer ("yes" or "no") !')
        if again.lower()=='yes':
            continue
        elif again.lower()=='no':
            break

def set_cousines(data1):
    for line in data1[1:]:
        if line[1].lower()=='yes':
            if line[4] not in cousines_list_ta:
                cousines_list_ta.append(line[4])
        if line[2].lower()=='yes':
            if line[4] not in cousines_list_ma:
                cousines_list_ma.append(line[4])
            


def choice_take(): # FIRST CHOICE, TAKAWAY OR MAKE FOOD
    while True:
        os.system('cls')
        choice_ta=input('Would you like to make the food yourself or order it as takeaway ("order" or "make") ? : ')
        if choice_ta.lower()=='make' or choice_ta.lower()=='order':
            break
        else:
            print('Please enter a valid answer ("order" or "make") !')
    os.system('cls')
    return choice_ta.lower()
    

mix_list=[]

def takaway(data1): # FUCNTION THAT CREATES A LIST OF TAKEAWAY MEALS
    for line in data1:
        if line[1].lower()=='yes':
            mix_list.append(line)

def make(data1): # FUNCTION THAT CREATES A LIST OF MAKE AT HOME MEALS
    for line in data1:
        if line[2].lower()=='yes':
            mix_list.append(line)
        
def cousine(): # FUNCTION THAT CHOOSE A COUSINE 
    while True:
        choice_cousine=input('Do you want to choose the cousine ("yes" or "no") ?: ')
        if choice_cousine.lower()=='yes' and choice_ta=='order':
            while True:
                print(cousines_list_ta)
                choice_cousine=input('Please enter a name of a cousine: ')
                if choice_cousine.lower() in cousines_list_ta:
                    os.system('cls')
                    return choice_cousine.lower()
                    break
                else:
                    os.system('cls')
                    print('Please enter a valid cousine !\n')
                    
            break
        elif choice_cousine.lower()=='yes' and choice_ta=='make':
            while True:
                print(cousines_list_ma)
                choice_cousine=input('Please enter a name of a cousine: ')
                if choice_cousine.lower() in cousines_list_ma:
                    os.system('cls')
                    return choice_cousine.lower()
                    break
                else:
                    os.system('cls')
                    print('Please enter a valid cousine !\n')
                    
            break
        elif choice_cousine.lower()=='no':
            os.system('cls')
            return 'no'
        else:
            os.system('cls')
            print('Please enter a valid answer ("yes" or "no") !')



def last_mix(mix1,choice2): # LAST LIST IF COUSINE CHOOSED
    for line in mix1:
        if line[4].lower()==choice2:
            cousine_mix.append(line)

def new_recom(): # CREATES A NEW RECOMMENDATION IF USER NOT SATISFIED
    while True:
        new_random=input('Do you want another recomendation ("yes" or "no") ?: ')
        if new_random.lower()=='yes' or new_random.lower()=='no':
            return new_random
            break
        else:
            os.system('cls')
            print('Please entere a valid answer ("yes" or "no") ! ')

def exit(): # EXIT SCREEN, CHOICE 'EXIT' OR 'START AGAIN'
    while True:
        os.system('cls')
        exit_answer=input('Do you want to exit or start over ("exit" or "start over") ?: ')
        if exit_answer.lower()=='exit' or exit_answer.lower()=='start over':
            if exit_answer.lower()=='exit':
                return exit_answer
                break
            else:
                return exit_answer
                break
        else:
            os.system('cls')
            print('Please provide a valid answer ("exit" or "start over") !')

###
# ACTUAL PROGRAM LOGIC
###       
while True:
    
    choice_1=welcome()
    if choice_1=='add':
        csv_saver()
    elif choice_1=='use':
        csv_opener()
        set_cousines(data_lines)
        choice_ta=choice_take()
        if choice_ta=='order':
            takaway(data_lines)
        else:
            make(data_lines)
        choice_cousine=cousine()
        if choice_cousine=='no':
            while True:
                result=random.choice(mix_list)
                if choice_ta=='order':
                    print(f"Today's recommendation is {result[0]} from {result[3]}")
                else:
                    print(f"Today's recommendation is {result[0]}")
                new_random=new_recom()
                os.system('cls')
                if new_random.lower()=='yes':
                    continue
                else:
                    break
        else:
            while True:
                cousine_mix=[]
                last_mix(mix_list,choice_cousine)
                print(cousine_mix)
                result=random.choice(cousine_mix)
                if choice_ta=='order':
                    print(f"Today's recommendation is {result[0]} from {result[3]}")
                else:
                    print(f"Today's recommendation is {result[0]}")
                new_random=new_recom()
                os.system('cls')
                if new_random.lower()=='yes':
                    continue
                else:
                    break
    exit_answer=exit()
    if exit_answer=='exit':
        break









