while True:

    jahr= int(input(" In welchem Jahr bist du geboren?"))
    monat= int(input(" In welchem Monat (als Zahl) haste Geburtstag?"))
    tag= int(input ("An welchem Tag hast du Geburtstag?"))

    if monat ==1 and tag ==17:
        print("Happy Birthday!!!")

    elif monat ==1 and tag >=17:
        print ("You will have Birthday in the next days")

    elif monat ==1 and tag <= 17:
        print ("You had Birthday before a few days")

    elif monat >=1 and tag ==17:
        print ("You will have Birthday in a few months")

    elif monat >=1 and tag >=17:
        print ("You will have Birthday in a few months")

    elif monat >=1 and tag <=17:
        print ("You will have Birthday in a few months")

    elif monat <=1 and tag ==17:
        print ("You had Birthday before a few monthS")

    elif monat <=1 and tag >=17:
        print ("You had Birthday before a few monthS")

    elif monat <=1 and tag <=17:
        print ("You had Birthday before a few monthS")

    alter = 2017-jahr
    print("You're", alter, "years old")

    antwort = input ("\nWollen sie es noch einmal aus probieren?(yes/no) ")

    if antwort != "yes":
        break
    else:
        print ("\n\n")


     
    
