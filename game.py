import random
name1=input(("player 1 name,:"))
name2=input(("player 2 name,:"))
d1=random.randint(1,25)
d2=random.randint(1,25)
s1=25
s2=25
print("player one turn,:")
while (True):
    g=int(input("enter ur guess,:"))
    s1=s1-1
    if d1==g:
        print("ur guess is correct")
        break
    elif d1<g:
        print("ur guess is more")
    else:
        print("ur guess is less")
print("player two turn,:")
while (True):
    g=int(input("enter ur guess,:"))
    s2=s2-1
    if d2==g:
        print("ur guess is correct")
        break
    elif d2<g:
        print("ur guess is more")
    else:
        print("ur guess is less")
if s1==s2:
    print("draw")
elif s1<s2:
    print("player 2 wins")
else:
    print("player 1 wins")