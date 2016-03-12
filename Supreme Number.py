start = raw_input()
seperated = list(start)
output = 0
while len(seperated)>1:
    print seperated
    for i in seperated:
        output+=int(i);
    seperated = list(str(output))
print seperated[0]