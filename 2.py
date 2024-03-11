import argparse 

parser = argparse.ArgumentParser(description="Принимает строку с окладом и премией")
parser.add_argument('-bs', type=int, default=100)
parser.add_argument('-bs', type=int, default=10)

args = parser.parse_args()
print(args)

def func(base, bonus):
    return base + base * bonus / 100

print(func(1000, 10)) 
print(func(args.bs, args.bn))


