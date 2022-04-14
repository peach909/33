#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys
EPS = 1e-10
if __name__ == '__main__':
    x = float(input("x = "))
    if x == 0:
        print("Ошибка", file=sys.stderr)
        exit(1)
    a = -x**3/3
    S, n = a, 0
    while math.fabs(a) > EPS:
        a *= ((2*n + 3)*(n + 1))/((2*n+1)*x**2)
        S += a
        n += 1
    print(f"erf({x}) = {2/ math.sqrt(math.pi) + S}")