# Write code below 💖
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

Q1 = int(input("Do you like Dawn or Dusk?  1)Dawn  2)Dusk : "))
if Q1 == 1:
  Gryffindor+=1
  Ravenclaw+=1
elif Q1 == 2:
  Hufflepuff+=1
  Slytherin+=1
else:
  print("Wrong input.")

Q2 = int(input("When I'm dead, I want people to remember me as:  1)The Good  2)The Great  3)The Wise  4)The Bold : "))
if Q2 == 1:
  Hufflepuff+=2
elif Q2 == 2:
  Slytherin+=2
elif Q2 == 3:
  Ravenclaw+=2
elif Q2 == 4:
  Gryffindor+=2
else:
  print("Wrong Input.")

Q3 = int(input("Which kind of instrument most pleases your ear? 1)The violin 2)The trumpet 3)The piano 4)The drum : "))
if Q3 == 1:
    Slytherin+=4
elif Q3 == 2:
    Hufflepuff+=4
elif Q3 == 3:
  Ravenclaw+=4
elif Q3 == 4:
  Gryffindor+=4
else:
  print("Wrong input")

print("Gryffindor has : ", Gryffindor)
print("Ravenclaw has : ", Ravenclaw)
print("Hufflepuff has : ", Hufflepuff)
print("Slytherin has : ", Slytherin)
