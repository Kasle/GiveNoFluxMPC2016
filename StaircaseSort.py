N = int(raw_input())

matLine = []
for i in range(N):
    line = raw_input()
    line = line.replace("\r", "").split(",")
    for n in line:
        matLine.append(int(n))


MAT = []
for e in range(N):
    MAT.append(sorted(matLine)[e*N:(e*N)+N])

flip = False
for out in MAT:
    if (flip):
        print ",".join(map(str, out[::-1]))
        flip = False
    else:
        print ",".join(map(str, out))
        flip = True