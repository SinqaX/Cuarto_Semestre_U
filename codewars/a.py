"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""
# def count(s):
#     dic ={}
#     for caracter in s:
#         if caracter not in dic:
#             dic[caracter] = 1
#         else:
#             dic[caracter] += 1
#     return dic

# print(count('aba'))
# print(count(''))
# print(count('aa'))
# print(count('aabb'))


# def divisors(n):
#     z = 0
#     i = 1
#     while i <= n:
#         if n % i == 0:
#             z += 1
#         i += 1
#     return z
# divisors(1) #1
# divisors(4) #3
# divisors(5) #2
# divisors(12) #6
# divisors(30) #8
# divisors(4096) #13

