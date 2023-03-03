# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:30:55 2021

@author: sibuj

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

"""

import copy as cp


class Solution(object):
    
    def QualifyingIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        AllOnesInGrid=[]
        #print("Input Grid size {}x{} ".format(m, n))
        
        #Finding Ones in Grid values
        for x in range(0, m):
            for y in range(0, n):
                if (grid[x][y])>0:
                    AllOnesInGrid.append((x, y))

        #print("Qualifying Island locations: {}".format(AllOnesInGrid))
        #print("Total number of individual Islands: {}".format(len(AllOnesInGrid)))
 
        #Return [(r,c),...] of Ones in Grid
        return AllOnesInGrid
    
    
    #Recursive Function
    def FindLongestIsland(self, PartOfSameIsland, CurrLongestIsland):
        
        for i in range(0,len(PartOfSameIsland)):
            if PartOfSameIsland[i] in AllOnesInGrid_MutableCopy:
                r=PartOfSameIsland[i][0]
                c=PartOfSameIsland[i][1]
                #print(r,c)
                #For i'th (r,c), check if row value 'r' and column value 'c' qualify for 4 directional traversal
                #Eg. if r=zero'th row, then it can traverse left, right and down. Not up 
                if r-1>=0: #Up
                    FourDims.append((r-1, c))
                if r+1<=m: #Down
                    FourDims.append((r+1, c))
                if c-1>=0: #Left
                    FourDims.append((r, c-1))
                if c+1<=n: #Right
                    FourDims.append((r, c+1))
                #print(FourDims)
                
                for j in FourDims:
                    if j in AllOnesInGrid_MutableCopy and j not in PartOfSameIsland:
                        PartOfSameIsland.append((j))
                        CurrLongestIsland+=1
                
                AllOnesInGrid_MutableCopy.remove(PartOfSameIsland[i])
                CurrLongestIsland=self.FindLongestIsland(PartOfSameIsland, CurrLongestIsland)

        return CurrLongestIsland

    
if __name__ == "__main__":
    
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,1,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    m=len(grid) #Rows
    n=len(grid[0]) #Columns
    PartOfLongestIsland=[]
    maxAreaOfland=0

    x=Solution()
    rAllOnesInGrid=x.QualifyingIslands(grid)
    #print(rAllOnesInGrid)

    if len(rAllOnesInGrid)>0:
        AllOnesInGrid_MutableCopy=cp.deepcopy(rAllOnesInGrid)
        CurrLongestIsland=1 #As atleast one island exists
        for i in range(0, len(rAllOnesInGrid)):
            PartOfSameIsland=[]
            FourDims=[]
            #Start from 0 position of the ones grid [(r, c),....]
            if rAllOnesInGrid[i] in AllOnesInGrid_MutableCopy:
                PartOfSameIsland.append(rAllOnesInGrid[i]) 
                #AllOnesInGrid_MutableCopy.remove(rAllOnesInGrid[i])
                LongestIsland=x.FindLongestIsland(PartOfSameIsland, CurrLongestIsland)
                if LongestIsland>maxAreaOfland:
                    PartOfLongestIsland=PartOfSameIsland
                    maxAreaOfland=LongestIsland
    
    #print(PartOfLongestIsland)
    print(maxAreaOfland)

    
    