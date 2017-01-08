def pascal(a, b):
    rows = [[1], [1, 1]]
    index = 1
    while index < a:
        lastRow = rows[index]
        newRow = [1]
        rowIndex = 0
        while rowIndex<len(lastRow)-1:
            newRow.append(lastRow[rowIndex]+lastRow[rowIndex+1])
            rowIndex+=1
        newRow.append(1)
        rows.append(newRow)
        index+=1
    return rows[a][b]


print(pascal(100, 50))

