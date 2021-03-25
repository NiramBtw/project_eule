"""
project euler 17
https://projecteuler.net/problem=17
by: Nir
Number letter counts
"""



def compute():
    ans = sum(len(to_en(i)) for i in range(1, 1001))
    return str(ans)


def to_en(n):
    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + (ones[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ones[n // 100] + "hundred" + (("and" + to_en(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return to_en(n // 1000) + "thousand" + (to_en(n % 1000) if (n % 1000 != 0) else "")
    else:
        raise ValueError()


ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if __name__ == "__main__":
    print(compute())
