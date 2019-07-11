from matmul import readm, matmul
#1.read matrix A from
A = readm('A.csv')

#2.read matrix b from 'b.csv'
b = readm('b.csv')
#3.find the result of C = A x b
def matmul(A,b):
    m, n = len(A), len(b[0])
    J = len(A[0]) # A-mxJ #b - Jxn
    if len(A[0])== len(b):
        C = [ [0]*n] for i in range(m)]
        for i in range(m):
            for c in range(n):
                C[r][c] = sum( [A[r][j]*b[j][0] for j in range(3) ])
        
        return c
    return [] # ไม่สามารถดูคูณได้

#4.print c
C = matmul(A, b)
#5.test
c = A*b
print(c)
A = [
    [1,2,3,4],
    [2,1,3,4],
    [1,3,2,1]
]
b = [
    [1,2],
    [3,1],
    [2,2],
    [3,4]
]
c = matmul(A, b)
print('-----')
for row in C:
    print(row)
print('-----')
