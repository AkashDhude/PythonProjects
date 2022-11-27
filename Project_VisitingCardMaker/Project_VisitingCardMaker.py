
from tkinter import *

root = Tk()
root.title("VISITING CARD MAKER")
root.geometry("450x400")


l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = l9 = None
def addLabel(parent):
    global l1, l2, l3, l4, l5, l6, l7, l8, l9

    l0 = ttk.Label(parent, width=25)
    l0.grid(row=0, column=1)
    l1 = ttk.Label(parent, text="Name :")
    l1.grid(row=1, column=1, sticky=E, padx=5, pady=3)
    l2 = ttk.Label(parent, text="Position :")
    l2.grid(row=2, column=1, sticky=E, padx=5, pady=3)
    l3 = ttk.Label(parent, text="Email :")
    l3.grid(row=3, column=1, sticky=E, padx=5, pady=3)
    l4 = ttk.Label(parent, text="Mobile No.:")
    l4.grid(row=4, column=1, sticky=E, padx=5, pady=3)
    l5 = ttk.Label(parent, text="Company Name :")
    l5.grid(row=5, column=1, sticky=E, padx=5, pady=3)
    l6 = ttk.Label(parent, text="Website :")
    l6.grid(row=6, column=1, sticky=E, padx=5, pady=3)
    l7 = ttk.Label(parent, text="Address :")
    l7.grid(row=7, column=1, sticky=E, padx=5, pady=3)
    l8 = ttk.Label(parent, text="Font Name :")
    l8.grid(row=8, column=1, sticky=E, padx=5, pady=3)
    l9 = ttk.Label(parent, text="Upload Logo :")
    l9.grid(row=9, column=1, sticky=E, padx=5, pady=3)


e1 = e2 = e3 = e4 = e5 = e6 = e7  = None
def addEntry(parent):
    global e1, e2, e3, e4, e5, e6, e7

    e1 = ttk.Entry(parent, width=30)
    e1.grid(row=1, column=2, sticky="w", padx=2, pady=3)
    e2 = ttk.Entry(parent, width=30)
    e2.grid(row=2, column=2, sticky="w", padx=2, pady=3)
    e3 = ttk.Entry(parent, width=30)
    e3.grid(row=3, column=2, sticky="w", padx=2, pady=3)
    e4 = ttk.Entry(parent, width=30)
    e4.grid(row=4, column=2, sticky="w", padx=2, pady=3)
    e5 = ttk.Entry(parent, width=30)
    e5.grid(row=5, column=2, sticky="w", padx=2, pady=3)
    e6 = ttk.Entry(parent, width=30)
    e6.grid(row=6, column=2, sticky="w", padx=2, pady=3)
    e7 = ttk.Entry(parent, width=30)
    e7.grid(row=7, column=2, sticky="w", padx=2, pady=3)


menu = None
def addOptionMenu(parent):
    global menu
    font_list = [None, "Ebrimo", "Calibri", "Arial", "Times New Roman"]
    menu = StringVar()
    menu.set("Select Font Style")
    drop = ttk.OptionMenu(parent, menu, *(font_list))
    drop.grid(row=8, column=2, padx=2, pady=5)


def getFont():
    selection = menu.get()
    return str(selection)


from tkinter import ttk
def addTheme(parent):
    style = ttk.Style()
    theme = style.theme_use(themename="clam")
    return theme


f1 = None
def addFrame(parent):
    global f1
    f1 = ttk.Frame(parent)
    f1.pack(expand=True, fill=BOTH)


from tkinter import filedialog
upload_path = None
def addUploadPath():
    global upload_path
    upload_path = filedialog.askopenfilename(initialdir="C:/", filetypes=(("JPG files", "*.jpg"), ("PNG Files", "*.png"), ("All Files", "*.*")))


def addButton(parent):
    b3 = ttk.Button(parent, text="Browse File ...", command=lambda: addUploadPath())
    b3.grid(row=9, column=2, padx=5, pady=5)
    b1 = ttk.Button(parent, text="Download File", command=addInfo, width=20)
    b1.grid(row=11, column=2, padx=5, pady=3)
    b2 = ttk.Button(parent, text="Close", command=root.destroy, width=20)
    b2.grid(row=12, column=2, padx=5, pady=3)


def addDownloadPath():
    download_path = filedialog.asksaveasfilename(initialdir="Downloads", filetypes=(("PPT", "*.pptx"), ("All Files", "*.*")))
    return download_path


from VisitingCardTemplate import addPPT
def addInfo():
    name = e1.get()
    position = e2.get()
    email_e = e3.get()
    mob_num = e4.get()
    com_name = e5.get()
    website = e6.get()
    address = e7.get()
    font = getFont()
    addPPT(name=name, position_of_employee=position, email=email_e, mobile_num=mob_num, company_name=com_name, website=website, address=address, fontname=font, file_upload=upload_path, file_download=addDownloadPath())


frame_fromcreator = ttk.Frame(root)
lable = Label(frame_fromcreator, text="Welcome Folks...,\nI hope you are enjoying the journey.\n\nThanks!!!", bg="coral1", font="Arial,Bold, 15")
lable.pack(fill=BOTH, expand=True)

def fromCreator():
    hideAll()
    frame_fromcreator.pack(fill=BOTH, expand=True)


def hideAll():
    frame_fromcreator.pack_forget()
    f1.pack_forget()



def addMenuBar(parent):
    menubar = Menu(parent)
    filemenu = Menu(menubar)
    parent.config(menu=menubar)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Explore", command=lambda :exploreMenu())
    filemenu.add_command(label="From Creator", command=fromCreator)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=parent.quit)


def exploreMenu():
    hideAll()
    addTheme(root)
    addFrame(root)
    addLabel(f1)
    addEntry(f1)
    addOptionMenu(f1)
    addButton(f1)


def main():
    addTheme(root)
    addFrame(root)
    addMenuBar(root)
    addLabel(f1)
    addEntry(f1)
    addOptionMenu(f1)
    addButton(f1)

main()

root.mainloop()







