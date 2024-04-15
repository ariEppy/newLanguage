from functools import reduce

# 9
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# 10
print("ANSWER 10:")
concat_strings = lambda strings: reduce(lambda x, y: x + ' ' + y, strings)

strings = ["Hello", "world", "from", "Lambda"]
result = concat_strings(strings)
print(result)

# 11
print("ANSWER 11:")
cumulative_sum_of_squares_of_even = lambda lists: list(
    map(lambda sublist: sum(map(lambda num: num ** 2, filter(lambda x: x % 2 == 0, sublist))), lists))

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = cumulative_sum_of_squares_of_even(lists)
print(result)

# 12
print("ANSWER 12:")

nums = [1, 2, 3, 4, 5, 6]
sum_squared = reduce(lambda acc, x: acc + x, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
print(sum_squared)

# 13
print("ANSWER 13:")
count_palindromes = lambda lists: list(
    map(lambda sublist: reduce(lambda acc, x: acc + 1 if x == x[::-1] else acc, sublist, 0), lists))

lists = [['level', 'noon', 'hello'], ['madam', 'racecar', 'python']]
result = count_palindromes(lists)
print(result)

# 14
print("ANSWER 14:")
print("\n"
      "In \"lazy evaluation\", \n"
      "values  are not calculated until they are actually needed.\n"
      " In the program, all values are pre-calculated even if they are not used. \n"
      " On the other hand, in the \"lazy evaluation\" approach,\n"
      "  the values are calculated only when they really work,\n"
      "   this allows for a more efficient management of resources\n")
