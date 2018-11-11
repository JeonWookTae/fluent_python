#listcomp
LISTCOMP = [
    (1, '대한'),
    (2, '민국'),
    (3, '대통령'),
    (4, '문재인')
]
print(LISTCOMP)

#dictcomp
DICTCOMP = {key:word for key, word in LISTCOMP }
print(DICTCOMP)

'''
원자적 불변형은 모두 해시 가능하다.
'''
tt = (1,2,3)
print(hash(tt))

tt = (1,2,(30,40))
print(hash(tt))