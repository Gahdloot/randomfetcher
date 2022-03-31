import random

hii = []


#this Function splits the user input and use them to generate its figures
def RanGenrator(x):
    l = x // 2
    b = random.randint(1, l)
    xr = l - b
    c = random.randint(0, xr)
    xr = b - c
    d = random.randint(0, xr)
    o = b + c + d
    i = x - o
    hii.append(b)
    hii.append(c)
    hii.append(d)
    hii.append(i)
    #print(f'your numbers are {b},{c},{d},{i} which make up {x}')


'''def randi():
    w = random.choice(hii)
    print(w)
    hii.remove(w)'''



try:
    rr = int(input('Enter a random number from 20 - 100 : '))
    RanGenrator(rr)
    print(hii)
    print(f'That Makes up {rr}')

except ValueError :
    print('Invalid Input Try Again')


except IndexError:
    print('ouch!! code crash try again!!!')

