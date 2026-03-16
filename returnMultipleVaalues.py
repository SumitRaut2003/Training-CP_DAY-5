def add():
    n1= int( input("Enter the value of n1:"))
    n2 = int(input("Enter value of n2:"))
    
    sum = n1+n2
    sub = n1-n2
    div = n1/n2
    mul = n1*n2
    return sum,sub,div,mul

add()
result = add()
print(result)
#we can only pass 4 types of arguments 
# 1. Positional Argument 
# 2. Keyword Argumaent 
# 3. Default Argument 
# 4. Variable length argument / variable number of argument 


