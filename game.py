import random
import sys
def lucky(n1,n2,n3):
    if n1==n2==n3==7:
        print("you won the jacpot")
    elif n1==n2 or n1==n3 or n2==n3:
        print("you won the bonus")
    else:
        print("you loss")
    
while True:
    print("Do you want to play the 7lucky game")
    s=input("YES/NO")
    s=s.upper()
    if s=='YES':
       n1=random.randint(5,7)
       n2=random.randint(5,7)
       n3=random.randint(5,7)
       lucky(n1,n2,n3)
    elif s=='NO':
        sys.exit()
    else:
        sys.exit()
        
