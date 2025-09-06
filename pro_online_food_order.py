#online food order

foodlist = []

while True :
   print("1.menu")
   print("2.light item")
   print("3.heavy item")
   print("4.soft drinks")
   print("5.exit")

   item = input("enter your option :")

   if item == "1" :
        print("1.light food \t"
              "2.heavy food \t"
              "3.soft drinks")

   elif item == "2" :
         lightitem = input("cha,coffie,snaks which one ? :")
         if lightitem == "cha" :
             print("normal cha is 20tk \t"
                   "special cha is 50tk")
         elif lightitem == "coffie":
             print("normal coffie is 20tk\t"
                   "black coffie is 40 tk")
         elif lightitem == "snaks" :
             print("biscuits is 30tk\t"
                   "pestre is 50tk")
         orderdone = input("if you want to order: [yes/no]")
         if orderdone == "yes":
             print("your order is accepted sir")
         else:
             print("try another things")

   elif item == "3" :
        heavyitem = input("kacchi,biriyani,tehari which one ? :")
        if heavyitem == "kacchi":
            print("kacchi price is 250tk")
        elif heavyitem == "biriyani" :
            print("biriyani price is 150tk")
        elif heavyitem == "tehari" :
            print("tehari price is 150tk")
        orderdone = input("if you want to order: [yes/no]")
        if orderdone == "yes":
            print("your order is accepted sir")
        else:
            print("try another things")

   elif item == "4" :
        softitem = input("sarbat,juice,mojo which one ? :")
        if softitem == "sarbat" :
            print("normal sarbat price is 20tk \t"
                  "special cold sarbat is 30tk")
        elif softitem == "juice":
            print("lemon juice is 25tk \t"
                  "mango juice is 25tk \t"
                  "mix juice is 30tk ")
        elif softitem == "mojo" :
            print("mini pack is 20tk \t"
                  "1 liter is 40tk \t"
                  "2 liter is 80tk")

        orderdone = input("if you want to order: [yes/no]")
        if orderdone == "yes":
            print("your order is accepted sir")
        else:
            print("try another things")

   elif item == "5" :
        print ("thanks for comming , take care")
        break


   else:
        print("try between 1 to 4")














