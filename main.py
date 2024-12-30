import random
def game(com,you):
    if com==you:
        return None
    elif com=='s':
        if you=='w':
            return False
        else:
            return True
    elif com=='w':
        if you=='g':
            return False
        else:
            return True
    else:
        if you=='s':
            return False
        else:
            return True
print("!!!Computers turn!!!")
ran=random.randint(1,3)
if ran==1:
    com='s'
elif ran==2:
    com='w'
else:
    com='g'
print("!!!Your Turn!!!")
print("Choose Snake(s) Water(w) Gun(g):")
you=input()
a=game(com,you)
print(f"Computer Chose {com}")
print(f"You Choose {you}")
if a==None:
    print("!!!The game is tie!!!")
elif a:
    print("!!!You Win!!!")
else:
    print("!!!You Loose!!!")


