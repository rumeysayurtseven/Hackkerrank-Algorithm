""" Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output
5
"""

"start"
n = int(input())
n1 = set(map(int,input().split()))
b = int(input())
b1 = set(map(int,input().split()))

setintersection = n1.intersection(b1)
print(len(setintersection));

"end"
