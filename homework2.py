def sum(a, b):
    print("Результат суммы: " + f"{a + b}")

while True:
    Num1 = input("Введите первое число [type q to quit]: ")
    Num2 = input("Введите второе число [type q to quit]: ")
    if (Num1.count("-") <= 1 and Num2.count("-") <= 1 and
        Num1.lstrip("-").replace(".", "", 1).isdigit() and
        Num2.lstrip("-").replace(".", "", 1).isdigit()):
        sum(float(Num1), float(Num2))
    elif (Num1 == "q" or Num2 == "q"):
        break
    else:
        print("Ошибка: введенные значения не являются числами")
