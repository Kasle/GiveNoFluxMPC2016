start = raw_input()
seperated = list(start)
output = 0
while len(seperated)>1:
    for i in seperated:
        output+=int(i);
    seperated = list(str(output))
    output = 0
print seperated[0]