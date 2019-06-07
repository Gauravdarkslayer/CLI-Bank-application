'''
    Bank Application. Just some basic functionalities
'''
import os,time,datetime
from tkinter import *
import tkinter.messagebox
import tkinter as tk

def main_screen():
    currentDT = datetime.datetime.now()
    print (str(currentDT))
    #os.system('color 4')
    print('WELCOME TO OUR BANK'.center(170,'*'))
    print('CHOOSE FROM ONE OF THE BELOW OPTIONS')
    print('1. LOGIN')
    print('2. SIGN UP')
    print('3. EXIT')

    choice = int(input())
    if choice == 1:
        print('YOU ARE REDIRECTING TO LOGIN PAGE....')
        time.sleep(3)
        login()
    elif choice==2:
        print('YOU ARE REDIRECTING TO SIGNUP PAGE....')
        time.sleep(3)
        signup()
    elif choice == 3:
        print('BYE BYE USER TATA')
        logintime(start_time)
        time.sleep(2)
        exit()
    else:
        print('You\'ve entered wrong choice. Please restart the application')

data = { 
    #None : { 'name':None,'bal':None,'password':None},
    '1000' : { 'name':'gaurav', 'bal':250000, 'password':'hello123'},
    
        }
start_time = 0        
def login():
    os.system('CLS')
    currentDT = datetime.datetime.now()
    print (str(currentDT))
    while True:
        acc_no = input('Enter your account number')
        password = input('Enter your password') 
        if acc_no in data.keys():
            
            if data[acc_no]['password'] == password : 
                global start_time
                start_time = time.time()
                
                print(f"Welcome back user {data[acc_no]['name']}")
                after_login(data,acc_no) #Calling after_login function
                break
            else : 
                print("Invalid Password")
                continue
        else : 
            print("no such user exists")
            continue       


def logintime(start_time):
    mins = 0
    hours = 0
    sec = '%.f' % (time.time() - start_time)

    sec = int(sec)
    a=time.strftime('%H:%M:%S', time.gmtime(sec))
    print('USer logged in for:')
    print("Time",a)
    root = tk.Tk()
    #root.overrideredirect(1)
    root.withdraw()
    root.attributes('-topmost',True)
    tk.messagebox.showinfo("Time",a) #Output the time
    time.sleep(6)

def signup():
    os.system('CLS')                       
    print('Sign Up')
    name = input('Please enter your name')
    bal = eval(input('Please enter your initial balance'))
    pwd = input('Enter your password')
    new_number = str(int(max(data.keys()))+1)
    #print(str(new_number))
    data.update({new_number:{'name':name,'bal':bal,'password':pwd}})
    print('Your details are:')
    print('Your account number is:',new_number)
    
    for key,value in data[new_number].items():
        print(key,'=',value)
    print('Now You can login')
    time.sleep(2)
    login()

def after_login(currentdata, currentaccount):
    print('Now what you want to do?\nPlease choose from below')
    print('1. Credit')
    print('2. Debit')
    print('3. Exit')
    print('4. Check balance')
    print('5. log out')    
    choose = int(input())
    if choose == 1:
        amount = int(input('Enter how much to credit in your account'))
        currentdata[currentaccount]['bal'] += amount    #Adding current balance to given amount
        print('New balance is:',currentdata[currentaccount]['bal'])
        logintime(start_time)
    elif choose == 2:
        amount = int(input('Enter how much to debit in your account'))
        currentdata[currentaccount]['bal'] -= amount    #Deducting current balance to given amount
        print('New balance is:',currentdata[currentaccount]['bal'])
        logintime(start_time)

    elif choose == 3:
        print('Thank you! Visit again')
        logintime(start_time)
        time.sleep(3)
        exit()

    elif choose == 4:
        d = data.get(currentaccount,False)
        if  d :
            print('Your available balance is:',d['bal'])    
        else:
            print('No such information available')
    elif choose == 5:
        print('Logging you out')
        time.sleep(1)
        
        logintime(start_time)
        login()


main_screen()    
