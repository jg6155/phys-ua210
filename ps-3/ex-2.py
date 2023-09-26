
from numpy import zeros,ones,dot
from time import time
import matplotlib.pyplot as plt

N = 50
A = ones([N,N], float)
B = ones([N,N], float)
def matrix_mult(N,A,B):
    C = zeros([N,N], float)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j]+= A[i,k]*B[k,j]
    return C

def matrix_mult_dot(N,A,B):
    C = zeros([N,N], float)
    for i in range(N):
        for j in range(N):
            C[i,j] = dot(A[i],B[:,j])
    return C

def time_exec(func, *args):
    start = time()
    func(*args)
    end = time()
    return end-start
sizes = []
reg_results = []
dot_results = []

for i in range(10, 100, 10):
    A = ones([i, i], float)
    B = ones([i, i], float)
    
    reg_res = time_exec(matrix_mult, i, A, B)
    dot_res = time_exec(matrix_mult_dot, i, A, B)
    
    sizes.append(i)
    reg_results.append(reg_res)
    dot_results.append(dot_res)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sizes, reg_results, 'o-', label='Regular Multiplication')
plt.plot(sizes, dot_results, 's-', label='Dot Multiplication')
plt.xlabel('Matrix Size (N)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. Matrix Size')
plt.legend()
plt.grid(True)
plt.show()



