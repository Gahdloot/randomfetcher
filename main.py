import random


#this Function splits the user input and use them to generate its figures
def RanGenrator(x):
    Predicted_Values = []
    l = x // 2
    b = random.randint(1, l)
    xr = l - b
    c = random.randint(0, xr)
    xr = b - c
    d = random.randint(0, xr)
    o = b + c + d
    i = x - o
    Predicted_Values.append(b)
    Predicted_Values.append(c)
    Predicted_Values.append(d)
    Predicted_Values.append(i)
    return Predicted_Values
    #print(f'your numbers are {b},{c},{d},{i} which make up {x}')


'''def randi():
    w = random.choice(hii)
    print(w)
    hii.remove(w)'''



'''try:
    input_value = int(input('Enter a random number from 20 - 100 : '))
    print(f'{RanGenrator(input_value)} Are Random numbers that make up {input_value}')

except ValueError :
    print('Invalid Input Try Again')


except IndexError:
    print('ouch!! code crash try again!!!')'''