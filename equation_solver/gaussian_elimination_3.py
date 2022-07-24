def echelon(matrix):
    for a in range(0,len(matrix) - 1):
        for i in range(1, len(matrix)):
            matrix[i] = [ matrix[i][u] - matrix[a][u] * matrix[i][a] / matrix[a][a] for u in range(len(matrix[a]))]
    return matrix

def echelon2(matrix):
    n = len(matrix) - 1
    for a in range(n, 0, -1): 
        for i in range(len(matrix) - 1):
            eq1 = []
            eq2 = []
            for o in matrix[a]:
                eq1.append(o * (-matrix[i][a]) / matrix[a][a])
            for e in range(len(eq1)):
                eq2.append(eq1[e] + matrix[i][e])
            matrix[i] = eq2
    return matrix
            
                


# M = [
#   [x0, y0, z0, c0] -> L0,
#   [x1, y1, z1, c1] -> L1,
#   [x2, y2, z2, c2] -> L2
# ]
# L0 * (-x1 / x0) + L1 -> L1
# L0 * (-x2 / x0) + L2 -> L2

# M = [
#   [x0, y0, z0, c0] -> L0,
#   [0,  y1, z1, c1] -> L1,
#   [0,  y2, z2, c2] -> L2
# ]
# L1 * (-y2 / y1) + L2 -> L2
# ----

# M = [
#   [x0, y0, z0, c0] -> L0,
#   [0,  y1, z1, c1] -> L1,
#   [0,  0,  z2, c2] -> L2
# ]
# L2 * (-z1/ z2) + L1 -> L1
# L2 * (-z0/ z2) + L0 -> L0

# M = [
#   [x0, y0, 0,  c0] -> L0,
#   [0,  y1, 0,  c1] -> L1,
#   [0,  0,  z2, c2] -> L2
# ]
# L1 * (-y0/ y1) + L0 -> L0

# M = [
#   [x0, 0,  0,  c0] -> L0,
#   [0,  y1, 0,  c1] -> L1,
#   [0,  0,  z2, c2] -> L2
# ]

# [c0/x0, c1/y1, c2/z2]
