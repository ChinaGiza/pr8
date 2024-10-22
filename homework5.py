arr = []
print("Введите числа [введите stop или end для завершения ввода]: ")
while True:
    i = input()
    if i == "stop" or i == "end":
        break
    arr.append(i)

for i in range(0, len(arr)):
    if (arr[i].count("-") <= 1 and arr[i].lstrip("-").replace(".", "", 1).isdigit()):
        arr[i] = float(arr[i])
    else:
        arr.clear()
        break

if len(arr) == 0:
    print("Ошибка: введенные значения не являются числами")
else:
    print(f"Результат: {sum(arr)}")
