import sys
sys.path.append("../../")
from appJar import gui

app=gui()
app.addLabel("f1", "Choose a file:", row=0, column=0)
app.addFileEntry("file", row=0, column=1)
app.getEntryWidget("file").config(font="Times 20 italic underline")
app.go()
