#basic function syntax : write a function to cal a squre of that number and hold that result in a variable
number=19
def square(number):
    return number**2 
result=square(number) 
print(result)

#create a function that takes two numbers as parmeters and return thai sum 

def add(numone,numtwo):
    return numone+numtwo 
print(add(46547,5354576)) 

# create a function that returns both circumfrerence and area  | # for more precition upto two decimal 

import math                                                  
def circle_stats(radius):
    area = math.pi*(radius**2)
    cf= 2*math.pi*radius 
    return area,cf
A,C=circle_stats(9)
print("Area :",A, "-Circumferance :",C) 

#

def circle_stats(radius):                                      
    area = 3.14*(radius**2)                                 
    cf= 2*3.14*radius                                       
    return area,cf                                              
A,C=circle_stats(9)
print("Area :",A, "-Circumferance :",C)  

# make function that geet the user if no name is provided ,it should greet witha default name 

def greet(name="user"):
    return "Hello, " + name +  " !"
print(greet())                         
# with user name 
print(greet("adit))

# create a lambda function to compute a cube of a number 

cube= lambda x : x **3 
print(cube(6))

# make a function that tkes variable no of arguments and give their sum use *args 
def sum_all(*args):
    return sum(args) 
print(sum_all(1,2,3))
print(sum_all(4,5,6,7,8,9,10)) 

#create a function that accrpts any number of keyword arguments and print them in the formate on key:word ,use **kwargs 

ef print_kwargs(**kwargs): 
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    
print_kwargs(name="dwij",power="karate")
print_kwargs(name="dwij",power="karate",enemy="vansh") 

# write a  generator function that yeilds a even number upto specifed limit

ef even_gen(limit):
    for z in range(2,limit+1,2):
         yield z 
for num in even_gen(15):
    print(num)




























