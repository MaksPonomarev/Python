"выписать подряд значения на четных позициях, затем значения на неченых позициях"

msg = input()
halfLength = round(len(msg)/2)
evenLetters = msg[:halfLength]
oddLetters = msg[halfLength:]

for i in range(0, len(msg)):
    if (int(i + 1) % 2) == 0:
        print(evenLetters[0], end='')
        evenLetters = evenLetters[1:]
    else:
        print(oddLetters[0], end='')
        oddLetters = oddLetters[1:]
