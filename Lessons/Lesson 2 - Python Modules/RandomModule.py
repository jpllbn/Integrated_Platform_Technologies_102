# import random
#
# rand = random.random()
#
# print(rand)

# import random
#
# RandUniform = random.uniform(10,20)
#
# print(f"{RandUniform:2f}")

# import random
#
# RandInt = random.randint(10,20)
#
# print(RandInt)

# import random
#
# RandRange = random.randrange(1,10,2)
#
# print(RandRange)

# import random
#
# fruits = ['apple', 'banana', 'cherry']
# rand = random.choice(fruits)
#
# print(rand)

# random.shuffle

# import random
#
# deck = [1,2,3,4,5]
#
# random.shuffle(deck)
#
# print(deck)

# random.sample

# import random
#
# numbers = range(1,1000)
#
# rand = random.sample(numbers, 500)
#
# for i in rand:
#     print(i)

# random.SystemRandom()

# import random
#
# secure_random = random.SystemRandom()
#
# generateKey = secure_random.randint(1,100)
#
# print(generateKey)


import random
import string

characters = string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase + string.digits

secure_random = random.SystemRandom(characters)

generateKey = ''.join(random.choice(characters) for i in characters)

print(f"Key Generated: {generateKey}")