#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Sigai"
import itertools, math
from operator import itemgetter
import time
from functools import wraps


def timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (function.__name__, str(t1 - t0))
              )
        return result

    return function_timer


def spiral(n, m):
    _status = itertools.cycle(['right', 'down', 'left', 'up'])  # 用于状态周期性的切换
    _movemap = {
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0),
        'up': (0, -1),
    }
    pos2no = dict.fromkeys([(x, y) for x in range(n) for y in range(m)])  # 生成字典键值是向量元组
    _pos = (0, 0)
    _st = next(_status)
    for i in range(1, n * m + 1):
        _oldpos = _pos
        _pos = tuple(map(sum, zip(_pos, _movemap[_st])))  # 根据状态进行移动
        if (_pos not in pos2no) or (pos2no[_pos]):  # 当超出范围或遇到障碍时切换方向
            _st = next(_status)
            _pos = tuple(map(sum, zip(_oldpos, _movemap[_st])))
        pos2no[_oldpos] = i
    return pos2no


def prime(n):
    if n is None:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5
    for p in range(7, int(math.sqrt(n)) + 1, 2):  # 只考虑奇数作为可能因子
        if n % p == 0:
            return False
    return True


def display_spiral(n,m):
    pos2no = spiral(n, m)
    for i in range(m):
        for j in range(n):
            print(pos2no[(j, i)], end='\t', )
        print('\n')
    print('-' * 5 * n)


class Uzimaki(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.rank={}
        self.spiral = spiral(self.n, self.m)


    @timer
    def get_prime_neighbors(self):

        nbs_pos = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 or y != 0]  # 邻居相对向量

        for i in range(1, self.n * self.m+1):
            i_pos = dict(zip(self.spiral.values(), self.spiral.keys()))[i]#得到i的坐标
            nbs = []#i的邻居数字
            for x, y in nbs_pos:
                num = self.spiral.get((i_pos[0] + x, i_pos[1] + y), None)
                nbs.append(num)
            tmp = []
            for j in nbs:
                if prime(j):
                    tmp.append(j)
            self.rank[i] = len(tmp)
        #print(self.rank)
        top = sorted(self.rank.items(), key=itemgetter(1), reverse=True)[0]
        print("在给定%d行和%d列的螺旋矩阵中，%d拥有的质数邻居最多,它有%d个质数邻居." % (self.n, self.m, top[0], top[1]))
        return top



# Uzimaki(day10, 100).display_spiral()
# Uzimaki(4, 4).neighbors(14)
# Uzimaki(4, 4).get_prime_neighbors(14)
if __name__ == '__main__':
    display_spiral(4,4)
    Uzimaki(400, 100).get_prime_neighbors()
