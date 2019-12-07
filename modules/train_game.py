from .num import *
import math

def generate(a, b, c, d):

    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
    except:
        return None

    item = Num(a, b, c, d)
    solutions = item.get_solutions()
    i = 0

    if len(solutions) == 0:
        print("No solutions found.")
    else:
        while i < len(solutions):
            print(f"Solution {i+1}: {solutions[i]}")
            i += 1

    return solutions

def main(a, b, c, d):
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    d = int(nums[3])
    generate(a, b, c, d)

if __name__=="__main__":
    main()
