def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multi(x,y):
    return x * y

def div(x,y):
    return x / y



def Calculator():
    
    print("***My Simple Calculator***")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    


    choice = input("Enter the choice(1/2/3/4): ")

    if choice in ['1','2','3','4']:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == '1':
        
            print(f"{num1} + {num2} = {add(num1,num2)}")

    
        elif choice == '2':
        
             print(f"{num1} - {num2} = {sub(num1,num2)}") 
   
        elif choice == '3':
        
              print(f"{num1} * {num2} = {multi(num1,num2)}")    
   
        elif choice == '4':
       
              print(f"{num1} / {num2} =  {div(num1,num2)}")  
      
     

               

    else:
        print("Invalid choice,Try Again.")    

while True: 
    Calculator()       
    
       

    

