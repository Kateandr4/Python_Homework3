#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов, отличной от 0.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19



my_list = [1.1, 1.2, 3.1, 5, 10.01]
fin_list = []
for i in my_list:
    if i % 1 != 0:
        fin_list.append(round(i % 1, 3))
i_max = 0.000
i_min = 0.999
for i in range(len(fin_list)):
      if i_max < fin_list[i]:
         i_max = fin_list[i]
      elif i_min > fin_list[i]:
           i_min = fin_list[i]
print(i_max - i_min)





