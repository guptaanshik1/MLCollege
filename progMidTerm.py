from math import sqrt

# factorial
def fact(n):
    if n == 1: return 1
    
    return n * fact(n - 1)

print(fact(4))

# distance
def findDistance(x1, x2, y1, y2, z1, z2):
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1))

print(findDistance(1, 2, 3, 4, 5, 6))

# addition of two matrices
mat1 = [
    [1, 2, 3],
    [3, 4, 5]
]

mat2 = [
    [5, 6, 1, 2],
    [7, 8, 3, 4]
]

summ2 = [[mat1[i][j] + mat2[i][j] for j in range(len(mat2))] for i in range(len(mat2))]
print(summ2)

# multiplication of two matrices
mul = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]

for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            mul[i][j] += mat1[i][k] * mat2[k][j]
            
print(mul)
            
# fibonacci
def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

print("Fibonacci series: ")
for i in range(10):
    print(fibo(i), end=' ')

print(fibo(10))

# concat and find length
# str1 = input("Enter string1: ")
# str2 = input("Enter string2: ")

# print(str1 + str2)
# print(len(str1 + str2))

# insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        j, key = i - 1, arr[i]
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [4, 5, 1, 2, 3]
print(arr)

insertionSort(arr)
print(arr)

# reading from a file
fptr = open("demo.txt", 'r')

if fptr:
    data = fptr.read()
else:
    print("No file")

print(data)
