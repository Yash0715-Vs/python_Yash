with open("notes.txt", "w") as f:
    f.write("Python makes file handling easy.\n")
    f.write("This is line two.")

    with open("notes.txt", "r") as f:
        line= f.read()
        print(line)