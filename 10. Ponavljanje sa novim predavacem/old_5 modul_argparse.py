import argparse

parser = argparse.ArgumentParser(description='Input file name')
parser.add_argument('--integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
parser.add_argument('--input_file', type = str,help='Name of the file to open',required=True)

args = parser.parse_args()
print(args)

print(args.input_file)
print(args.integers)
izlaz = open("palindromi.txt","w")
with open("datoteka.txt","r") as f:
    reci = f.read().split()
    for rec in reci:
        if rec == rec[::-1]:
            izlaz.write(rec + " ")
    
    izlaz.write (" ".join([rec for rec in f.read().split() if rec == rec[::-1])])

