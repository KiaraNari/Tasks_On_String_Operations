# Дана строка.
my_str = str(input())
# Сначала выведите третий символ этой строки.
print(my_str[2])
# Во второй строке выведите предпоследний символ этой строки.
print(my_str[-2])
# В третьей строке выведите первые пять символов этой строки.
print(my_str[:5])
# В четвертой строке выведите всю строку, кроме последних двух символов.
print(my_str[:-2])
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
print(my_str[0::2])
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print(my_str[1::2])
# В седьмой строке выведите все символы в обратном порядке.
print(my_str[::-1])
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
print(my_str[-1::-2])
# В девятой строке выведите длину данной строки.
print(len(my_str))

