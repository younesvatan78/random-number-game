import random

takenNum = random.randrange(1000)
converted_input = int(input("Try to guess the number: "))
print(takenNum)

while True:   
    if converted_input == takenNum:
        print('yay,Hit! (:')
        again = input('try again?(y or n)')
        if again == 'y':
            converted_input = int(input("Try to guess the number: "))
        if again != 'y':
            print('bye')
            break
    elif converted_input > takenNum:
        print('nooo, its smaller')
        converted_input = int(input("Try to guess the number: "))
    else:
        print('nooo, man try again a bigger one (;')
        converted_input = int(input("Try to guess the number: "))
       
