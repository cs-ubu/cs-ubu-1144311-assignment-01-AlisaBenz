import numpy as np
import numpy.linalg as linalg
A = np.array( 
    [
        [ 4.0, -2.0,  1.0],
        [-2.0,  4.0, -2.0],
        [ 1.0, -2.0,  3.0] 
    ] 
)
b = np.array( [1.0, 4.0, 2.0] )
print(np.dot(A,b))
A[0][0]*b[0] A[0][1]*b[1] A[0][2]*b[2]
A[0][3]*b[3] A[0][4]*b[4] A[0][5]*b[5]
A[0][6]*b[6] A[0][7]*b[7] A[0][8]*b[8]
