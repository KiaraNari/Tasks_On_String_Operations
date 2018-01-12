# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите.

my_str = str(input())

# print(my_str.find("f"))
# print(my_str.rfind("f"))

if my_str.find('f') == -1:
    print()
elif my_str.find('f') == my_str.rfind('f'):
    print(my_str.find('f'))
else:
    print(my_str.find('f'), my_str.rfind('f'))