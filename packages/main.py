import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo") # 第一个参数
args = parser.parse_args()
print(args.echo)