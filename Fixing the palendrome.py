while True:
inp = raw_input()
fin=list(inp)
out = 0
changed = False
for i in range(len(fin)):
    if (fin[i]!= fin[-(i+1)]):
        oldfin = fin
        fin = fin[0:i]+fin[i+1:]
        charcheck=True
        for b in range(len(fin)):
            if (fin[b]!= fin[-(b+1)]):
                charcheck = False
                break
        if charcheck:
            print i
            changed = True
        else:
            print len(oldfin)-(i+1)
            changed = True
        break
if not changed:
    print "-1"