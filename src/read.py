data = open("data/line.txt", "rb")

byte = data.read(1)
while byte:
    print(f'{byte}  {byte[0]}  {byte[0]:b}')
    byte = data.read(1)

data.close()
