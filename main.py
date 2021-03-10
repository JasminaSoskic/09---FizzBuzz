print("This program prints numbers in some range, except for numbers divisible by 3 and 5")
num = int(input("Insert number between 1 an 100: "))

for i in range(1,num+1):
    if i % 3 == 0 and i % 5 == 0:
        print ("fizzbuzz")
    elif i % 3 == 0:
        print ("fizz")
    elif i % 5 == 0:
        print ("buzz")
    else:
        print(i)
#        print ("{0}".format(i))