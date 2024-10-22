Num1 = input("Введите первое число: ")
Num2 = input("Введите второе число: ")
if (Num1.count("-") <= 1 and Num2.count("-") <= 1 and
    Num1.lstrip("-").replace(".", "", 1).isdigit() and
    Num2.lstrip("-").replace(".", "", 1).isdigit()):
        print(f"Целые числа между {Num1} и {Num2}:")
        Num1 = float(Num1)
        Num2 = float(Num2)
        if Num1 > Num2:
            Num1, Num2 = Num2, Num1
        if Num1 >= 0:
            Num1 = int(Num1) + 1
        else:
            if Num1 == int(Num1):
                Num1 = int(Num1) + 1
            else:
                Num1 = int(Num1)
        i = Num1
        while i < Num2:
            print(i)
            i += 1
else:
    print("Ошибка: введенные значения не являются числами")
