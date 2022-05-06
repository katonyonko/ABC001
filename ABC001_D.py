import io
import sys

_INPUT = """\
6
4
1148-1210
1323-1401
1106-1123
1129-1203
1
0000-2400
6
1157-1306
1159-1307
1158-1259
1230-1240
1157-1306
1315-1317
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  ans=[0]*289
  tmp=set()
  for i in range(N):
    x=input()
    s,e=x[:4],x[5:]
    ans[12*int(s[:2])+int(s[2:])//5]+=1
    ans[12*int(e[:2])+(int(e[2:])-1)//5+1]-=1
  i=0
  tmp=0
  while i<289:
    tmp+=ans[i]
    if tmp>0:
      s=i
      while tmp>0:
        i+=1
        tmp+=ans[i]
      print(str(s//12).zfill(2),str(s%12*5).zfill(2),'-',str(i//12).zfill(2),str(i%12*5).zfill(2),sep='')
    i+=1