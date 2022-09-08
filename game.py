import random
random_number=random.randint(1,10)
i=1
while i<=8:
    
    user=int(input("Enter the No."))
    if random_number==user:
        print(f"You won the game{i}")
        break
    elif user<random_number:
        print ("guess is low")
       
    elif user>random_number:
        print ("guess is high")

    i=i+1

if i>8:
    print("game is over")
