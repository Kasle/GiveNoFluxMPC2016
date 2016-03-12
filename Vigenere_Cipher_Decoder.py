
cyphe = raw_input().strip()
text = raw_input().strip()

cyph = ""
q=0
for i in range(len(text)):
    if (text[i] == " "):
        cyph += " "
        q+=1
    else:
        cyph += cyphe[(i-q) % len(cyphe)]

out = ""
for i in range(len(text)):
    if (text[i] == " "):
        out += text[i].upper()
    else:
        out += chr(((ord(text[i])-ord(cyph[i]))%26)+ord("a")).upper()

print out
