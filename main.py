from tkinter import *
from tkinter import  filedialog,Text,scrolledtext,colorchooser
from os import path

fileBeingEdited = ""
filename = "Untitled"
text_color = "#000000"
edditor_color = "#ffffff"
cursor_color = "#000000"
warnings = "None"

def openFile():
    global master
    global filename
    global warnings
    global fileBeingEdited
    fileName = filedialog.askopenfilename(title="Open a File...",filetypes=([("Text files(.txt)", "*.txt",)]))
    
    if fileName == "":
        warnings = "No file opened."
    else:
        fileBeingEdited = fileName
        f = open(fileName,'r')
        text.delete(1.0,"end")
        text.insert(1.0, f.read())
        warnings = "File succesfully opened!"
        master.title("Text Editor - " + path.basename(fileName))
        f.close()


def saveFile():
    global warnings
    global fileBeingEdited
    if fileBeingEdited == "":
        warnings = "Unable to save,no file opened."
    else:
        f = open(fileBeingEdited,'w')
        f.write(text.get("1.0", "end-1c"))
        f.close()
        warnings = "File successfully saved!"


def saveAs():
    global warnings
    global fileBeingEdited

    f = filedialog.asksaveasfile(title="Save As...",mode="w",defaultextension=".txt",filetypes=([("Text files(.txt)", "*.txt",)]))
    if f != None:
        f.write(text.get("1.0", "end-1c"))
        f.close
        warnings = "File saved."
        master.title("Text Editor - " + path.basename(f.name))

    else:
        warnings = "No file selected."

def exit(window_close):
    window_close.destroy()

def accept_font_prefs(choice_font,choice_size,text):
    #print(str(choice_font.get(ACTIVE)) + str(choice_size.get(ACTIVE)))
    text.configure(font=(choice_font.get(ACTIVE), choice_size.get(ACTIVE), "bold"))

def edditor_prefs():
    pref_win = Tk()
    pref_win.resizable(False, False)
    pref_win.title("Preferences")
    pref_win.iconbitmap('C:\\Users\\Alexandros\\Desktop\\Alex Python Related\\textEdditor\\window_icon.ico')

    fonts = ["Roboto","Arial", "Calibri","Impact","Verdana"]
    font_size = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,22,23,24,25,26,27,28,29,30]
    options = Frame(pref_win)
    options.grid(row=0,column=0,pady=(10,0),padx=10)

    l1 = LabelFrame(options,text="Fonts")
    l1.grid(row=0,column=0,padx=10,pady=10)

    l2 = LabelFrame(options,text="Font Size")
    l2.grid(row=0,column=1,padx=10,pady=10)

    #======================================================
    scrollbar1 = Scrollbar(l1) 
    scrollbar1.pack(side = RIGHT, fill = BOTH)

    fonts_list = Listbox(l1)
    for entry in fonts:
        fonts_list.insert(END, entry)

    fonts_list.pack(side = LEFT, fill = BOTH,padx=(10,0),pady=10)

    fonts_list.config(yscrollcommand = scrollbar1.set) 
    scrollbar1.config(command = fonts_list.yview) 
    #======================================================
    scrollbar2 = Scrollbar(l2)
    scrollbar2.pack(side = RIGHT, fill = BOTH)

    font_size_list = Listbox(l2)
    
    for entry in font_size:
        font_size_list.insert(END, entry)

    font_size_list.pack(side = LEFT, fill = BOTH,padx=(10,0),pady=10)

    font_size_list.config(yscrollcommand = scrollbar2.set) 
    scrollbar2.config(command = font_size_list.yview) 
    #======================================================

    buttons = Frame(pref_win)
    save = Button(buttons,text="Save",command=lambda: accept_font_prefs(fonts_list,font_size_list,text))
    cancel = Button(buttons,text="Close",command=lambda:exit(pref_win))

    save.grid(row=0,column=0)
    cancel.grid(row=0,column=1)
    buttons.grid(row=1,column=0,sticky="e",padx=(0,20),pady=(0,10))

    pref_win.mainloop()

def change_text_color(widget_to_destroy):
    global text_color
    color = colorchooser.askcolor()[1]
    text.configure(foreground=color)
    text_color = color
    widget_to_destroy.destroy()

def change_edditor_color(widget_to_destroy):
    global edditor_color
    color = colorchooser.askcolor()[1]
    text.configure(background=color)
    edditor_color = color
    widget_to_destroy.destroy()

def change_cursor_color(widget_to_destroy):
    global cursor_color
    color = colorchooser.askcolor()[1]
    text.configure(insertbackground=color)
    cursor_color = color
    widget_to_destroy.destroy()

def color_prefs():
    global text_color,edditor_color,cursor_color
    master_color = Tk()
    master_color.title("Edditor Colros")
    master_color.resizable(False,False)

    main_frame = Frame(master_color)
    main_frame.grid(row=0,column=0,padx=5,pady=5)

    text_color_frame = LabelFrame(main_frame,text="Text")
    text_color_frame.grid(row=0,column=0,padx=5,pady=5)

    edditor_color_frame = LabelFrame(main_frame,text="Edditor")
    edditor_color_frame.grid(row=1,column=0,padx=5,pady=5)

    cursor_color_frame = LabelFrame(main_frame,text="Cursor")
    cursor_color_frame.grid(row=2,column=0,padx=5,pady=5)

    #---------------------------------------------------------------------------

    text_color_label = Label(text_color_frame,text="Current text color:      ")
    text_color_label.grid(row=0,column=0,padx=5,pady=5)

    text_color_box = Label(text_color_frame,text="      ",bg=text_color)
    text_color_box.grid(row=0,column=1,padx=5,pady=5)

    text_color_pick = Button(text_color_frame,text="Set...",command=lambda: change_text_color(master_color))
    text_color_pick.grid(row=0,column=2,padx=5,pady=5)

    #---------------------------------------------------------------------------

    edditor_color_label = Label(edditor_color_frame,text="Current edditor color: ")
    edditor_color_label.grid(row=1,column=0,padx=5,pady=5)

    edditor_color_box = Label(edditor_color_frame,text="      ",bg=edditor_color)
    edditor_color_box.grid(row=1,column=1,padx=5,pady=5)

    edditor_color_pick = Button(edditor_color_frame,text="Set...",command=lambda: change_edditor_color(master_color))
    edditor_color_pick.grid(row=1,column=2,padx=5,pady=5)

    #---------------------------------------------------------------------------

    cursor_color_label = Label(cursor_color_frame,text="Current cursor color:     ")
    cursor_color_label.grid(row=2,column=0)

    cursor_color_box = Label(cursor_color_frame,text="      ",bg=cursor_color)
    cursor_color_box.grid(row=2,column=1,padx=5,pady=5)

    cursor_color_pick = Button(cursor_color_frame,text="Set...",command=lambda: change_cursor_color(master_color))
    cursor_color_pick.grid(row=2,column=2,padx=5,pady=5)

    master_color.mainloop()

def refresh_bot_info():
    global warnings
    temp = text.index(INSERT).split(".",1)
    lineInfo.configure(text="Lines: " + temp[0] + "   Column: " + str(int(temp[1])+1) + "   Warnings:  " + warnings)
    text.after(1,refresh_bot_info)




master = Tk()
master.geometry("1000x600")
master.title("Text Editor - " + filename)
master.iconbitmap('C:\\Users\\Alexandros\\Desktop\\Alex Python Related\\textEdditor\\window_icon.ico')
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)



#menus
menu =  Menu(master)

file_menu = Menu(menu, tearoff=False)
file_menu.add_command(label="Open File",command=openFile)
file_menu.add_command(label="Save File",command=saveFile)
file_menu.add_command(label="Save As...",command=saveAs)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=lambda: exit(master))
menu.add_cascade(label="File", menu=file_menu)

pref_menu = Menu(menu,tearoff=False)
pref_menu.add_command(label="Fonts",command=edditor_prefs)
pref_menu.add_command(label="Colors",command=color_prefs)
menu.add_cascade(label="Preferences", menu=pref_menu)

master.config(menu=menu)

#text
text = Text(master,wrap="none")
text.grid(row=0,column=0,sticky="nsew")
text.configure(padx=10,pady=10,foreground=text_color,background=edditor_color,font=("Roboto",15,"bold"),insertbackground=cursor_color)


#scroll
scrollV = Scrollbar(master,command=text.yview)
scrollV.grid(row=0,column=1,sticky='nsew')
text['yscrollcommand'] = scrollV.set

scrollH =Scrollbar(master,orient="horizontal",command=text.xview)
scrollH.grid(row=1,column=0,sticky='nsew')
text['xscrollcommand'] = scrollH.set


#bottom frame
bottomInfos = Frame(master)
bottomInfos.grid(row=2,column=0,sticky="W")

lineInfo = Label(bottomInfos,text="Line:  Column: ",bg="#abc4ff")
lineInfo.grid(row=0,column=0)
text.after(1,refresh_bot_info)

master.mainloop()
