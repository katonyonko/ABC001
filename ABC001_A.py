import io
import sys

_INPUT = """\
6
15
10
0
0
5
20
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H1=int(input())
  H2=int(input())
  print(H1-H2)