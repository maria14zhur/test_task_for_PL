import argparse

parser = argparse.ArgumentParser()

parser.add_argument('f1')
parser.add_argument('f2')
args = parser.parse_args()

try:
    with open(args.f1) as f:
        l = [line.split() for line in f]
        try:
            xc = float(l[0][0])
            yc = float(l[0][1])
            r = float(l[1][0])
        except Exception:
            print('Wrong format of file 1')
            exit(1)
except Exception:
    print('Cant open file 1')
    exit(1)
	
	
try:
	with open(args.f2) as f:
		for line in f:
			try:
				x = float(line.split()[0])
				y = float(line.split()[1])
			except Exception:
				print('Wrong format of file 2')
				exit(1)
			if ((x-xc)*(x-xc)+(y-yc)*(y-yc)) < r*r:
				ans = 1
			elif ((x-xc)*(x-xc)+(y-yc)*(y-yc)) > r*r:
				ans = 2
			else:
				ans = 0
			print(ans)
except Exception:
    print('Cant open file 2')
    exit(1)
