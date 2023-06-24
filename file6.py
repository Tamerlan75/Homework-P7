# Ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
# одинаковое, фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке. (пара-ра-рам рам-пам-папам па-ра-па-да)

# couplet = input("Введите текст")
# list = couplet.split()
# list1 = []
# print(list)
# for i in range(len(list)):
#     count = 0
#     for j in list[i]:
#         if j == "а":
#             count += 1
#     list1.append(count)
# print(list1)
# sum = 0
# for i in list1:
#     sum += i
# if sum / len(list1) == list1[0]:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")
    
# 2. Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и 
# столбца.
# def print_operation_table( operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows+1):
#         for j in range(1, num_columns+1):
            
#             print(operation(i, j), end="\t" )
#         print()
# print_operation_table(lambda x,y: x*y)
