<<<<<<< HEAD
<<<<<<< HEAD
# def has_duplicate(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 return True
#     return False


# pole: list = [1, 2, 3, 1]
# print(has_duplicate(pole))


# def transpose_matrix(matrix):

#     rows= len(matrix)
#     cols = len(matrix[0])
#     result = [[0] * rows for _ in range(cols)]

#     for i in range(rows):
#         for j in range(cols):
#             result[j][i] = matrix[i][j]

#     return result

matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6]]


def matrix_transpose(matrix):
    temp = zip(*matrix)
    result = []
    for row in temp:
        result.append(list(row))

    return result


print(matrix_transpose(matrix))
=======
def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(prime_number(7))
>>>>>>> parent of 8128e21 (makame)
=======
>>>>>>> parent of 0dcbe44 (makame)
