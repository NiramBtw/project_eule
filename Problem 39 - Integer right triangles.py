"""
project euler 39
https://projecteuler.net/problem=39
by: Nir
Integer right triangles
"""

perimiter_lim = 1000

def Set_powers(array):
    for i in range(len(array)):
        array[i] = i * i


def Get_rightAngle_triangles_byPerimeter(perimeter_limit):
    powers = [0] * (perimeter_limit + 1)
    Set_powers(powers)
    perimeter_solutions = [[] for i in range(perimeter_limit + 1)]
    for p in range(3, perimeter_limit, 1):
        for c in range(1, p, 1):
            for a in range(1, c, 1):
                b = p - (a + c)
                if a + b <= c:
                    continue
                if powers[a] + powers[b] == powers[c]:
                    perimeter_solutions[p].append((a, b, c))
    return perimeter_solutions



def main():
    max_solutions = 0
    max_solutions_index = 0
    perimeter_solutions = Get_rightAngle_triangles_byPerimeter(perimiter_lim)
    for solution_index in range(len(perimeter_solutions)):
        number_of_solutions = len(perimeter_solutions[solution_index])
        if max_solutions < number_of_solutions:
            max_solutions = number_of_solutions
            max_solutions_index = solution_index

    
    print(max_solutions_index)


if __name__ == "__main__":
    main()
