import time
run_calc = True
while run_calc:
    print ("This is an Arithmetic and Temperature Calculator.")
    print ("""[1] Convert Fahrenheit to Celsius.
              [2] Convert Fahrenheit to Kelvin.
              [3] Convert Celsius to Fahrenheit.
              [4] Convert Celsius to Kelvin.
              [5] Convert Kelvin to Fahrenheit.
              [6] Convert Kelvin to Celsius.
              [7] Add (x + y)
              [8] Subtract (x - y)
              [9] Multiply (x * y)
              [10] Divide (x / y)
              [11] Remainder Division ( x % y)
              
            """)
    print ("""This machine can also perform advanced numerical operations like calcuating Speed, Distance, and Time
>
           [12] Speed (if distance and time are known)
           [13] Distance (if time and speed are known)
           [14] Time (if distance and speed are known)
           """)
    def add():
        import time
        first_val = int(input("First Value: "))
        second_val = int(input("Second Value: "))
        result = first_val + second_val
        print("Calculating...")
        time.sleep(1)
        print("The Sum of %s + %s = %s" % (first_val, second_val, result))

    def subtract():
        import time
        first_val = int(input("First Value: "))
        second_val = int(input("Second Value: "))
        result = (first_val - second_val)
        print("Calculating...")
        time.sleep(1)
        print("The Difference of %s - %s = %s" % (first_val, second_val, result))

    def multiply():
        import time
        first_val = int(input("First Value: "))
        second_val = int(input("Second Value: "))
        result = first_val * second_val
        print("Calculating...")
        time.sleep(1)
        print("The Product of %s * %s = %s" % (first_val, second_val, result))

    def divide():
        import time
        first_val = int(input("First Value: "))
        second_val = int(input("Second Value: "))
        result = first_val/second_val
        print("Calculating...")
        time.sleep(1)
        print("The Quotient of %s / %s = %s" % (first_val, second_val, result))

    def modulo():
        import time
        first_val = int(input("First Value: "))
        second_val = int(input("Second Value: "))
        result = int(first_val % second_val)
        print("Calculating...")
        time.sleep(1)
        print("The Remainder of %s % %s = %s" % (first_val, second_val, result))


    def speed():
        distance = int(input("Distance Value: "))
        time = int(input("Time Value: "))
        result = int(distance % time)
        print("If your destination is, %s kilometers away and it takes you %s minutes you would be travelling at a rate of %s meters per second." % (distance, time, result))
        
    def distance():
        speed = int(input("Rate Value: "))
        time = int(input("Time Value: "))
        result = (speed * time)
        print("If you were travelling at a rate of %s meters per second, and it took % minutes, your destination is probably %skm away." % (speed, time, result))

    def time():
        distance = int(input("Distance Value: "))
        speed = int(input("Speed Value: "))
        result = (distance / speed)
        print("If you destination is %s kilometers away, and you are travelling at a rate of %s meters per second, it will take you %s minutes to reach your destination." % (distance, speed, result))    
        
    
    
    
        
    def f_to_c():
        fahr = int(input("Fahrenheit Value: "))
        cels = (fahr - 32) * 5/9
        print("%s degrees Fahrenheit is %.1f degrees Celsius." % (fahr, cels))


    def f_to_k():
        fahr = int(input("Fahrenheit Value: "))
        kelv = (fahr -32)* 5/9 + 273.15
        print("%s degrees Fahrenheit is %.1f degrees Kelvin." % (fahr, kelv))


    def c_to_f():
        cels = int(input("Celsius Value: "))
        fahr = (cels * 9/5) + 32
        print("%s degrees Celsius is %.1f degrees Fahrenheit." % (cels, fahr))


    def c_to_k():
        cels = int(input("Celsius Value: "))
        kelv = (cels + 273.15)
        print("%s degrees Celsius is %.1f degrees Kelvin." % (cels, kelv))


    def k_to_c():
        kelv = int(input("Kelvin Value: "))
        cels = (kelv - 273.15)
        print("%s degrees Kelvin is %.1f degrees Celsius." % (kelv, cels))


    def k_to_f():
        kelv = int(input("Kelvin Value: "))
        fahr = (kelv - 273.15) * 9/5 + 32
        print("%s degrees Kelvin is %.1f degrees Fahrenheit." % (kelv, fahr))

    def functions():
        print("To quit press [Enter].")
        choice = int(input("Choose one of the numbers above: "))
        if choice == 1:
            print("You have chosen %s." % (choice))
            f_to_c()
            
        elif choice == 2:
            print("You have chosen %s." % (choice))
            f_to_k()
        elif choice == 3:
            print("You have chosen %s." % (choice))
            c_to_f()
        elif choice == 4:
            print("You have chosen %s." % (choice))
            c_to_k()
        elif choice == 5:
            print("You have chosen %s." % (choice))
            k_to_f()
        elif choice == 6:
            print("You have chosen %s." % (choice))
            k_to_c()
        elif choice == 7:
            print("You have chosen %s." % (choice))
            add()
        elif choice == 8:
            print("You have chosen %s." % (choice))
            subtract()
        elif choice == 9:
            print("You have chosen %s." % (choice))
            multiply()
        elif choice == 10:
            print("You have chosen %s." % (choice))
            divide()
        elif choice == 11:
            print("You have chosen %s." % (choice))
            modulo()
        elif choice == 12:
            print("You have chosen %s." % (choice))
            speed()
        elif choice == 13:
            print("You have chosen %s." % (choice))
            distance()
        elif choice == 14:
            print("You have chosen %s." % (choice))
            time()
        elif choice == " ":
            run_calc = False
        else:
            print("You have chosen an invalid choice.")
            print("<>><><><><><><><><><")
            print("Try again.")
            print(temp)
    functions()

    endelea = input("Would you like to continue [yes or no]? ")
    if endelea == "yes":
        functions()
    elif endelea =="y":
        functions()
    elif endelea == "no":
        exit(0)
    elif endelea == "n":
        exit(0)
    elif endelea == " ":
        run_calc = False
    else:
        print ("Thank You for using this Basic Arithmetic and Temperature calculator or (BAT calc).")
        time.sleep(5)
        print("Initiating Shutdown...")
        time.sleep(1)
        exit(0)

