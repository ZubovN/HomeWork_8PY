
import csv

with open('HomeWork_8PY-main/phone.csv', 'r') as file:
    reader = csv.reader(file)
    line = list(reader)

row_number = int(input("Введите номер строки: ")) - 1

with open('HomeWork_8PY-main/phone_1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(line[row_number])

print("Запись сохранена в файл phone_1.csv")
