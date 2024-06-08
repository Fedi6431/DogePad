#https://it.lambdageeks.com/python-project-ideas/
#https://www.pythontutorial.net/tkinter/
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import tkinter as tk
import subprocess
import random
import time
import os


def on_tab_change(event):
    current_tab = notebook.index(notebook.select())
    if current_tab == 2:  
        text_widget.config(state=NORMAL)
    elif current_tab == 1:
        
        text_widget.config(state=DISABLED)
        update_tree_view()


def save_file(event):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get("1.0", END))

def install_doge():
    showinfo(
    title='Installing Doge',
    message='Installing doge, please wait'
)
    pb.start(1)  
    for _ in range(60):  
        frame4.update_idletasks()  
        pb.step(random.randint(1, 30)) 
        frame4.after(280)  

    pb.stop()

    showinfo(
        title='Installing Doge',
        message='Doge installed successfully!'
    )

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)

    with open('Doge.txt', 'w') as file:
        file.write("""You need to share with your friend DogePad 
Because is very nice and usefull :D""")


    with open('DogeAscii.txt', 'w') as file:
        file.write("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0OkxxddddxkOOkkkkkO0KXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kxolccccc:::;;;;;;::::::coxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdllooolc::;,,,,,;;;;::c::cc:;::ldONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWN0kxdooddolllc:;,,,,,,;;;;;;;::ccccc::;;lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWNX0Oxolldxkkkkxdllc:;,',,,,;;;;;:::ccccccc:::;;cdOXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWXOxoc,,;cloooxkOOOkxolc:;,,,,,,;:cccllooollcc:::::::::cdkXMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWN0xl:,'',:loooodxxkkkkxxdooc:;;;;:cloooooddddollcc:::::::::::lkXMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMWKkdl;,,,,,;lxxdoodxOkddxxxxxdoc:::clodxxxxoooolllcc:::::cc:;;,,;;,cxOXWMMMMMMMMMMMMMMMMMMM
MMMMMMWXkdc:;;:::;:ldkkkdl;...;clddddoollcclloooddddolclloddoc::::cccc:,.''..'',lkNMMMMMMMMMMMMMMMMM
MMMMMMXxlcccllodxxxkO0KK0kc.  .',:loolccc::ccclcccclc::clooolc:;;;:cccc;..........cONMMMMMMMMMMMMMMM
MMMMMMNkl::::cdxkO0KXNWNKK0xoll:;:cc::;;,,,,;;:::,'............',;:cclc:,..........'c0NMMMMMMMMMMMMM
MMMMMMMWXK0x:cxOKXNWMMWNXKKK0Oxolc::;,,''',,,;;;,..............,:::cclccc;...........'lKWMMMMMMMMMMM
MMMMMMMMMMWkloOXNWWMMMMMWWNX0Oxdollcc:::;;;;,,;;'...,:oollloodddolllllccccc;..........';lONMMMMMMMMM
MMMMMMMMMWk:o0XWWMMMMMMWWNXkc;'......';clolc::::;;;:ldkkkxxxdoooodkkxolllloo:,...'..''''',cxKWMMMMMM
MMMMMMMMW0llOXWMMMMMMMMWXO:.           .,ldxdolc:;;:ok000000Okxxk0XX0xolccllc:,',;::::;;;,,';o0WMMMM
MMMMMMMMXockKWMMMMMMWNNXXo               .lOOxlc:;,;lxO0000KK0OO0NWWXOxocccllc;,;clc:;;;;;;,..lNMMMM
MMMMMMMWk:o0NWMMMMMWNX0KXo.               :kkdc::;,,;cxO00000OO0XWWWXK0kdlcolc;'',;;;lddolcc:lKMMMMM
MMMMMMMXl:xKNWMMMMMWNX00Kx.              .lkxl::;,,'',lxkO00OO0KNWWNXKK0kdllc:;'.,okKWMWWWWWNWMMMMMM
MMMMMMMO;l0XWMMMMMMWWNK00kc.           .,codl:;,,'''.';:lx000OO0XNNX00KK0xdlc:;',OWMMMMMMMMMMMMMMMMM
MMMMMMWx:dKXNWWWMMWWWWXOxo:;.        ..,:clc:;,''.......;okOkxxOXXXKOOKK0Oxol:;.;0MMMMMMMMMMMMMMMMMM
MMMMMMNd;oOKNWWWMMMMWWXk:,,'..      ...';::;,'.......   .;okdcckKXK000KK0Oxdlc;',OMMMMMMMMMMMMMMMMMM
MMMMMMW0l:d0NWMMMMMMMWN0o:,..         ........          'codc;lk0K0000K0Oxxdl:,..dWMMMMMMMMMMMMMMMMM
MMMMMMMMXo:dKNWMMMMMMMMN0xoc,'.                        .;cc;,;dO0OOOO0Okxddoc;'..oNMMMMMMMMMMMMMMMMM
MMMMMMMMMNOdOKXWMMMMMMMMNOxdoc;'........             ..,,,,,:oxkxxxkOkkxxxxo:;'.'xWMMMMMMMMMMMMMMMMM
MMMMMMMMMMWXK0KXWMMMMMMMMXkdool:,',,,''..        ......'';cdxxdoodxxkkkkkkdlc;,.,OMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWNKKKXWWMMMMMMMNOdool:,;;,....    .........';coxxdolloxkkkOkkkdolc;..oXMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWNXKKXNWMMMMMMMWXkc,'......   ...... ....,cllollcclxOOOOOOkxdoc;,..cKMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWNKKXXNWMMMMMMMNOl,..      ....  ...',:lllllllooxOO0OOkxolc:,..'lKWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWNXKKNWWWWWWMWN0d:'...  ........';:coooddooodxkOOOOxdol:,',;oKWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWNXXXXXXNNNNNX0koc,'.........,;:cloooddooodxkOkxdol:;,;dKNWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWNXKKKKKKKXK0kdl:;,''''',;;:ccloooollloddddolclllldONMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWNXXX0O0OOkxdolcc::::::cllllllccclloddxkkkOKNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXKK0OkxxdolcclllllllllooxOKXXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNXXK00O00OOOO000XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 """)

root = Tk()
root.title('DogePad')
root.geometry('900x700')
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(notebook, width=1000, height=900)
frame2 = ttk.Frame(notebook, width=1000, height=900)
frame3 = ttk.Frame(notebook, width=1000, height=900)
frame4 = ttk.Frame(notebook, width=1000, height=900)


frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)


notebook.add(frame3, text='Note')
notebook.add(frame1, text='Doge')
notebook.add(frame4, text='Fun Install')
notebook.add(frame2, text='Info')


pb = ttk.Progressbar(
    frame4,
    orient='horizontal',
    mode='determinate',
    length=280,
    maximum=280,  
    value=0,    
)


start_button = ttk.Button(
    frame4,
    text='Install',
    command=install_doge
)

frame4.grid_rowconfigure(0, weight=1)
frame4.grid_columnconfigure(0, weight=1)

pb.grid(row=0, column=0, padx=100, pady=200, sticky="nsew")

start_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


root.iconbitmap('./Icon/DogeIco.ico')


photo = PhotoImage(file='./Image/Doge.png')
image_label = ttk.Label(
    frame1,
    image=photo,
    padding=5
)
image_label.pack()

text_widget = Text(frame3)
text_widget.pack(side='left', fill='both', expand=True)  

scrollbar = ttk.Scrollbar(frame3, orient='vertical', command=text_widget.yview)
scrollbar.pack(side='right', fill='y') 
text_widget.config(yscrollcommand=scrollbar.set)

label = ttk.Label(
    frame2,
    text='Info',
    font=("sans", 20))
label.pack(ipadx=10, ipady=10)

Fe = ttk.Label(frame2, text='Coded by Fedi6431', font=("sans", 15))
Ve = ttk.Label(frame2, text='Version 3.9', font=("sans", 10))

Fe.pack(ipadx=10, ipady=10)
Ve.pack(ipadx=10, ipady=10)

root.bind("<Control-s>", save_file)
root.mainloop()
