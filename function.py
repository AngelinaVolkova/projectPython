# todo: lambda
add = lambda x, y: x+y
print(add(2, 5))
print(add('Hello', ' world'))

print((lambda x, y: x+y)(2,6))

# todo: кортеж
fun = lambda *args: args
print(fun(23, 456, 65))
