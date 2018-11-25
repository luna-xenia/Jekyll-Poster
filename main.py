from tkinter import *

root = Tk()


def makePost(x, y, z):
    global file

    print("Making file...")
    file = open(x + ".md", "a")
    print("Made file.")

    print("Adding front...")
    file.write("---\nlayout: post\ntitle: " + y + "\n---\n\n")
    print("Added front.")

    print("Adding content...")
    file.write(z)


def retrieve_input():
    global x
    global y
    global z

    # date
    xTemp = textBox.get("1.0", "end-1c")
    # title
    y = textBox2.get("1.0", "end-1c")
    # content
    z = textBox3.get("1.0", "end-1c")
    # file name
    x = xTemp + "-" + y

    makePost(x, y, z)


T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Enter the date\nYYYY-MM-DD\n")

textBox = Text(root, height=1, width=40)
textBox.pack()

X = Text(root, height=1, width=30)
X.pack()
X.insert(END, "Enter the title")

textBox2 = Text(root, height=1, width=40)
textBox2.pack()

Y = Text(root, height=1, width=30)
Y.pack()
Y.insert(END, "Enter the content")

textBox3 = Text(root, height=40, width=120)
textBox3.pack()

buttonMake = Button(root, height=1, width=10, text="Finish",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonMake.pack()

mainloop()
