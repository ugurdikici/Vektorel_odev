from tkinter import *
from socket import gethostname, gethostbyname
from tkinter import messagebox as msgbx

root = Tk()
root.geometry("900x500")
root.title("IP Adres")
root.config(bg="black")
Label(root, text="Ip Bulucu", font=("Times", 35, "bold underline"), bg="black", fg="grey").pack()


def getIP():
    hostname = gethostname()
    ip = gethostbyname(hostname)
    giveip.delete(0, END)
    if ip == "127.0.0.1":
        msgbx.showinfo("İnternet YOK", "İnternete Bağlı Değilsiniz\nYerel IP Adresiniz Gösterilecek")
        giveip.insert(END, ip)
    else:
        giveip.insert(END, ip)


def quitted():
    msgbx.showinfo("UğurDikici")
    quit()

    


Button(root, text="Get IP Address", font=("Times", 25, "bold underline"), bg="black", fg="grey", bd=10, command=getIP).place(x=140, y=100, width=270, height=70)
giveip = Entry(root, bd=10, font=("Times", 25, "bold"))
giveip.place(x=450, y=100, width=240, height=65)
Button(root, text="Çıkış", font=("Times", 25, "bold underline"), bg="black", fg="grey", bd=10, command=quitted).place(x=750, y=420)
Label(root, text="UğurDikici", font=("Times", 25, "bold"), bg="black", fg="grey", bd=10).pack(side=BOTTOM, anchor=W)
root.mainloop()