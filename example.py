# def has_duplicate(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 return True
#     return False


# pole: list = [1, 2, 3]
# print(has_duplicate(pole))


# def transpose_matrix(matrix):

#     rows= len(matrix)
#     cols = len(matrix[0])
#     result = [[0] * rows for _ in range(cols)]

#     for i in range(rows):
#         for j in range(cols):
#             result[j][i] = matrix[i][j]

#     return result

# matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6]]


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

# pole: list[int | float] = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     0,
#     -1,
#     -2,
#     -3,
#     -4,
#     -5,
#     1.2,
#     3.2,
#     4.5,
#     -1.4,
#     -5.2,
# ]


# def spocitej_mi_to(data) -> str:
#     nula: list[int] = list(item for item in data if item == 0)
#     kladny: list[int | float] = list(item for item in data if item > 0)
#     zaporny: list[int | float] = list(item for item in data if item < 0)
#     desetine: list[float] = list(item for item in data if isinstance(item, float))
#     return f"nula: {len(nula)}\nkladny: {len(kladny)}\nzaporny: {len(zaporny)}\ndesetinny: {len(desetine)}"


# print(spocitej_mi_to(pole))


# pole = [1,2,3,4,5,-1,-2,-3,-4,-5,0,5.1,4.2,3.3,2.4,1.5]


# def urci_pocet(cisla):
#     kladna = 0
#     zaporna = 0
#     nuly = 0
#     desetinna = 0

#     for i in cisla:
#         if not isinstance(i, (int, float)):
#             continue
#         if i < 0:
#             zaporna += 1
#         elif i == 0:
#             nuly += 1
#         elif i > 0:
#             kladna += 1
#         if isinstance(i, float):
#             desetinna += 1

#     print(f"Počet kladných čísel v poli: {kladna}")
#     print(f"Počet záporných čísel v poli: {zaporna}")
#     print(f"Počet nul v poli: {nuly}")
#     print(f"Desetinných čísel v poli: {desetinna}")


slova = [
    "radar",
    "level",
    "madam",
    "civic",
    "rotor",
    "deified",
    "noon",
    "racecar",
    "refer",
    "stats",
]


def palindrom(slovo) -> bool:
    return True if slovo == slovo[::-1] else False


def porovnej(pole) -> bool:
    flag = True

    for item in pole:
        if not palindrom(item):
            flag = False

    return flag


print(porovnej(slova))
