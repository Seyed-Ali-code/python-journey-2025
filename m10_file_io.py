notes = []
while True:
        line = input("> ")
        if line == 'done':
                break
        notes.append(line)

with open('notes.txt','w') as f:
        for note in notes:
                f.write(note + "\n")

with open('notes.txt','r') as f:
        print("\n Your notes:")
        print(f.read())