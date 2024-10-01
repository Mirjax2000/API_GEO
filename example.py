# def has_duplicate(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 return True
#     return False


# pole: list = [1, 2, 3]
# print(has_duplicate(pole))


def transpose_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(transpose_matrix(matrix))


# def matrix_transpose(matrix):
#     temp = zip(*matrix)
#     result = []
#     for row in temp:
#         result.append(list(row))

#     return result


# print(matrix_transpose(matrix))


# def has_duplicate(arr):
#     seen: set[int] = set()
#     for item in arr:
#         if item in seen:
#             return True
#         seen.add(item)
#     return False


# pole = [1, 2, 3, 1]
# print(has_duplicate(pole))
