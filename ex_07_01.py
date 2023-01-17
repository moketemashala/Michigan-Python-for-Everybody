fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    fh_upper = line.strip().upper()
    print(fh_upper)
    