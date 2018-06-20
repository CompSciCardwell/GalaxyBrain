s = "The Quick Brown Fox Jumps Over The Lazy Dog."

newS = ""

for char in s:
    capital = range(65, 90)
    lower = range(97, 122)
    c = ord(char)
    if (c not in capital) and (c not in lower):
        newS = newS + chr(c)
    elif (c in capital and c < 78) or (c in lower and c < 110):
        newS = newS + chr(c + 13)
    elif (c in capital and c >= 78) or (c in lower and c >= 110):
        newS = newS + chr(c - 13)

print newS