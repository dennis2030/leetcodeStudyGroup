func findMin(a int, b int, c int) int {
    var min = a
    if b < min {
        min = b
    }
    if c < min {
        min = c
    }
    return min
}

func initEdgeNum(b byte) int {
    if b == '1' {
        return 1
    } else {
        return 0
    }
}

func maximalSquare(matrix [][]byte) int {
    var numRows = len(matrix)
    if numRows == 0 {
        return 0
    }

    var numCols = len(matrix[0])
    if numCols == 0 {
        return 0
    }

    var record [][]int
    for i := 0; i < numRows; i++ {
        record = append(record, make([]int, numCols))
    }

    var best = 0

    for i := 0; i < numRows; i++ {
        record[i][numCols - 1] = initEdgeNum(matrix[i][numCols - 1])
        if record[i][numCols - 1] == 1 {
            best = 1
        }
    }

    for i := 0; i < numCols; i++ {
        record[numRows - 1][i] = initEdgeNum(matrix[numRows - 1][i])
        if record[numRows - 1][i] == 1 {
            best = 1
        }
    }

    for i := numRows - 2; i >= 0; i-- {
        for j := numCols - 2; j >= 0; j-- {
            if matrix[i][j] == '0' {
                continue
            }
            var battle = findMin(record[i][j + 1], record[i + 1][j], record[i + 1][j + 1]) + 1
            if battle > best {
                best = battle
            }
            record[i][j] = battle
        }
    }

    return best * best;
}
