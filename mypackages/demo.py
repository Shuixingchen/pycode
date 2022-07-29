import sys
import os
sys.path.append(os.path.dirname(__file__) + os.sep + '../') #把上一级目录放入sys.path中

import commons.fibo #导入commons/fibo模块
import cal  #导入同一个目录的文件

res = cal.add(1,3)
res = commons.fibo.fib(5)
print(__file__)