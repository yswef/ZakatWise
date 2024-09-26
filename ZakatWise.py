def colc_cash():
    monay = int(input("hom much monay you have?\n"))
    
    totel = monay/1000 *2.5
    
    print("you will get out for zakat" + str(totel))

def colc_gold():
    gold = int(input("how much gold you have?\n"))
    
    if gold >= 85:
        zakat = gold%2.5
        print("you will get out for zakat" + str(zakat))
    else:
        print("You do not have to pay zakat")

def colc_silver():
    silver = int(input("how much gold you have?\n"))
    
    if silver >= 595:
        zakat = silver%2.5
        print("you will get out for zakat" + str(zakat))
    else:
        print("You do not have to pay zakat")

Type_of_zakat = input("What type of zakat do you want to calculate (silver, gold, cash):\n")

while True:
    if Type_of_zakat == "silver":
        colc_silver
    elif Type_of_zakat == "gold":
        colc_gold
    elif Type_of_zakat == "cash":
        colc_cash
    
    loop_look = input("do you want to colcet anather value zakat (y , n)")
    
    if loop_look == "n":
        break


