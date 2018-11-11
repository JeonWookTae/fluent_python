lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude, longitude)

print(divmod(20,8))

t = (20,8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient, remainder)

a, b, *rest = range(5)
print(a, b, rest)
# 0 1 [2, 3, 4]

a, b, *rest = range(2)
print(a, b, rest)
# 0 1 []

a, *rest, b = range(5)
print(a, rest, b)
# 0 [1, 2, 3] 4

