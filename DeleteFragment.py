# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

my_string = str(input())

a1 = my_string.find("h")
a2 = my_string.rfind("h")

new_string = my_string[:a1] + my_string[a2 + 1:]
print(new_string)