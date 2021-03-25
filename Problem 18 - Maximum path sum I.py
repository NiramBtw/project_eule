"""
project euler 1
https://projecteuler.net/problem=17
by: Nir
Number letter counts


create new blank triangle with the same dimensions as the original big triangle.
 for each cell of the big triangle, that consider the sub-triangle whose top is at this cell,
 calculate the maximum path sum when starting from this cell, and store the result
 in the corresponding cell of the blank triangle.

 if start at particular cell, what is the maximum path total?
 If the cell is at the bottom of the big triangle?
 then it is simply the cells value. Otherwise is
 the cells value plus either -> {the maximum path total of the cell down and to the left}
 or {the maximum path total of the cell down and to the right} , whichever is greater.
 so computing the blank triangles values from bottom up is needed, the dependent values are always
 computed before they are utilized. 
 dynamic programming:
     https://www.geeksforgeeks.org/dynamic-programming/
     https://skerritt.blog/dynamic-programming/
     https://towardsdatascience.com/solving-problems-with-dynamic-programming-ea4a872dae61
"""



def compute():
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return str(triangle[0][0])


triangle = [  # mutable
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]

if __name__ == "__main__":
    print(compute())
