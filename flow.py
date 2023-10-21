# create a list of numbers
numbers = [1, 2, 3, 4, 5]

# print the list
print(numbers)

# access the first element of the list
print(numbers[0])

# access the last element of the list
print(numbers[-1])

# add an element to the end of the list
numbers.append(6)

# print the updated list
print(numbers)

# remove the last element from the list
numbers.pop()

# print the updated list
print(numbers)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# range() function
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:  # In a for loop, the else clause is executed after the loop reaches its final iteration.
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# match statement


def http_error(s):
    match s:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error(404))
print(http_error(500))

# match statement with multiple patterns


def match_to_name(x):
    match x:
        case 1 | 2 | 3:
            return "low"
        case 4 | 5 | 6:
            return "medium"
        case 7 | 8 | 9:
            return "high"


print(match_to_name(2))

# The default value is evaluated only once.
# This makes a difference when the default is a mutable object such as a list,
# dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# call the function
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
