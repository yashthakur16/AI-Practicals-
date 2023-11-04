def multiply(a,b): #parameters 
    a=8
    return a*b

def fact(n):
    if(n==0 or n==1):   # base case
        return 1
    else:
        return n* fact(n-1) #recursive call
    

a=7
print(multiply(a,6)) #arguments
print(a) # checking the scope of a
print(fact(5)) # calculating factorial using recursion

