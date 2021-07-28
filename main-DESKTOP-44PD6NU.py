
# CALCULATOR AND CONVERTER IN ONE PROJECT


# import numpy
import math

print("\nWELCOME TO CALCULATOR AND CONVERTER ALL IN ONE!!!!")

while(True):
    
    def select1():
        print("\n1. Converter\n2. Area\n3. Basic Calculation\n")


    def square(e):
        print(f'\n"The area of square is:{round(e*e,2)} "')

    def rectangle(le,br):
        print(f'\n"The area of rectangle is: {round(le*br,2)}"')

    def circle(r):
        area = math.pi*r*r
        print(f'\n"The area of circle is: {round(area,2)}"')

    def triangle(b,h):
        A = 0.5*b*h
        print(f'\n"The area of triangle is: {round(A,2)} "')




    def length():
        print("Which value you want to convert:\n1. km\n2. m\n3. cm\n")
        x = int(input("Enter the choice from above you want to opt for(in number):\n"))
        y = int(input("Enter in what unit you want to convert(in number):\n"))
        if x == 1 and y == 2:
            km = float(input("Enter the value in km: "))
            km_to_m = km*1000
            print(f'\n"The value is {km_to_m} m"')

        elif x == 1 and y == 3:
            km = float(input("Enter the value in km: "))
            km_to_cm = km*100000
            print(f'\n"The value is {km_to_cm} cm"')

        elif x == 2 and y == 1:
            km = float(input("Enter the value in m: "))
            m_to_km = km/1000
            print(f'\n"The value is {m_to_km} km"')

        elif x == 2 and y == 3:
            km = float(input("Enter the value in m: "))
            m_to_cm = km*100
            print(f'\n"The value is {m_to_cm} cm"')

        elif x == 3 and y == 1:
            km = float(input("Enter the value in cm: "))
            cm_to_km = km/100000
            print(f'\n"The value is {cm_to_km} km"')

        elif x == 3 and y == 2:
            km = float(input("Enter the value in cm: "))
            cm_to_m = km/100
            print(f'\n"The value is {cm_to_m} m"')

        else:
            print('\n"You cannot covert same units"')    
        

    def temp():
        print("\n1. C to F\n2. F to C\n")
        n = int(input("Enter the choice(in numbers): "))

        if n == 1:
            e = float(input("Enter the value: "))
            F = (e * 9/5) + 32
            print(f'\n"The temperature is {F} F"')

        if n == 2:
            o = float(input("Enter the value: "))
            C = (o - 32) * 5/9
            print(f'\n"The temperature is {C} C"')


    def converter():   
        print("\n1. Length\n2. Temperature\n")
        a = int(input("Enter the choice from above you want to opt for(in number):\n"))
        if a == 1:
            length()
        
        if a == 2:
            temp()


    def area():
        print("\n1. square\n2. rectangle\n3. circle\n4.Triangle\n")
        b = int(input("Enter the choice from above you want to opt for(in number):\n"))


        if b == 1:
            e = float(input("Enter the length of side: "))
            square(e)

        elif b == 2:
            len = float(input("Enter the length: "))
            bre = float(input("Enter the breadth: "))
            rectangle(len,bre)

        elif b == 3:
            rad = float(input("Enter radius: "))
            circle(rad)

        elif b == 4:
            base = float(input("Enter the value of base: "))
            height = float(input("Enter the value of height: "))
            triangle(base,height)
            
            
    def addition(n):
        y = [] 
        for i in range(0, n):
            b = float(input(f"\nEnter number {i+1}: "))
            x = y.append(b)

        s = sum(y)
        print(f'\n"The addition of entered numbers is {s}"') 

    def subtraction():
        a = float(input("Enter the number: "))
        b = float(input("Enter the number: "))
        s = a - b
        print(f'\n"The subtraction of entered numbers is {s}"') 

    def multiplication(n):
        y = []
        pro = 1
        for i in range(0, n):
            b = float(input(f"\nEnter number {i+1}: "))
            y.append(b)

        # pro = numpy.prod(y)
        for i in y:
            pro = pro*i
        print(f'\n"The multiplication of entered numbers is: { round(pro, 2)}"')

    def division():
        a = float(input("Enter the number: "))
        b = float(input("Enter the number: "))
        s = a / b
        print(f'\n"The division of entered numbers is { round(s, 2)}"') 


    def basic():
        print("\n1. addition\n2. subtraction\n3. multiplication\n4. division\n")
        d = int(input("Enter the choice from above you want to opt for(in number):\n"))

        if d == 1:
            add = int(input("\nHow many numbers you want to do addition of: ")) 
            addition(add)

        elif d == 2:
            subtraction()

        elif d == 3:
            mul = int(input("\nHow many numbers you want to do multiplication of: ")) 
            multiplication(mul)

        elif d == 4:
            division() 





    
    # drivers code
    select1()
    print("Press 0 if you want to exit the code\n")
    x = int(input("Enter the choice from above you want to opt for(in number):\n"))

    if x == 0:
        print("\nTHANKS FOR USING THIS APPLICATION.\nHAVE A GREAT DAY!!")
        break

    if x == 1:
        converter()
        print("\n-----------------------------------------------------------------\n-----------------------------------------------------------------\n-----------------------------------------------------------------")
    
    elif x == 2:
        area()
        print("\n-----------------------------------------------------------------\n-----------------------------------------------------------------\n-----------------------------------------------------------------")
        

    elif x == 3:
        basic()    
        print("\n-----------------------------------------------------------------\n-----------------------------------------------------------------\n-----------------------------------------------------------------")
        
    else:
        print('\n"Please enter valid number between 1, 2 and 3 only"')
        print("\n-----------------------------------------------------------------\n-----------------------------------------------------------------\n-----------------------------------------------------------------")
