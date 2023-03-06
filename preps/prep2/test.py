
force = 1
position = 6
slots = 8
if force + position >= slots:
    position = (force + position) % slots
else:
    position += force

print(position)