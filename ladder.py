""" Created by Shahen Kosyan on 11/28/17 """

import math

if __name__ == "__main__":
    h, a = [int(x) for x in input().split()]
    l = (h / math.sin(math.radians(a)))
    print(math.ceil(l))