import argparse

parser = argparse.ArgumentParser()
parser.add_argument('f1')
args = parser.parse_args()

nums = []
try:
	with open(args.f1) as f:
		for line in f:
			nums.append(int(line.split()[0]))
except Exception:
	print('Something wrong with file')
	exit(1)

median = sorted(nums)[len(nums) // 2]

sum = 0
for n in nums:
    sum += abs(n - median)

print(sum)
