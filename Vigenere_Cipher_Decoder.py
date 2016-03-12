cyphe = "lemon"

text = raw_input("Text: ").lower()

cyph = ""
for i in range(len(text)):
    cyph += cyphe[i%len(cyphe)]
print cyph

out = ""
for i in range(len(text)):
    if (cyph[i] == "-"):
        out += text[i].upper()
    else:
        out += chr(((ord(text[i])-ord(cyph[i]))%26)+ord("a"))

print out
