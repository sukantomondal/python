'''
Count number of ways to reach destination in a Maze
Given a maze with obstacles, count number of paths to reach rightmost-bottommost cell from topmost-leftmost cell. A cell in given maze has value -1 if it is a blockage or dead end, else 0.

From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only.

Examples:

    Input: maze[R][C] =  {{0,  0, 0, 0},
                      {0, -1, 0, 0},
                      {-1, 0, 0, 0},
                      {0,  0, 0, 0}};
Output: 4

'''

import sys
sys.path.append('/home/sukanto/Development/python/basic')
from ds import *

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        

def count_path(maze):
    
    if not maze:
        pass

    n = len(maze)     # no  of row
    m = len(maze[0])  # no of col

    q = Queue()
    q.push(Point())

    count = 0

    while not q.empty():
        p = q.front()
        q.pop()

        if(p.x == n-1 and p.y == m-1):
            count+=1

        if(p.x + 1 < n and maze[p.x+1][p.y] == 1):
            q.push(Point(p.x+1, p.y))
        if(p.y+1 < m and maze[p.x][p.y+1] == 1):
            q.push(Point(p.x, p.y+1))

    return count


maze = [[1,1,1,1,1],[0,1,0,1,0],[1,1,1,1,1],[1,1,0,1,1]]

print("Path count" , count_path(maze))
