matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,0,1,2],
        [3,4,5,6]]
res=[]
while matrix:
    if matrix:  res.extend(matrix.pop(0))
    if matrix:  res.extend([i.pop() for i in matrix])
    if matrix:  res.extend(matrix.pop()[::-1])
    if matrix:  res.extend([i.pop(0) for i in matrix][::-1])
print(res)
