"""
output = " "
for i in reversed(range(5)):
    for x in range(i):
        output = "*" + output + "*"
    print(output.center(30))

"""


def my_function(x):
    return x[::-1]


string = "***** *****\n **** **** \n  *** ***  \n   ** **   \n    * *    "

print(string)

print(my_function(string))