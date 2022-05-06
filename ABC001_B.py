import io
import sys

_INPUT = """\
6
15000
75000
200
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  m=int(input())
  if m<100: print('00')
  elif m<=5000: print(str(m//100).zfill(2))
  elif m<=30000: print(m//1000+50)
  elif m<=70000: print((m//1000-30)//5+80)
  else: print(89)