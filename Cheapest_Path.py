inp = raw_input()
mat = []
for i in range(int(inp)):
    mat.append(raw_input().split(","))
inp = int(inp)
sums = []
_points = []

class Point:
    def __init__(self, sindex, loc, psum):
        self.startIndex = sindex
        self.locations = [self.startIndex]
        if len(loc)!=0:
            self.locations+=loc
        self.csum = psum + int(mat[self.startIndex[0]][self.startIndex[1]])
    
    def makePoints(self):
        temp = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not ((i == 0) and (j == 0)):
                    if ((self.startIndex[0]+i >= 0) and (self.startIndex[0]+i < inp)):
                        if ((self.startIndex[1]+j >= 0) and (self.startIndex[1]+j < inp)):
                            if ([self.startIndex[0]+i, self.startIndex[1]+j] not in self.locations):
                                temp.append([[self.startIndex[0]+i, self.startIndex[1]+j], self.csum])
        return temp
        
temp0 = 0
for i in mat:
    for j in i:
        temp0+=int(j)

if inp == 1:
    print mat[0][0]        
else:
    for i in range(inp):
            _points.append(Point([0, i], [], 0))
          
    while len(_points)>0:
        new_points = []          
        for i in _points:
            t = i.makePoints()
            if len(t)!=0:
                for j in t:
                    new_points.append(Point(j[0], i.locations, j[1]))
                    
        _points = new_points
        new_points = []     
        
        for i in _points:
            if i.startIndex[0] == (inp-1):
                if i.csum < temp0:
                    temp0 = i.csum
            elif i.csum < temp0:
                new_points.append(i)
        _points = new_points
print temp0