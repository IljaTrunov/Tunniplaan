from tkinter import *
from tkinter.messagebox import *

def failist_sõnastikusse():
        tund_kirjeldus={}
        f = open("tundid_kirjeldused.txt","r")
        for line in f:
            tund,kirjeldus=line.strip().split(":")
            tund_kirjeldus[tund.strip()]=kirjeldus.strip()
        f.close()
        print(tund_kirjeldus)
        return tund_kirjeldus
        

def kirjeldus_aknasse(t:str):
    if (askyesno("Küsimus", "Kas tahad kirjeldust näha?")):
        alam_aken=Toplevel()
        alam_aken.title(t)
        lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
        c=Canvas(alam_aken,height=800,width=1200)
        file=PhotoImage(file=t)
        c.create_image(10,10,image=file,anchor=NW)
        c.pack()
        alam_aken.mainloop()
    else:
         showinfo("Vastus","Kui ei taha siis ei taha")
    print(tund_kirjeldus[t])
    
tund_kirjeldus=failist_sõnastikusse()

#def kirjeldus():
    #print(tund_kirjeldus)
    #pass



aken = Tk()
aken.title("Tunniplaan TARpv21")
aken.geometry("1920x1080")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(1,10,2):
    paev=Label(aken, text=p[j],relief="solid",font="Calibri 25").grid(row=i, column=0, rowspan=2, sticky=N+S+W+E)
    j+=1
#paev2=Label(aken, text="Teisipäev",relief="solid",font="Calibri 25").grid(row=3, column=0, rowspan=2, sticky=N+S+W+E)
#paev3=Label(aken, text="Kolmapäev",relief="solid",font="Calibri 25").grid(row=5, column=0, rowspan=2, sticky=N+S+W+E)
#paev4=Label(aken, text="Neljapäev",relief="solid",font="Calibri 25").grid(row=7, column=0, rowspan=2, sticky=N+S+W+E)
#paev5=Label(aken, text="Reede",relief="solid",font="Calibri 25").grid(row=9, column=0, rowspan=2, sticky=N+S+W+E)
kell=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
for i in range(11):
    tund="t"+str(i)
    tund=tund1=Label(aken, text=str(i)+"\n"+kell[i], relief="solid",font="Calibri 15").grid(row=0, column=i+1, sticky=N+S+W+E)

#tund1=Label(aken, text="0\n7:40-8:25", relief="solid",font="Calibri 20").grid(row=0, column=1, sticky=N+S+W+E)
#tund2=Label(aken, text="1\n8:30-9:15", relief="solid",font="Calibri 20").grid(row=0, column=2, sticky=N+S+W+E)
#tund3=Label(aken, text="2\n9:20-10:05", relief="solid",font="Calibri 20").grid(row=0, column=3, sticky=N+S+W+E)
#tund4=Label(aken, text="3\n10:10-10:55", relief="solid",font="Calibri 20").grid(row=0, column=4, sticky=N+S+W+E)
#tund5=Label(aken, text="4\n11:00-11:45", relief="solid",font="Calibri 20").grid(row=0, column=5, sticky=N+S+W+E)
#tund6=Label(aken, text="5\n11:50-12:35", relief="solid",font="Calibri 20").grid(row=0, column=6, sticky=N+S+W+E)
#tund7=Label(aken, text="6\n12:40-13:25", relief="solid",font="Calibri 20").grid(row=0, column=7, sticky=N+S+W+E)
#tund8=Label(aken, text="7\n13:30-14:15", relief="solid",font="Calibri 20").grid(row=0, column=8, sticky=N+S+W+E)
#tund9=Label(aken, text="8\n14:20-15:05", relief="solid",font="Calibri 20").grid(row=0, column=9, sticky=N+S+W+E)
#tund10=Label(aken, text="9\n15:10-15:55", relief="solid",font="Calibri 20").grid(row=0, column=10, sticky=N+S+W+E)
#tund11=Label(aken, text="10\n16:00-16:45", relief="solid",font="Calibri 20").grid(row=0, column=11, sticky=N+S+W+E)

#Понедельник
p1=Button(text="Multimeedia", command=lambda:kirjeldus_aknasse("retrochrome_.png"),font="Calibri 20",bg="cornflowerblue",relief="groove").grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
p2=Button(text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("prog.png"), font="Calibri 20",bg="skyblue",relief="groove").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
p3=Button(text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("prog.png"), font="Calibri 20",bg="skyblue",relief="groove").grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
p4=Button(text="Multimeedia",command=lambda:kirjeldus_aknasse("retrochrome_.png"), font="Calibri 20",bg="cornflowerblue",relief="groove").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
p5=Button(text="Rühmajuhatuja tund",command=lambda:kirjeldus_aknasse("prog.png"), font="Calibri 20",bg="skyblue",relief="groove").grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)

#Вторник
p6=Button(text="Inglise keel",command=lambda:kirjeldus_aknasse("english.png"), font="Calibri 26",bg="floralwhite",relief="groove").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
p7=Button(text="Inglise keel",command=lambda:kirjeldus_aknasse("english.png"), font="Calibri 26",bg="mediumslateblue",relief="groove").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
p8=Button(text="Operatsioonisüsteemide alused",command=lambda:kirjeldus_aknasse("console.png"), font="Calibri 26",bg="mediumorchid",relief="groove").grid(row=3,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
p10=Button(text="Kehaline kasvatus",command=lambda:kirjeldus_aknasse("phys.png"), font="Calibri 26",bg="palevioletred",relief="groove").grid(row=3,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
p11=Button(text="Eesti keel",command=lambda:kirjeldus_aknasse("Eesti keel Gruup 1"), font="Calibri 26",bg="mediumpurple",relief="groove").grid(row=3,column=9,sticky=N+S+W+E)
p12=Button(text="Eesti keel",command=lambda:kirjeldus_aknasse("Eesti keel Gruup 2"), font="Calibri 26",bg="darkgrey",relief="groove").grid(row=4,column=9,sticky=N+S+W+E)
p13=Button(text="Ajalugu",command=lambda:kirjeldus_aknasse("history.png"), font="Calibri 26",bg="khaki",relief="groove").grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)

#Среда
p14=Button(text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("prog.png"), font="Calibri 26",bg="skyblue",relief="groove").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
p15=Button(text="Multimeedia",command=lambda:kirjeldus_aknasse("retrochrome_.png"), font="Calibri 26",bg="cornflowerblue",relief="groove").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
p16=Button(text="Multimeedia",command=lambda:kirjeldus_aknasse("retrochrome_.png"), font="Calibri 26",bg="cornflowerblue",relief="groove").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
p17=Button(text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("prog.png"), font="Calibri 26",bg="skyblue",relief="groove").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
p18=Button(text="Kunstiained",command=lambda:kirjeldus_aknasse("isk.png"), font="Calibri 26",bg="orchid",relief="groove").grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

#Четверг
p19=Button(text="Andmebaasisüsteemide alused",command=lambda:kirjeldus_aknasse("base.png"), font="Calibri 26",bg="DeepPink1",relief="groove").grid(row=7,column=2,columnspan=5,rowspan=2,sticky=N+S+W+E)
p20=Button(text="Ajalugu",command=lambda:kirjeldus_aknasse("history.png"), font="Calibri 26",bg="khaki",relief="groove").grid(row=7,column=6,rowspan=2,sticky=N+S+W+E)
p21=Button(text="Eesti keel",command=lambda:kirjeldus_aknasse("Eesti keel Gruup 1"), font="Calibri 26",bg="mediumpurple",relief="groove").grid(row=7,column=7,sticky=N+S+W+E)
p22=Button(text="Eesti keel",command=lambda:kirjeldus_aknasse("Eesti keel Gruup 2"), font="Calibri 26",bg="darkgrey",relief="groove").grid(row=8,column=7,sticky=N+S+W+E)

#Пятница
p23=Button(text="Vene keel",command=lambda:kirjeldus_aknasse("book.png"), font="Calibri 26",bg="greenyellow",relief="groove").grid(row=9,column=3,columnspan=2,rowspan=3,sticky=N+S+W+E)
p24=Button(text="Matemaatika",command=lambda:kirjeldus_aknasse("maths.png"), font="Calibri 26",bg="lightpink",relief="groove").grid(row=9,column=6,columnspan=2,rowspan=2,sticky=N+S+W+E)
p25=Button(text="Suhtlemine ja kliienditeenindus",command=lambda:kirjeldus_aknasse("talk.png"), font="Calibri 26",bg="mediumslateblue",relief="groove").grid(row=9,column=8,columnspan=2,rowspan=2,sticky=N+S+W+E)
p26=Button(text="Ajalugu",command=lambda:kirjeldus_aknasse("history.png"), font="Calibri 26",bg="khaki",relief="groove").grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)

aken.mainloop()
