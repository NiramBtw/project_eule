"""
project euler 38
https://projecteuler.net/problem=38
by: Nir
Pandigital multiples
"""

def Is_valid_array(array, valid_values):
    for v in array:
        if v not in valid_values:
            return False
    return True


def Set_digits_counter(number, digits_counter):
    for d in str(number):
        digits_counter[int(d)] += 1


def Is_pandigital_multipication(number):
    n = 2
    digits_counter = [0] * 10
    parietal_multiplication = str(number)
    Set_digits_counter(number, digits_counter)
    while Is_valid_array(digits_counter, [0, 1]):
        if 0 == digits_counter[0] and \
                9 == sum(digits_counter[1:]) and \
                n > 1:
            return True, int(parietal_multiplication)
        multiplication = n * number
        multiplication_as_taring = str(multiplication)
        parietal_multiplication += multiplication_as_taring
        Set_digits_counter(multiplication_as_taring, digits_counter)
        n += 1
    return (False, 0)


def Get_max_pandigital_multipication():
    max_parietal_multiplication = 0
    for number in range(1, 99999, 1):
        (is_parietal_multiplication, parietal_multiplication) = \
            Is_pandigital_multipication(number)
        if is_parietal_multiplication and \
                max_parietal_multiplication < parietal_multiplication:
            max_parietal_multiplication = parietal_multiplication
    return max_parietal_multiplication



def main():
    
    print(Get_max_pandigital_multipication())


if __name__ == "__main__":
    main()
