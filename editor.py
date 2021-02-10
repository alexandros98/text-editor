from tkinter import *
from tkinter import  filedialog,Text,scrolledtext,colorchooser
from os import path
from sys import platform

class Editor:

    def __init__(self):
        self.fileBeingEdited = ""
        self.filename = "Untitled"
        self.text_color = "#000000"
        self.edditor_color = "#ffffff"
        self.cursor_color = "#000000"
        self.warnings = "None"
        self.master = Tk()
        self.menu =  Menu(self.master)
        self.text = Text(self.master,wrap="none")
        self.scrollV = Scrollbar(self.master,command=self.text.yview)
        self.scrollH =Scrollbar(self.master,orient="horizontal",command=self.text.xview)
        self.bottomInfos = Frame(self.master)
        self.lineInfo = Label(self.bottomInfos,text="Line:  Column: ",bg="#abc4ff")

        self.master.geometry("1000x600")
        self.master.title("Text Editor - " + self.filename)
        if platform == "linux" or platform == "linux2":
            self.master.iconbitmap('@window_icon.xbm')
        elif platform == "win32":
            self.master.iconbitmap('window_icon.ico')
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        #menus
        file_menu = Menu(self.menu, tearoff=False)
        file_menu.add_command(label="Open File",command=self.openFile)
        file_menu.add_command(label="Save File",command=self.saveFile)
        file_menu.add_command(label="Save As...",command=self.saveAs)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=lambda: exit(self.master))
        self.menu.add_cascade(label="File", menu=file_menu)

        pref_menu = Menu(self.menu,tearoff=False)
        pref_menu.add_command(label="Fonts",command=self.edditor_prefs)
        pref_menu.add_command(label="Colors",command=self.color_prefs)
        self.menu.add_cascade(label="Preferences", menu=pref_menu)

        self.master.config(menu=self.menu)

        #text
        self.text.grid(row=0,column=0,sticky="nsew")
        self.text.configure(padx=10,pady=10,foreground=self.text_color,background=self.edditor_color,font=("Roboto",15,"bold"),insertbackground=self.cursor_color)

        #scroll
        self.scrollV.grid(row=0,column=1,sticky='nsew')
        self.text['yscrollcommand'] = self.scrollV.set

        self.scrollH.grid(row=1,column=0,sticky='nsew')
        self.text['xscrollcommand'] = self.scrollH.set

        #bottom frame
        self.bottomInfos.grid(row=2,column=0,sticky="W")

        self.lineInfo.grid(row=0,column=0)
        self.text.after(1,self.refresh_bot_info)

    def run(self):
        self.master.mainloop()
        
    def edditor_prefs(self):
        pref_win = Tk()
        pref_win.resizable(False, False)
        pref_win.title("Preferences")
        pref_win.iconbitmap('window_icon.ico')

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
        save = Button(buttons,text="Save",command=lambda: self.accept_font_prefs(fonts_list,font_size_list))
        cancel = Button(buttons,text="Close",command=lambda:self.exit(pref_win))

        save.grid(row=0,column=0)
        cancel.grid(row=0,column=1)
        buttons.grid(row=1,column=0,sticky="e",padx=(0,20),pady=(0,10))

        pref_win.mainloop()

    def accept_font_prefs(self,choice_font,choice_size):
        self.text.configure(font=(choice_font.get(ACTIVE), choice_size.get(ACTIVE), "bold"))

    def openFile(self):
        fileName = filedialog.askopenfilename(title="Open a File...",filetypes=([("Text files(.txt)", "*.txt",)]))
        if fileName == "":
            self.warnings = "No file opened."
        else:
            self.fileBeingEdited = fileName
            f = open(fileName,'r')
            self.text.delete(1.0,"end")
            self.text.insert(1.0, f.read())
            self.warnings = "File succesfully opened!"
            self.master.title("Text Editor - " + path.basename(fileName))
            f.close()

    def saveFile(self):
        if self.fileBeingEdited == "":
            self.warnings = "Unable to save,no file opened."
        else:
            f = open(self.fileBeingEdited,'w')
            f.write(self.text.get("1.0", "end-1c"))
            f.close()
            self.warnings = "File successfully saved!"

    def saveAs(self):
        f = filedialog.asksaveasfile(title="Save As...",mode="w",defaultextension=".txt",filetypes=([("Text files(.txt)", "*.txt",)]))
        if f != None:
            f.write(self.text.get("1.0", "end-1c"))
            f.close
            self.warnings = "File saved."
            self.master.title("Text Editor - " + path.basename(f.name))

        else:
            self.warnings = "No file selected."

    def color_prefs(self):
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

        text_color_box = Label(text_color_frame,text="      ",bg=self.text_color)
        text_color_box.grid(row=0,column=1,padx=5,pady=5)

        text_color_pick = Button(text_color_frame,text="Set...",command=lambda: self.change_text_color(master_color))
        text_color_pick.grid(row=0,column=2,padx=5,pady=5)

        #---------------------------------------------------------------------------

        edditor_color_label = Label(edditor_color_frame,text="Current edditor color: ")
        edditor_color_label.grid(row=1,column=0,padx=5,pady=5)

        edditor_color_box = Label(edditor_color_frame,text="      ",bg=self.edditor_color)
        edditor_color_box.grid(row=1,column=1,padx=5,pady=5)

        edditor_color_pick = Button(edditor_color_frame,text="Set...",command=lambda: self.change_edditor_color(master_color))
        edditor_color_pick.grid(row=1,column=2,padx=5,pady=5)

        #---------------------------------------------------------------------------

        cursor_color_label = Label(cursor_color_frame,text="Current cursor color:     ")
        cursor_color_label.grid(row=2,column=0)

        cursor_color_box = Label(cursor_color_frame,text="      ",bg=self.cursor_color)
        cursor_color_box.grid(row=2,column=1,padx=5,pady=5)

        cursor_color_pick = Button(cursor_color_frame,text="Set...",command=lambda: self.change_cursor_color(master_color))
        cursor_color_pick.grid(row=2,column=2,padx=5,pady=5)

        master_color.mainloop()

    def change_edditor_color(self,widget_to_destroy):
        color = colorchooser.askcolor()[1]
        self.text.configure(background=color)
        self.edditor_color = color
        widget_to_destroy.destroy()

    def change_cursor_color(self,widget_to_destroy):
        color = colorchooser.askcolor()[1]
        self.text.configure(insertbackground=color)
        self.cursor_color = color
        widget_to_destroy.destroy()

    def change_text_color(self,widget_to_destroy):
        color = colorchooser.askcolor()[1]
        self.text.configure(foreground=color)
        self.text_color = color
        widget_to_destroy.destroy()

    def refresh_bot_info(self):
        temp = self.text.index(INSERT).split(".",1)
        self.lineInfo.configure(text="Lines: " + temp[0] + "   Column: " + str(int(temp[1])+1) + "   Warnings:  " + self.warnings)
        self.text.after(1,self.refresh_bot_info)

    def exit(self,window_close):
        window_close.destroy()