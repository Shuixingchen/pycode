import sys
import utils.match

def main():
    res = utils.match.Min(3,6)
    print(res)

def str():
    name = "C语言中文网"    
    age = 8
    course = 30
    s = "{} 已经 {} 岁了，共发布了{}套教程"
    ns = s.format(name,age,course)
    print(ns)
    
str()
