import random

n=random.radint(1,100)

a=-1

gueses=1

while(a!=n):
    
    a=int(input("guess the number:"))

    if(a>n):
        print("Lower number please")
        gueses+=1
    elif(a<n):
        print("Higher number please")
        gueses+=1

print(f"You have guessed the number {n} correctly in {gueses} attempts")