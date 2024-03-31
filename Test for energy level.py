''''welcome massage'''
welcom = input ("WELCOME, DO YOU WANT TO CALCULATE YOUR ENERGY LEVEL? 'YES' OR 'NO'\n").lower()

''''if the answer is yes ask the questions'''

if welcom == "yes":
    user_input = input("Name the five most important areas of your life. For example: relationship, work, etc.\n")
    inputs = user_input.split()
    print(inputs)

# def set_energy_level ():
    print ("Now you mustbset your energy level out of 100 for every area of your life you entered. For example: relationship : 80%, etc.\n")
    area1 = int(input (f"set your energy level for {inputs[0]}  "))
    area2 = int(input (f"set your energy level for {inputs[1]}  "))
    area3 = int(input (f"set your energy level for {inputs[2]}  "))
    area4 = int(input (f"set your energy level for {inputs[3]}  "))
    area5 = int(input (f"set your energy level for {inputs[4]}  "))

    ''''put the entered values in a dictionary'''
    level = {
        inputs[0]:area1,
        inputs[1]:area2,
        inputs[2]:area3,
        inputs[3]:area4,
        inputs[4]:area5
    }
    print (level)
    calculat_level = (area1 + area2 +area3 +area4 + area5)/5
    print(f"Your energy level will be {calculat_level}")
    if calculat_level > 63:
        print("LOVE UR ENERGY KATE")
        print("MOVIE TIME")
    elif calculat_level < 63:
        print ("Work Harder LOSER")
elif welcom == "no":
    print ("Go Watch Movie")
