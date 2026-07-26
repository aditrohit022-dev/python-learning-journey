# avoiding global x  
x=56
def fun2(y):
    z=x+y 
    return z
re=fun2(3) 
print(re)
  
# decalring veriable value out of main function  

x = 5 

def f1():
    x=8
    def f2():
        print(x) 
    f2()
f1()  
  









