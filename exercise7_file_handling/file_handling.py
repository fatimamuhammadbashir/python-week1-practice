with open("notes.txt", "w") as file:
    file.write("Assalamu alaikum")

with open("notes.txt", "r") as file:
    content = file.read()

print(content)
