def maximalSquare(M): 
    rows = len(M) #rows
    cols = len(M[0]) #cols

    S = [[0 for k in range(cols)] for l in range(rows)] 
    for i in range(1, rows): 
        for j in range(1, cols): 
            if (M[i][j] == 1): 
                S[i][j] = min(S[i][j-1], S[i-1][j], 
                            S[i-1][j-1]) + 1
            else: 
                S[i][j] = 0

    colsurrent = S[0][0] 
    max_rows = 0
    max_colsols = 0
    for i in range(rows): 
        for j in range(cols): 
            if (colsurrent < S[i][j]): 
                colsurrent = S[i][j] 
                max_rows = i 
                max_colsols = j 
    colsurr = []
    for i in range(max_rows, max_rows - colsurrent, -1): 
        for j in range(max_colsols, max_colsols - colsurrent, -1): 
            colsurr.append((M[i][j]) )
    return int(len(colsurr)**0.5)
  
M = [[0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0]] 
  
print(maximalSquare(M))