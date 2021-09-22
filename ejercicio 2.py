while True:

    a = int(input("Ingrese un numero entero de dos digitos: "))

    if a > 9 and a < 100:

        b = a % 10

        a = a // 10

       
        print(a)
        print(b)
        
    else:
        print("El numero ingresado debe ser un entero entre 10 y 99 ")
