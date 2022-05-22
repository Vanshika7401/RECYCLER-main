
from PIL import ImageTk
from tkinter import *
from tkinter import font
import qr_code_reader as qcr
import Testing 


path = "C:\\Users\\dexterous-devu\\Documents\\Hackathon Techx Innovate 2022\\website\\"
root = Tk()
#root.geometry('2540x1440')
root.attributes('-fullscreen', True)
bg = ImageTk.PhotoImage(file = path+"bg.jpg")
label1 = Label(root, image=bg)
label1.pack()
#label1.config(width = 1000, height=1000)

Bottle = 10
Metal = 25



def end():

    root.mainloop()


def fetch_address():
    address = qcr.main_new()
    print(address)


def category():
    def check():
        data = entry1.get()
        print(data)
        data1 = Testing.NN_model(data)
        if 'Bisleri' in data:
            if data1 == 'Plastic':
               print(data1)
               pass
            
            else:
                main()
        elif 'Can' in data:
            if data1 == 'Metal':
                print(data1)
                pass

            else:
                main()
        fetch_address()

    entry1 = StringVar()
    Entry(root, textvariable=entry1).place(x = 384, y=494)
    b = Button(root, text = 'Push', command=check)
    b.pack()
    b.place(x= 345, y=194)

    

def main():
    myfont = font.Font(family='Helvetica', size = 10)
    trash_label = Button(root, text= 'Put your Trash', font = myfont, command=category)
    trash_label.place(x=500, y= 308)
    trash_label.config(width=40, height=10)
    #trash_label.pack(side=CENTER).config(weight=100, height=100)
main()
end()