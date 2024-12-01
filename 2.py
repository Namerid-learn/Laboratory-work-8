def ScalarProduct(A, B):
    s = 0
    for i in range(len(A)):
        s += A[i] * B[i]
    return s

try:    
    A = list(map(float, input("Введите координаты вектора A (2 или 3 числа через пробел): ").strip().split(" ")))
    B = list(map(float, input("Введите координаты вектора B (2 или 3 числа через пробел): ").strip().split(" ")))
    X = list(map(float, input("Введите координаты вектора X (2 или 3 числа через пробел): ").strip().split(" ")))
    Y = list(map(float, input("Введите координаты вектора Y (2 или 3 числа через пробел): ").strip().split(" ")))

    if (len(A) != 2 and len(A) != 3) or \
       (len(B) != 2 and len(B) != 3) or \
       (len(X) != 2 and len(X) != 3) or \
       (len(Y) != 2 and len(Y) != 3):
        print ("Ошибка ввода!")
    else:
        print ("\nS1 (X, Y) равно:", ScalarProduct(X, Y))
        print ("S2 (A, B) равно:", ScalarProduct(A, B))

except ValueError:
    print ("Ошибка ввода!")