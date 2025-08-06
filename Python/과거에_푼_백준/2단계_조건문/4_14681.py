x = int(input())
y = int(input())

def a():

    if x > 0:
        if y > 0:
            print(1)
        elif y < 0:
            print(4)
    elif x < 0:
        if y > 0:
            print(2)
        elif y < 0:
            print(3)
#a()

#풀이2
def b():
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(4)
    elif x < 0 and y < 0:
        print(3)
    elif x < 0 and y > 0:
        print(2)
b()
