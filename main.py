from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, CENTER, END
import configparser
import clipboard
from googletrans import Translator
import re
from random import randint

config = configparser.ConfigParser()

ASSETS_PATH = (r"assets\frame0")
ASSETS_PATH2 = (r"assets\frame1")
first = 1


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def relative_to_assets2(path: str) -> Path:
    return ASSETS_PATH2 / Path(path)

def save(entry_1,entry_2):    
    config['Unique']['intermediate'] = entry_1.get()
    config['Unique']['target'] = entry_2.get()
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)


def delete_text(entry_1,entry_2):
    entry_1.delete(1.0, END)
    entry_2.delete(1.0, END)

def copytext(entry_2):
    text = entry_2.get(1.0, END)
    clipboard.copy(text)

def inserttext(entry_1):
    entry_1.delete(1.0, END)
    print(clipboard.paste())
    entry_1.insert(1.0, clipboard.paste())
    
def translate(lngs,target,entry_1,entry_2):
    text = entry_1.get(1.0, END)
    translator = Translator()
    pattern = r'(".{2,}?"|“.{2,}?”|«.{2,}?»)'
    results = re.findall(pattern, text)

    
    rcifra = []
    for i in results:
        random = randint(77777,999999999)
        random = str(random)  
        text = text.replace(i, random)        
        rcifra.append(str(random))

    for lang in lngs:
        text = translator.translate(text, dest=str(lang)).text        # Intermediate languages
    text = translator.translate(text, dest=str(target)).text          # Target language
    for i in rcifra:
        rptext = results[rcifra.index(i)]
        text = text.replace(i, rptext)
    entry_2.delete(1.0, END)
    entry_2.insert(1.0, text)

def setting(first,canvas,window):
    if first==1:
        first=0
        window = Tk()
        window.title('UniqueText 2.0')
    else:
        canvas.delete('all')
    

    window.geometry("326x609")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 609,
        width = 326,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        163.0,
        304.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,    
        borderwidth=0,
        highlightthickness=0,
        command=lambda: work(canvas,window,entry_1,entry_2),
        relief="flat"
    )
    button_1.place(
        x=108.0,
        y=517.0,
        width=111.0,
        height=42.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        166.5,
        320.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        justify=CENTER,
        font=('Arial 17'),
        bd=0,
        bg="#D9D9D9",
        fg="#5F5F5F",
        highlightthickness=0
    )
    entry_1.place(
        x=50.5,
        y=306.0,
        width=232.0,
        height=31.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        163.5,
        441.5,
        image=entry_image_2
    )
    entry_2 = Entry(    
        font=('Arial 18'),
        justify=CENTER,
        bd=0,
        bg="#D9D9D9",
        fg="#5F5F5F",
        highlightthickness=0
    )
    entry_2.place(
        x=142.5,
        y=428.0,
        width=42.0,
        height=31.0
    )

    canvas.create_text(
        34.0,
        224.0,
        anchor="nw",
        text="Intermediate \n                languages",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        31.0,
        359.0,
        anchor="nw",
        text="Target language",
        fill="#FFFFFF",
        font=("Inter", 36 * -1)
    )

    canvas.create_text(
        39.0,
        142.0,
        anchor="nw",
        text="UniqueText 2.0",
        fill="#FFFFFF",
        font=("Inter", 36 * -1)
    )
    config.read("settings.ini")
    lngsset = config["Unique"]["intermediate"]
    lngs = lngsset.split(', ')
    target = config["Unique"]["target"]
    entry_1.insert(0, lngsset)
    entry_2.insert(0, target)
    #print(entry_1.get())
    window.resizable(False, False)
    window.mainloop()







def work(canvas,window,entry_1,entry_2):

    save(entry_1,entry_2) 

    config.read("settings.ini")
    lngsset = config["Unique"]["intermediate"]
    lngs = lngsset.split(', ')
    target = config["Unique"]["target"]   
    
    canvas.delete('all')
    window.geometry("647x609")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 609,
        width = 647,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets2("image_1.png"))
    image_1 = canvas.create_image(
        324.0,
        304.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets2("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        172.5,
        324.5,
        image=entry_image_1
    )
    entry_1 = Text(
        font=('Arial 13'),
        bd=0,
        bg="#FFFFFF",
        fg="#5F5F5F",
        highlightthickness=0
    )
    entry_1.place(
        x=27.0,
        y=69.0,
        width=291.0,
        height=509.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets2("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        476.5,
        324.5,
        image=entry_image_2
    )
    entry_2 = Text(
        font=('Arial 13'),
        bd=0,
        bg="#FFFFFF",
        fg="#5F5F5F",
        highlightthickness=0
    )
    entry_2.place(
        x=331.0,
        y=69.0,
        width=291.0,
        height=509.0
    )

    button_image_1 = PhotoImage(
    file=relative_to_assets2("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: translate(lngs,target,entry_1,entry_2),
        relief="flat"
    )
    button_1.place(
        x=509.0,
        y=23.0,
        width=25.0,
        height=25.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets2("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: copytext(entry_2),
        relief="flat"
    )
    button_2.place(
        x=546.0,
        y=24.0,
        width=28.0,
        height=27.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets2("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: delete_text(entry_1,entry_2),
        relief="flat"
    )
    button_3.place(
        x=435.0,
        y=24.0,
        width=25.0,
        height=25.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets2("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: inserttext(entry_1),
        relief="flat"
    )
    button_4.place(
        x=472.0,
        y=24.0,
        width=25.0,
        height=27.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets2("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setting(0,canvas,window),
        relief="flat"
    )
    button_5.place(
        x=34.0,
        y=26.0,
        width=25.0,
        height=25.0
    )
    window.resizable(False, False)
    window.mainloop()


setting(first,'one','two')