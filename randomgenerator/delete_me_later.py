import random

lst = ['a', 'b', 'c', 'd', 'e', 'f']
for value in random.sample(lst, 4):
    print(value)

print("Random integers between 0 and 9: ")
for i in range(4, 15):
    y = random.randrange(9)
    print(y)

from secrets import randbelow

for _ in range(3, 9):
    print(randbelow(15))

# Python code to generate
# random numbers and
# append them to a list


# Function to generate
# and append them
# start = starting range,
# end = ending range
# num = number of
# elements needs to be appended
def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


# Driver Code
num = 10
start = 20
end = 40
print(Rand(start, end, num))

# Python code to generate
# random numbers and
# append them to a list


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(np.random.randint(start, end))

    return res


# Driver Code
num = 10
start = 20
end = 40
print(Rand(start, end, num))

import random

num = 10
start = 20
end = 40

result = random.sample(range(start, end + 1), num)

print(result)

from functools import reduce

num = 10
start = 20
end = 40

result = reduce(lambda acc, x: acc + [np.random.randint(start, end)], range(num), [])

print(result)
# This code is contributed by Rayudu.


from numpy.random import Generator, PCG64DXSM

pcg64dxsm_rng = Generator(PCG64DXSM())
pcg64dxsm_rng.random()
# 0.3472568589560456


import numpy as np

rng = np.random.default_rng()

rng.uniform()
# 0.5425301829704396

rng.uniform(low=3.4, high=5.6)
# 4.656018709365851


import numpy as np

rng = np.random.default_rng()
for i in range(5):
    rng.integers(3)
...
# 1
# 2
# 0
# 1
# 2


for count in range(5):
    rng.integers(low=1, high=4)
...
# 3
# 2
# 3
# 1
# 2


rng = np.random.default_rng()

input_array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
rng.choice(input_array_1d, size=3, replace=False)
# array([ 6, 12, 10])

rng.choice(input_array_1d, size=(2, 3), replace=False)
# array([[ 8, 12, 11], [10,  7,  5]])
