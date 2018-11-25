def addContent(z):
    print("Adding content...")
    file.write(z)


def makeFile(y, x):
    global file
    print("Making file...")
    file = open(x + ".md", "a")
    print("Made file.")
    print("Adding front...")
    file.write("---\nlayout: post\ntitle: " + y + "\n---\n\n")
    print("Added front.")


def start():
    global x
    global y
    global z
    y = input("What should the title be? ")
    xTemp = input("What is the date? (YYYY-MM-DD)")
    x = xTemp + "-" + y
    makeFile(y, x)
    z = input("Write the post contents with a [backslash]n for a newline.")
    addContent(z)


print("Welcome to the Poster. It is assumed this python file is in _posts.")
input("Press <--/ to start")
start()
