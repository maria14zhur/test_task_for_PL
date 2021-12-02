import argparse

parser = argparse.ArgumentParser()
parser.add_argument("length", type=int)
parser.add_argument("span", type=int)
args = parser.parse_args()


if args.length <= 0 or args.span <= 0:
    raise Exception('Incorrect data(length or span <= 0)')

length = args.length
span = args.span
array = [i+1 for i in range(length)]


def returnNumber():
    index = -1
    while True:
        index += 1
        yield array[index % len(array)]


path = [1]
numberGenerator = returnNumber()
next(numberGenerator)


if length == 1 or span == 1:
    print(1)
else:
    a = 0
    while a != 1:
        for _ in range(span-1):
            a = next(numberGenerator)
        if a != 1:
            path.append(a)

    answer = ''.join(str(i) for i in path)
    print(answer)
