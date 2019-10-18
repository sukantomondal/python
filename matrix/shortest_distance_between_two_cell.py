'''
Shortest path in a Binary Maze
Given a MxN matrix where each element can either be 0 or 1. We need to find the shortest path between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1.

Expected time complexity is O(MN).

For example –

Input:
mat[ROW][COL]  = {{1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
                  {1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
                  {1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
                  {1, 1, 1, 0, 1, 1, 1, 0, 1, 0 },
                  {1, 0, 1, 1, 1, 1, 0, 1, 0, 0 },
                  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
                  {1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
                  {1, 1, 0, 0, 0, 0, 1, 0, 0, 1 }};
Source = {0, 0};
Destination = {3, 4};

Output:
Shortest Path is 11
'''

import sys
sys.path.append("/home/sukanto/Development/python/basic")
from ds import *


def min_distance(maze, src, dst):
    

    if not maze: 
        return

    n = len(maze)
    m = len(maze[0])

    q = Queue()
    q.push((src[0],src[1],0)) # A tuple that have x, y and distance source have distance 0

    while not q.empty():        
        p = q.front()
        q.pop()
        
        x = p[0]
        y = p[1]
        d = p[2]

        maze[x][y] = '$'

        if (x == dst[0] and y == dst[1]):
            return d

        if(x+1 < n and maze[x+1][y] == 1):
            q.push((x+1,y,d+1))
        if(x-1 >= 0 and maze[x-1][y] == 1):
            q.push((x-1,y,d+1))
        if(y+1 < m and maze[x][y+1] == 1):
            q.push((x,y+1, d+1))
        if(y-1 >= 0 and maze[x][y-1] == 1):
            q.push((x,y-1,d+1))
    return -1



maze = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
    ]


src = (0,0)
dst = (3,4)

print(min_distance(maze,src,dst))

