import io
import sys

_INPUT = """\
8
2750 628
161 8
3263 15
1462 1959
1687 1029
2587 644
113 201
2048 16
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  Deg,Dis=map(int,input().split())
  s=int(Dis/6+0.5)
  if s<=2: print('C',0)
  else:
    d=['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
    dir=(Deg*10+1125)//2250
    f=[2,15,33,54,79,107,138,171,207,244,284,326,9000]
    for i in range(13):
      if s<=f[i]: print(d[dir%16],i);break