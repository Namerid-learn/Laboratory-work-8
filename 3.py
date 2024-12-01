def equal(n, s):
    if n == 0:
        return s == 0
    else:
        return equal(n // 10, s - n % 10)

try:    
    n = int(input("Введите n: "))
    s = int(input("Введите s: "))

    if n < 0 or s < 0:
        print ("Ошибка ввода!")
    else:
        if equal(n, s) == True:
            print ("Истина")
        else:
            print ("Ложь")
            
except ValueError:
    print ("Ошибка ввода!")
    
