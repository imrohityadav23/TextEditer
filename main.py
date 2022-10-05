import tempfile

tkinter from r import *
from tkinter.ttk import *
from tkinter import font,colorchooser,filedialog,messagebox
import os

#functonality

def find():



    #function
    def replace_words():
        word= findentryField.get()
        replaceword=replaceentryField.get()
        content=textarea.get(1.0,END)
        new_content=content.replace(word,replaceword)
        textarea.delete(1.0,END)
        textarea.insert(1.0,new_content)




    def find_words():
        word=findentryField.get()
        start_position='1.0'   #line number 1 character 0
        while True:
             start_position=textarea.search(word,start_position,stopindex=END) #1.7
             if not start_position:
                 break
             end_position=f'{start_position}+{len(word)}c'  #1.7+4c
             textarea.tag_add('match',start_position,end_position)  #kuma
             textarea.tag_config('match',foreground='white',background='Green')
             start_position=end_position


    #GUI part
    root1=Toplevel()
    root1.title('Find')
    root1.geometry('450x250+500+200')
    root1.resizable(0,0)

    labelFrame=LabelFrame(root1,text='Find/Replace')
    labelFrame.pack(pady=50)

    findlabel=Label(labelFrame,text='Find')
    findlabel.grid(row=0,column=0,pady=5,padx=5)

    findentryField=Entry(labelFrame)
    findentryField.grid(row=0,column=1,pady=5,padx=5)

    replacelabel = Label(labelFrame, text='Replace')
    replacelabel.grid(row=1, column=0, pady=5, padx=5)

    replaceentryField = Entry(labelFrame)
    replaceentryField.grid(row=1, column=1, pady=5, padx=5)

    findButton=Button(labelFrame,text='FIND',command=find_words)
    findButton.grid(row=2,column=0,padx=10,pady=10)

    replaceButton = Button(labelFrame, text='REPLACE',command=replace_words)
    replaceButton.grid(row=2, column=1, padx=10,pady=10)

    root1.mainloop()


def statusBarFunction(event):
    if textarea.edit_modified():
        words=len(textarea.get(0.0,END).split())
        charecters=len(textarea.get(0.0,'end-1c').replace(' ',''))
        status_bar.config(text=f'charecters:{charecters} :words={words}')
    textarea.edit_modified(False)


url=''
def new_file():
    global url
    url=''
    textarea.delete(0.0,END)

def open_file():
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd,title='Select file',filetypes=(('Text File','text'),('All Files','*.*')))
    if url !='':
       data=open(url,'r')
       textarea.insert(0.0,data.read())
    root.title(os.path.basename(url))  # use titel url change after select file

def save_file():
    if url =='':
        save_url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','txt'),('All Files','*.*')))

        content=textarea.get(0.0,END)
        save_url.write(content)
        save_url.close()

    else:
        content=textarea.get(0.0,END)
        file=open(url,'w')
        file.write(content)

def saveas_file():
    save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                        filetypes=(('Text File', 'txt'), ('All Files', '*.*')))
    content = textarea.get(0.0, END)
    save_url.write(content)
    save_url.close()
    if url !="":
       os.remove(url)

def iexit():
    if textarea.edit_modified():
        result=messagebox.askyesnocancel('warning','Do you wan to save as file?')
        if result is True:
            if url !='':
                content=textarea.get(0.0,END)
                file=open(url,'w')
                file.write(content)
                root.destroy()
            else:
                content = textarea.get(0.0, END)
                save_url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                    filetypes=(('Text File', 'txt'), ('All Files', '*.*')))
                save_url.write(content)
                save_url.close()
                root.destroy()
        elif result is False:
            root.destroy()

        else:
            pass
    else:
        root.destroy() # file is not modified then exit used is line






fontsize=12
fontstyle='arial'
def font_style(event):
    global fontstyle
    fontstyle=font_familes_variable.get()
    textarea.config(font=(fontstyle,fontsize))

def font_size(event):
    global fontsize
    fontsize=size_variable.get()
    textarea.config(font=(fontstyle,fontsize))


def bold_text():
    text_property=font.Font(font=textarea['font']).actual()
    if text_property['weight']=='normal':
        textarea.config(font=(fontstyle,fontsize,'bold'))

    if text_property['weight']=='bold':
        textarea.config(font=(fontstyle,fontsize,'normal'))

def italic_text():
    text_property = font.Font(font=textarea['font']).actual()
    if text_property['slant']=='roman':
        textarea.config(font=(fontstyle,fontsize,'italic'))

    if text_property['slant']=='italic':
        textarea.config(font=(fontstyle,fontsize,'roman'))

def underline_text():
    text_property = font.Font(font=textarea['font']).actual()
    if text_property['underline']==0:
        textarea.config(font=(fontstyle,fontsize,'underline'))

    if text_property['underline']==1:
        textarea.config(font=(fontstyle,fontsize,'underline'))

def color_select():
    color=colorchooser.askcolor()
    textarea.config(fg=color[1])


def aline_right():
    data=textarea.get(0.0,END)
    textarea.tag_config('right',justify=RIGHT)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'right')

def aline_left():
    data=textarea.get(0.0,END)
    textarea.tag_config('left',justify=LEFT)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'left')

def aline_center():
    data=textarea.get(0.0,END)
    textarea.tag_config('center',justify=CENTER)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'center')




root=Tk()
root.title('Create by Rohit')
root.geometry('1200x620+10+10')
root.resizable(False,False)

#create menubar
menubar=Menu(root)
root.config(menu=menubar)

#create file menu section
filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='File',menu=filemenu)
newImage=PhotoImage(file='add.png')
saveImage=PhotoImage(file='save.png')
openImage=PhotoImage(file='open.png')
saveasImage=PhotoImage(file='saveas.png')
exitImage=PhotoImage(file='exitfile.png')
printImage=PhotoImage(file='print.png')
filemenu.add_command(label='New',accelerator='Ctrl+N',image=newImage,compound=LEFT,command=new_file)
filemenu.add_command(label='Open',accelerator='Ctrl+O',image=openImage,compound=LEFT,command=open_file)
filemenu.add_command(label='Save',accelerator='Ctrl+S',image=saveImage,compound=LEFT,command=save_file)
filemenu.add_command(label='Save As',accelerator='Ctrl+Alt+S',image=saveasImage,compound=LEFT,command=saveas_file)
filemenu.add_command(label='Print',accelerator='Ctrl+P',image=printImage,compound=LEFT)
filemenu.add_separator()
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',image=exitImage,compound=LEFT,command=iexit)


#create edit manu section
editmenu=Menu(menubar,tearoff=False)
cutImage=PhotoImage(file='cut.png')
copyImage=PhotoImage(file='copy.png')
clearImage=PhotoImage(file='clear (2).png')
pasteImage=PhotoImage(file='paste.png')
findImage=PhotoImage(file='find.png')
timetableImage=PhotoImage(file='timetable.png')
editmenu.add_command(label='Cut',accelerator='Ctrl+X',image=cutImage,compound=LEFT,command=lambda: textarea.event_generate('<Control x>'))
editmenu.add_command(label='Copy',accelerator='Ctrl+C',image=copyImage,compound=LEFT,command=lambda :textarea.event_generate('<Control c>'))
editmenu.add_command(label='Paste',accelerator='Ctrl+V',image=pasteImage,compound=LEFT,command=lambda : textarea.event_generate('<Control v>'))
editmenu.add_command(label='Clear',accelerator='Ctrl+Alt+X',image=clearImage,compound=LEFT,command=lambda:textarea.delete(1.0,END))
editmenu.add_command(label='Find',accelerator='Ctrl+F',image=findImage,compound=LEFT,command=find)
editmenu.add_command(label='Date',image=timetableImage,compound=LEFT)
menubar.add_cascade(label='Edit',menu=editmenu)

#create view menu section
show_toolbar=BooleanVar()
show_statusbar=BooleanVar()
statusbarImage=PhotoImage(file='status_bar.png')
toolbarImage=PhotoImage(file='tool_bar.png')
viewmenu=Menu(menubar,tearoff=False)
viewmenu.add_checkbutton(label='Tool Bar',variable='toolbar',onvalue=True,offvalue=False,image=statusbarImage,compound=LEFT)
viewmenu.add_checkbutton(label='Status Bar',variable='statusbar',onvalue=True,offvalue=False,image=toolbarImage,compound=LEFT)
menubar.add_cascade(label='View',menu=viewmenu)

#create themes menu section
themesmenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='Themes',menu=themesmenu)
theme_choice=StringVar()
lightImage=PhotoImage(file='light_plus.png')
nightImage=PhotoImage(file='night_blue.png')
monikaImage=PhotoImage(file='monokai.png')
darkImage=PhotoImage(file='dark.png')
themesmenu.add_radiobutton(label='Light default',image=lightImage,variable=theme_choice,compound=LEFT)
themesmenu.add_radiobutton(label='Night Blue',image=nightImage,variable=theme_choice,compound=LEFT)
themesmenu.add_radiobutton(label='Monika',image=monikaImage,variable=theme_choice,compound=LEFT)
themesmenu.add_radiobutton(label='Dark',image=darkImage,variable=theme_choice,compound=LEFT)

#toolbar section
tool_bar=Label(root)
tool_bar.pack(side=TOP,fill=X)
font_familes=font.families()
font_familes_variable=StringVar()
fontfamily_Combobox=Combobox(tool_bar,width=20,values=font_familes,state='readonly',textvariable=font_familes_variable)
fontfamily_Combobox.current(font_familes.index('Arial'))
fontfamily_Combobox.grid(row=0,column=0,padx=4)

#text size section
size_variable=IntVar()
font_size_Combobox=Combobox(tool_bar,width=12,textvariable=size_variable,state='readonly',values=tuple(range(8,81)))
font_size_Combobox.current(4)
font_size_Combobox.grid(row=0,column=1,padx=4)

fontfamily_Combobox.bind('<<ComboboxSelected>>',font_style)
font_size_Combobox.bind('<<ComboboxSelected>>',font_size)

#button section
#create bold button
boldImage=PhotoImage(file='bold-button.png')
boldButton=Button(tool_bar,image=boldImage,compound=LEFT,width=1,command=bold_text)
boldButton.grid(row=0,column=2,padx=4)

italicImage=PhotoImage(file='italics.png')
italicButton=Button(tool_bar,image=italicImage,compound=LEFT,width=1,command=italic_text)
italicButton.grid(row=0,column=3,padx=4)

underlineImage=PhotoImage(file='underline.png')
underlineButton=Button(tool_bar,image=underlineImage,compound=LEFT,width=1,command=underline_text)
underlineButton.grid(row=0,column=4,padx=4)

fontcolorImage=PhotoImage(file='font_color.png')
fontcolorButton=Button(tool_bar,image=fontcolorImage,compound=LEFT,width=1,command=color_select)
fontcolorButton.grid(row=0,column=5,padx=4)

leftAlineImage=PhotoImage(file='left.png')
leftAlineButton=Button(tool_bar,image=leftAlineImage,compound=LEFT,width=1,command=aline_left)
leftAlineButton.grid(row=0,column=6,padx=4)

centerAlineImage=PhotoImage(file='center.png')
CenterAlineButton=Button(tool_bar,image=centerAlineImage,compound=LEFT,width=1,command=aline_center)
CenterAlineButton.grid(row=0,column=7,padx=4)

rightAlineImage=PhotoImage(file='right.png')
rightAlineButton=Button(tool_bar,image=rightAlineImage,compound=LEFT,width=1,command=aline_right)
rightAlineButton.grid(row=0,column=8,padx=4)

#textarea create section
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(root,yscrollcommand=scrollbar.set,font=('arial',12),undo=True)
textarea.pack(fill=BOTH,expand=True)
scrollbar.config(command=textarea.yview)

status_bar=Label(root,text='Status Bar')
status_bar.pack(side=BOTTOM)

textarea.bind('<<Modified>>',statusBarFunction)




root.mainloop()


