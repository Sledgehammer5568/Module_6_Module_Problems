# Emanuel Ramos
# 11/08/2022
#
# Problem 3: Uses the choice function within the random module to print a random day of the week

import random

# assign a variable associated to a list for each day of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# print a random day from the lsit using the choice function within the random module
print(random.choice(days))
