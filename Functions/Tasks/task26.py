folders = {
    "Documents": {
        "Projects": {
            "Python": {},
            "Java": {}
        },
        "Resume.pdf": None
    }
}


def explore(folder, spaces=0):
    for name, content in folder.items():

        print("    " * spaces + name)

        if isinstance(content, dict):
            explore(content, spaces + 1)


explore(folders)