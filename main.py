n = int(input('Ввести число: '))

if n % 2 != 0:
    print("Weird")


if n % 2 == 0:
    if n in range(2,5):
         print('Not Weird')

if n % 2 == 0:
    if n in range(6,20):
         print('Weird')

if n % 2 != 0:
    if n > 20:
        print("Not Weird")

print('Кінець')