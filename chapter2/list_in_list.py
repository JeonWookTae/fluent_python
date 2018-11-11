board = [['_']*3 for _ in range(3)]
print(board)

board[2][1] = 'X'
print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', 'X', '_']]

# 참조를 가진 3개의 리스트가 생성된다.
board = [['_']*3]*3
print(board)

board[2][1] = 'X'
print(board)
# [['_', 'X', '_'], ['_', 'X', '_'], ['_', 'X', '_']]

l = [1,2,3]
print(id(l))
l *= 2
print(id(l))
print(l)

t = (1,2,3)
print(id(t))
t *= 2
print(id(t))
#튜플은 id가 변한다. 시퀀스가 추가되면 시퀀스 전체를 삭제후 다시 생성한다.
print(t)