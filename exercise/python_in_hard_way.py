
# 1. loop - while
# a = 0
# while a < 101:
#   print a
#   a += 1

# 1. loop - for

# for x in range(100):
#   print x

# 2. calculate

# print 3+2+1-5+4%2-1/4+6

# 3. print special character
# I am 6'2" tall.

# print "I am 6'2\" tall."

# 4. connect string with -
# "Mary had a little lamb."

# sentence = "Mary had a little lamb."
# newsentence = sentence.replace(' ', '-')
# print newsentence

# zeroandones = '0101101110'
# for char in zeroandones:
#   print char

animals = ["cat", "rabbit", "tortoise", "cat", "rabbit", "dinosaur"]

# counter = 0
# for anml in animals:
#   # print(anml)
#   if anml == 'cat':
#     counter += 1
#     # print(counter)
# print(counter)

# nums = []
# print(animals[1:])
# for i in range(len(animals)):
#   # print 'outer: ' + animals[i]
#   for j in range(len(animals[1:])):
#     # print 'innter: ' + animals[j]
#     if animals[i] == animals[j]:
#       print('found one: ' + animals[j])

# number_list = range(-5, 5)
# filterd_anmls = list(filter(lambda x: x != 'cat', animals))

filterd_anmls = list(dict.fromkeys(animals))
# print(filterd_anmls)

keys = dict.fromkeys(animals)
# print(keys)

animal_list = list(keys)
# print(animal_list)

no_repeated_list = []
for orig in animals:
  if orig not in no_repeated_list:
    no_repeated_list.append(orig)

# print(no_repeated_list)

# sort list:
random_list_sort = [1, 3, 5, -1, 2, 9, 6, 4, 0]

def larger(x, y):
  return x if x > y else y

the_largest = reduce(larger, random_list_sort)
print(the_largest)