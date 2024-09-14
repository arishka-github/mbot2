
with open("sounds.lst", "r") as file:
    sounds = [l.split('.')[1].strip() for l in file]

print(sounds)

with open("sounds_list.txt", "w") as out:
    out.write(str(sounds))

with open('sounds_one_column.txt', 'w') as out:
    for s in sounds:
        out.write(s + '\n')