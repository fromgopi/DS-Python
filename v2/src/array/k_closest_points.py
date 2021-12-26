# K Closest points from Origin
from random import randint
from typing import List

def k_closest(points: List[List[int]], k: int):
    """K Closest points from origin"""
    left, right, p = 0, len(points)-1, len(points)
    while p != k:
        p = __partition(P=points, left=left, right=right)
        if p < k:
            left = p + 1
        else:
            right = p - 1
    return points[:k]


def __partition(P: List[List], left, right):
    e_distance = lambda p: p[0]**2 + p[1]**2
    random_pivot = randint(left, right)
    P[right], P[random_pivot] = P[random_pivot], P[right]
    i, pivot_distance = left, e_distance(P[right])
    for j in range(left, right+1):
        if e_distance(P[j]) <= pivot_distance:
            P[i], P[j] = P[j], P[i]
            i += 1
    
    return i-1


if __name__ == '__main__':
    points = [[1,3],[-2,2]]
    res = k_closest(points=points, k=1)
    print(res)