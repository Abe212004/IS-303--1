blah = 25

def is_odd (numero):
    odd = True
    if numero % 2 == 0:
        odd = False
    if numero % 2 != 0:
        odd = True

    print(blah)
    
    return odd

is_odd = lambda numero: numero % 2 != 0

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")
