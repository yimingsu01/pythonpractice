i = 0
target = 5
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# temp = matrix[i+1][0: (i + 1)]
# temp = matrix[i + 1][0 : i + 1]


# print(temp)
while i < len(matrix) - 1:
    if matrix[i][i] == target:
        print(True)
        break
    elif matrix[i + 1][i + 1] == target:
        print(True)
        break
    elif matrix[i][i] < target < matrix[i + 1][i + 1]:
        temp = matrix[i + 1][0: i + 1]
        count = 1
        temp.append(matrix[0: (i + 1)][0][i + 1])
        while count <= i:
            temp.append(matrix[0: (i + 1)][count][i + 1])
            count += 1
        temp += matrix[i + 1][0: (i + 1)]
        temp.sort()

        if target in temp:
            print(True)
            break
        else:
            print(False)
            break
    else:
        i += 1

