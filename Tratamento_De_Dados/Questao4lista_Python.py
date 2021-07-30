ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

while(True):
    numero = int(input("escreva  um numero inteiro entre 0 a 999: "))

    if(numero == 0):
        break

    i = 0

    while( numero > 0):
        if( numero >= ints[i] ):
            print (str(nums[i]))
            numero = numero - ints[i]
        else:
            i= i + 1