### Modules
import time
import random
import turtle as trtl
t = trtl.Turtle()


print('Hi there! Welcome to The Meat Project founded by Abhi, Mohammed, Nolan, and Rami')
time.sleep(2)
##Rami
a1 = str(input("Would you like to open a new order or track an exsisting order? (N for New and T for track)"))
if a1.upper() == "T":
  print("Alright! Please enter your tracking order!")
  print("Connecting to System...")
  load = str(random.randint(1, 5))
  for i in (load):
    print("Connecting to System.")
    time.sleep(0.5)
    print("Connecting to System..")
    time.sleep(0.5)
    print("Connecting to System...")
    time.sleep(0.5)
    OrderInputTrack = input("PLease input your tracking ID: ")
    print("Could not find Order/Reset code to order again!")

  
  
if a1.upper() == "N":
  wn = trtl.Screen()
  screen_w = 327
  screen_h = 440
  wn.setup(width=screen_w, height=screen_h)
  wn.bgpic("ResterauntMenu.png")


  print("Your order ID is " + str(random.randint(1,100)))
  Crocadile_Roast = 18
  Seared_Beef = 15
  Baked_Frog =  17
  Stuffed_Duck = 22
  Soaked_Chicken = 16
  Baby_Kangaroo = 36

  Meat_strips = 14
  Meat_Salad = 16

  Exotic_Tropical_Drink = 8
  Jack_Sparrow_Rum = 12
  James_Bonds_Beer = 12

  ##foodmathtotal
  food_list = ["N/A",Crocadile_Roast, Seared_Beef, Baked_Frog, Stuffed_Duck, Soaked_Chicken, Baby_Kangaroo, Baby_Kangaroo, Meat_strips, Meat_Salad, Exotic_Tropical_Drink, Jack_Sparrow_Rum, James_Bonds_Beer]
  item_number = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth', 'ninth', 'tenth', 'eleventh', 'twelth']
  n_one = 0
  total_price = 0

  while True:
    food_choice = input('What is your ' + item_number[n_one] + ' item?')
    try:
      food_choice = int(food_choice)
    except ValueError:
      print('Please input number only!')
      continue
    n_one += 1
    total_price += food_list[food_choice]

    end = input('Would you like to end the order? (Y/N): ')
    if end.lower() == 'y':
      print('Your total price is: ' + str(total_price))
      print("Now paying by card...")
      time.sleep(1)
      print("Charging card ending in " + str(random.randint(1000,9999)))  
      time.sleep(1)
      print("Enjoy your food!")
      screen_w = 801
      screen_h = 312
      wn.setup(width=screen_w, height=screen_h)
      wn.bgpic("Proj.png")
      wn.mainloop()

      break
    else:
      continue





