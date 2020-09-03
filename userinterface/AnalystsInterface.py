# import the library
from appJar import gui
from util import CreateExcel


# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Sprint")
        if is_int(usr):
            CreateExcel.CreateExcel(usr)
        else:
            pass


# Verify if a string is an entire number
def is_int(int_string):
    try:
        int(int_string)
        return True
    except ValueError:
        return False


# create a GUI variable called app
app = gui("Ventana principal", "400x200")
app.setBg("white")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Azure audit")
app.setLabelBg("title", "white")
app.addLabelEntry("Sprint")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Sprint")

# start the GUI
app.go()
