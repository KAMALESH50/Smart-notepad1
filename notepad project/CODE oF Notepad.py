import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter  import colorchooser
from tkinter  import filedialog
from tkinter  import messagebox
import os
from tkinter.ttk import Button
from typing import Any, List
import win32api
import json
import requests
import datetime
datetime.datetime.now()
from fpdf import FPDF
from socket import socket

# Importing necessary modules required
import speech_recognition as spr
from gtts import gTTS
import os
from numpy import character

# Initialize recognizer
r = spr.Recognizer()

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Notepad')
#main_application.wm_iconbitmap('C:\\Users\\kamal\\Desktop\\PROJECT\\27.5.23\\icons2')
#os.chdir("C:/Users/kamal/Desktop/PROJECT/27.5.23")
import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_directory)

# Rest of your code goes here

########## main menu #############
# Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False

main_menu = tk.Menu()
# File icons

new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_menu, tearoff=False)
####edit
# edit icons

copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)
##commands are added after edit menu


####view
# view icons

tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)

###color theme
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)
# all icons saved in a tuple
theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
## text  ,background
#
color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}

# cascade

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)
# ----------&&&&& End main menu &&&&&----------#

########## toolbar  #############

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

##font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

##size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8, 80, 2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

##bold button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

##italic button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

##underline button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

##font color button
font_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_icon)
font_color_btn.grid(row=0, column=5, padx=5)

## align_left
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

##align center
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

##align right
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

## record
record_icon = tk.PhotoImage(file='icons2/rec.png')
record_btn = ttk.Button(tool_bar, image=record_icon)
record_btn.grid(row=0, column=9, padx=5)

##print
print_icon = tk.PhotoImage(file='icons2/print.png')
print_btn = ttk.Button(tool_bar, image=print_icon)
print_btn.grid(row=0, column=10, padx=5)

# Create a new PDF button
pdf_icon = tk.PhotoImage(file="icons2/pdf.png")
pdf_btn = ttk.Button(tool_bar, image=pdf_icon)
pdf_btn.grid(row=0, column=11, padx=5)

# Create a new dictionary button
dictionary_icon = tk.PhotoImage(file='icons2/dictionary.png')
dictionary_btn = ttk.Button(tool_bar, image=dictionary_icon)
dictionary_btn.grid(row=0, column=12, padx=5)

# ----------&&&&& End toolbar &&&&&----------#


########## text editor  #############

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

##  font family and font size functionality

current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    current_font_family = font_family.get()

    # Clear existing font_change tags
    text_editor.tag_remove("font_change", 1.0, tk.END)

    try:
        sel_start = text_editor.index(tk.SEL_FIRST)
        sel_end = text_editor.index(tk.SEL_LAST)
        if sel_start and sel_end:
            tag_name = f"font_change_{sel_start}_{sel_end}"
            text_editor.tag_add(tag_name, sel_start, sel_end)
            text_editor.tag_configure(tag_name, font=(current_font_family, current_font_size))
    except tk.TclError:
        pass

def change_size(event=None):
    current_font_size = size_var.get()

    # Clear existing size_change tags
    text_editor.tag_remove("size_change", 1.0, tk.END)

    try:
        sel_start = text_editor.index(tk.SEL_FIRST)
        sel_end = text_editor.index(tk.SEL_LAST)
        if sel_start and sel_end:
            tag_name = f"size_change_{sel_start}_{sel_end}"
            text_editor.tag_add(tag_name, sel_start, sel_end)
            text_editor.tag_configure(tag_name, font=(current_font_family, current_font_size))
    except tk.TclError:
        pass

# Binding comboboxes with functions
font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)


####### buttons functionality
## REC Voice & Print' dialoguebox functionality
import tkinter as tk
from tkinter import ttk, Button, Entry, StringVar, Label, Toplevel
import speech_recognition as sr

speak = StringVar()
write = StringVar()
def rec(event=None):
    global status_label 
    
    def ready():
              
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print("Speak now...")
            audio = recognizer.listen(source)  # Listen to microphone input
            
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        try:
            print(f"Command is: {text}\n")
            print("You said: {}".format(text))
            speak.set(text)
            write.set("Listening")            
            ok_input.insert(0, text)
        except sr.UnknownValueError:

            print("Could not understand audio")
            speak.set("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {0}".format(e))
            speak.set("Speech recognition service error")
        except Exception as e:  # Catch any other unexpected errors
            print(f"An error occurred: {type(e).__name__} - {str(e)}")
    def ok():
        current_position = text_editor.index(tk.INSERT)
        text_editor.insert(current_position, ok_input.get()) 
        rec_dialogue.destroy()

    rec_dialogue = Toplevel()
    rec_dialogue.title('Your Voice to Text')
    rec_dialogue.geometry('450x250+500+200')
    rec_dialogue.resizable(0, 0)

    rec_frame = ttk.LabelFrame(rec_dialogue, text='Voice to Test & Print')
    rec_frame.pack(pady=30)

    text_rec_label = ttk.Label(rec_frame, text='Mic :')
    text_ok_label = ttk.Label(rec_frame, text='TEXT:')

    text_rec_label.grid(row=0, column=0, padx=4, pady=4)
    text_ok_label.grid(row=1, column=0, padx=4, pady=4)
 
    rec_input = ttk.Entry(rec_frame, textvariable=write, state='readonly')
    rec_input.grid(row=0, column=1, padx=4, pady=4)

    ok_input = ttk.Entry(rec_frame, textvariable=speak, state='readonly')
    ok_input.grid(row=1, column=1, padx=4, pady=4)
    
    ready_button = ttk.Button(rec_frame, text='Ready', command=ready)
    confirm_button = ttk.Button(rec_frame, text='OK', command=ok)

    ready_button.grid(row=2, column=0, padx=8, pady=4)
    confirm_button.grid(row=2, column=1, padx=8, pady=4)

    ready_button.configure(command=ready)
    confirm_button.configure(command=ok)
    rec_dialogue.mainloop()

record_btn.configure(command=rec)
# Initialize the recognizer
recognizer = sr.Recognizer()

# bold button functionality

# Bold button functionality
def change_bold():
    try:
        current_tags = text_editor.tag_names("sel.first")
        if "bold" in current_tags:
            text_editor.tag_remove("bold", "sel.first", "sel.last")
        else:
            text_editor.tag_configure("bold", font=("Helvetica", 12, "bold"))
            text_editor.tag_add("bold", "sel.first", "sel.last")
    except tk.TclError:
        pass

bold_btn.configure(command=change_bold)

# Italic button functionality
def italic():
    try:
        current_tags = text_editor.tag_names("sel.first")
        if "italic" in current_tags:
            text_editor.tag_remove("italic", "sel.first", "sel.last")
        else:
            text_editor.tag_configure("italic", font=("Helvetica", 12, "italic"))
            text_editor.tag_add("italic", "sel.first", "sel.last")
    except tk.TclError:
        pass

italic_btn.configure(command=italic)
# underline button functionality
def underline():
    try:
        current_tags = text_editor.tag_names("sel.first")
        if "underline" in current_tags:
            text_editor.tag_remove("underline", "sel.first", "sel.last")
        else:
            text_editor.tag_configure("underline", underline=True)
            text_editor.tag_add("underline", "sel.first", "sel.last")
    except tk.TclError:
        pass

underline_btn.configure(command=underline)


##font color functionality

def change_font_color():
    try:
        color_var = tk.colorchooser.askcolor()
        text_editor.tag_configure("colored", foreground=color_var[1])
        
        sel_start = text_editor.index(tk.SEL_FIRST)
        sel_end = text_editor.index(tk.SEL_LAST)
        
        if sel_start and sel_end:
            text_editor.tag_add("colored", sel_start, sel_end)
    except tk.TclError:
        pass
font_color_btn.configure(command=change_font_color)


### align functionality


def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


align_left_btn.configure(command=align_left)


###align center

def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


align_center_btn.configure(command=align_center)


##align right

def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


align_right_btn.configure(command=align_right)

text_editor.configure(font=('Arial', 12))
# ----------&&&&& End text editor  &&&&&----------#


#########    status bar #############


status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():  ###checks if any character is added or not
        text_changed = True
        words = len(
            text_editor.get(1.0, 'end-1c').split())  ##it even counts new line character so end-1c subtracts one char
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f' Words: {words} Characters : {characters}')
    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', changed)

# ----------&&&&& End main status bar &&&&&----------#


########## main menu functinality #############

##file commands


##variable
url = ''


##new functionality

def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


file.add_command(label='new', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)


##open functionality
## it is coppying the data from the desired file into the working file
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                     filetypes=(('Text File', '*.txt'), ("PDF Files", "*.pdf"), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))


file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)


##save functionality


def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(('Text File', '*.txt'),("PDF Files", "*.pdf"), ('All files', '*.*')))
            content = text_editor.get(1.0, tk.END)
            url.write(content)
            url.close()
    except:
        return


file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=save_file)


###save as functionality
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('Text File', '*.txt'), ("PDF Files", "*.pdf"), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label='Save As', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)

## convert_to_pdf

def convert_to_pdf():
    # Get the content from the text editor
    content = text_editor.get("1.0", tk.END)

    # Create a PDF object
    pdf = FPDF()

    # Add a new page and set font properties
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add the content to the PDF
    lines = content.split("\n")
    for line in lines:
        pdf.cell(0, 10, txt=line, ln=True)

    # Save the PDF file
    file_name = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=[("PDF Files", ".pdf"), ("All Files", ".*")])
    if file_name:
        pdf.output(file_name)
        messagebox.showinfo("PDF Converter", "File converted to PDF successfully.")
pdf_btn.configure(command=convert_to_pdf)

##Dictionary(word):
import tkinter as tk
from tkinter import ttk, Button, StringVar, Label, Toplevel
from tkinter import simpledialog
from googletrans import Translator
from tkinter import simpledialog, messagebox, Toplevel


# Example usage:
# dictionary_btn.configure(command=lookup_word)

def lookup_word():
    result_dialogue =Toplevel()
    result_dialogue.withdraw()  # Hide the main window

    input_text = simpledialog.askstring("Input", "Enter the text to translate:")

    
    target_language = simpledialog.askstring("Input", "Enter the target language code (e.g., 'bn' for Bengali):")

    translated_text = search_dictionary(input_text, target_language)

    result_message = f"Original Text: {input_text}\nTranslated Text: {translated_text}"

    # Display the result in a dialogue box
    label= messagebox.showinfo("Translation Result", result_message)
    
def search_dictionary(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

dictionary_btn.configure ( command=lookup_word)


# Print File Function
def print_file():
    # printer_name = win32print.GetDefaultPrinter()
    # status_bar.config(text=printer_name)

    # Grab Filename
    file_to_print = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(
    ("Text Files", "*.txt"), ("HTML Files", "*.html"),("PDF Files", "*.pdf"), ("Python Files", "*.py"), ("All Files", "*.*")))

    # Check to see if we grabbed a filename
    if file_to_print:
        # Print the file
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)


print_btn.configure ( command=print_file )


#edit menu Time/Date option
def TimeDate():     
    now = datetime.datetime.now()
    # dd/mm/YY H:M:S
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Your Date & Time", dtString)

#help menu About option

def About():     
    label = messagebox.showinfo("About Notepad", "Notepad is created by - \nModern Notepad CSE 4th Student of Modern Institute of Engineering & Technology")

#adding help in help menu


def helps():     
    label = messagebox.showinfo("Help", "Notepad is created only for Project purpose.\n ")

#adding query in help menu

def query():     
    label = messagebox.showinfo("Query", "Ask the team KARAK.\n * THANK You *")

# help

help = tk.Menu(main_menu, tearoff =0 )
view.add_cascade(label='Help', menu = help)


# ----------&&&&& End Help menu &&&&&----------#


help.add_command(label='Query',compound=tk.LEFT, command=query)
help.add_command(label='Help', compound=tk.LEFT, command=helps)

##exit functionality

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file')
            if mbox is True:
                ##if user wants to save the file and it already exists
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                   filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return


file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)


###edit commands
### find functionality

def find_func(event=None):
    ##using tag inbuilt function
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if (not start_pos):
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.resizable(0, 0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find :')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    ##entry boxes
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## Button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    ##label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ##entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ##button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()
# Binding the undo functionality to Ctrl+Z
#def undo(event=None):
 #   try:
  #      text_editor.edit_undo()
   # except tk.TclError:
    #    pass
#edit.add_command(label='Undo', compound=tk.LEFT, accelerator='Ctrl+Z', command=undo)

edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C',
                 command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V',
                 command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X',
                 command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+ALt+X',
                 command=lambda: text_editor.delete(1.0, tk.END))
#edit.add_command(label='UNDO', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+z',
  #               command=lambda: text_editor.undo(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command=find_func)

# view check button
##it will have check button

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False

    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0, variable=show_toolbar, image=tool_bar_icon,
                     compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=show_statusbar, image=status_bar_icon,
                     compound=tk.LEFT, command=hide_statusbar)

view.add_command(label='Time & Date', command = TimeDate)
view.add_command(label='About', command =About)

###color theme
def change_theme():
    choose_theme = theme_choice.get()
    color_tuple = color_dict.get(choose_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT,
                                command=change_theme)
    count += 1

# ----------&&&&& End main menu functinality &&&&&----------#


##bindi shortcut keys
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)
#main_application.bind("<Control-z>", undo)

main_application.config(menu=main_menu)
main_application.mainloop()