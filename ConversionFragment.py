# Дана строка, в которой буква h встречается как минимум два раза.
# Разверните последовательность символов, заключенную между первым и последним появлением буквы h,
# в противоположном порядке.

my_string = str(input())

a1 = my_string.find("h")
a2 = my_string.rfind("h")

new_string = my_string[a1+1:a2]
final_string = my_string[:a1+1] + new_string[::-1] + my_string[a2:]
print(final_string)
