info = print("a. +")
infoo = print("b. *")
infooo = print("c. /")
infoooo = print("d. -")
user_input = input("Please select your method: ")
if user_input == "a":
    aa = input("Please select your first number: ")
    bb = input("Please select your second number: ")
    aa = int(aa)
    bb = int(bb)
    print(aa + bb)

if user_input == "b": 
    cc = input("Please select your first number: ")
    dd = input("Please select your second number: ")
    cc = int(cc)
    dd = int(dd)
    print(cc * dd)

if user_input == "c": 
    ee = input("Please select your first number: ")
    ff = input("Please select your second number: ")
    ee = int(ee)
    ff = int(ff)
    print(ee / ff)

if user_input == "d": 
    gg = input("Please select your first number: ")
    hh = input("Please select your second number: ")
    gg = int(gg)
    hh = int(hh)
    print(gg - hh)
