def generate(numRows):
    def helper(num_rows):
        if numRows < 1:
            return []
        if num_rows == 1:
            return [[1]]
        if num_rows == 2:
            return [[1],[1,1]]
        former_part = helper(num_rows-1)
        last_row    = former_part[-1]
        tmp         = []
        for i in range(1, len(last_row)):
            tmp.append(last_row[i-1]+last_row[i])
        tmp.insert(0, 1)
        tmp.append(1)
        return former_part + [tmp]
    return helper(numRows)

if __name__ == "__main__":
    numRows1 = 0
    numRows2 = 1
    numRows3 = 7
    print(generate(numRows1))
    print(generate(numRows2))
    print(generate(numRows3))