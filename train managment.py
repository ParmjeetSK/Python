from tkinter import*
from tkinter import Tk,StringVar,ttk
from tkinter import messagebox
import random
import time;
import datetime
root=Tk()

root.geometry("1350x750+0+0")
root.title("TrainTicket")
root.configure(background="pink")

Tops=Frame(root,width=1350,height=100,bd=14,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

frametopRight=Frame(f2,width=440,height=650,bg="yellow",bd=12,relief="raise")
frametopRight.pack(side=TOP)
frameBottomRight=Frame(f2,width=440,height=50,bg="yellow",bd=16,relief="raise")
frameBottomRight.pack(side=BOTTOM)

f1a=Frame(f1,width=900,height=330,bg="darkgreen",bd=8,relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=320,bg="darkgreen",bd=6,relief="raise")
f2a.pack(side=BOTTOM)

topLeft1=Frame(f1a,width=300,height=200,bg="coral",bd=16,relief="raise")
topLeft1.pack(side=LEFT)
topLeft2=Frame(f1a,width=300,height=200,bg="teal",bd=16,relief="raise")
topLeft2.pack(side=RIGHT)
topLeft3=Frame(f1a,width=300,height=200,bg="lightgreen",bd=16,relief="raise")
topLeft3.pack(side=RIGHT)

Tops.configure(background="red")
f1.configure(background="green")
f2.configure(background="blue")

bottomLeft1=Frame(f2a,width=450,height=450,bg="red",bd=14,relief="raise")
bottomLeft1.pack(side=LEFT)

bottomLeft2=Frame(f2a,width=450,height=450,bg="skyblue",bd=14,relief="raise")
bottomLeft2.pack(side=RIGHT)

Tops.configure(background="red")
f1.configure(background="green")
f2.configure(background="blue")

lb1Title=Label(Tops,font=("arial",40,"bold"),text="Train Ticketing Systems",bg="pink",fg="red",bd=10,width=41,justify="center")
lb1Title.grid(row=0,column=0)

Date1=StringVar()
time1=StringVar()
Ticketclass=StringVar()
TicketPrice=StringVar()
Child_Ticket=StringVar()
Adult_Ticket=StringVar()
SeniorCitizen_Ticket=StringVar()
From_Destination=StringVar()
To_Destination=StringVar()
Fee_Price=StringVar()
Route=StringVar()
Receipt_Ref=StringVar()


Ticketclass.set("")
TicketPrice.set("")
Child_Ticket.set("")
Adult_Ticket.set("")
SeniorCitizen_Ticket.set("")
From_Destination.set("")
To_Destination.set("")
Fee_Price.set("")
Route.set("")
Receipt_Ref.set("")

lb1Receipt=Label(frametopRight,font=("arial",18,"bold"),text="\nTravelling Ticketing Systems\n",bg="purple"
                 ,fg="white",bd=10,width=25,justify="center")
lb1Receipt.grid(row=0,column=0)

lb1Class1=Label(frameBottomRight,font=("arial",10,"bold"),text="Class",bg="purple",fg="white",relief="sunken",width=8,justify="center")
lb1Class1.place(x=0,y=0)

lb1Class2=Label(frameBottomRight,font=("arial",10,"bold"),bg="purple",fg="white",width=8,relief="sunken",justify="center")
lb1Class2.place(x=0,y=22)

lb1Ticket1=Label(frameBottomRight,font=("arial",9,"bold"),text="Ticket",bg="purple",fg="white",width=8,relief="sunken",justify="center")
lb1Ticket1.place(x=70,y=0)

lb1Ticket2=Label(frameBottomRight,font=("arial",9,"bold"),bg="purple",fg="white",width=8,relief="sunken",textvariable=TicketPrice,justify="center")
lb1Ticket2.place(x=70,y=22)

lb1Child1=Label(frameBottomRight,font=("arial",9,"bold"),text="Child",bg="purple",fg="white",relief="sunken",width=8,justify="center")
lb1Child1.place(x=133,y=0)

lb1Child2=Label(frameBottomRight,font=("arial",9,"bold"),bg="purple",fg="white",relief="sunken",
                textvariable=Child_Ticket,width=8,justify="center")
lb1Child2.place(x=133,y=22)

lb1Adult1=Label(frameBottomRight,font=("arial",9,"bold"),text="Adult",bg="purple"
                ,fg="white",relief="sunken",width=8,justify="center")
lb1Adult1.place(x=195,y=0)

lb1Adult2=Label(frameBottomRight,font=("arial",9,"bold"),bg="purple",fg="white",
                relief="sunken",textvariable=Adult_Ticket,width=8,justify="center")
lb1Adult2.place(x=195,y=22)

lb1SeniorCitizen1=Label(frameBottomRight,font=("arial",9,"bold"),text="SeniorCitizen",bg="purple",
                        fg="white",relief="sunken",width=11,anchor="w")
lb1SeniorCitizen1.grid(row=0,column=3)

lb1SeniorCitizen2=Label(frameBottomRight,font=("arial",9,"bold"),bg="purple",fg="white"
                        ,relief="sunken",textvariable=SeniorCitizen_Ticket,width=11)
lb1SeniorCitizen2.grid(row=1,column=3)

lb1sp=Label(frameBottomRight,font=("arial",12,"bold"),bg="yellow",fg="white",relief="sunken",width=34,height=2,justify="center")
lb1sp.grid(row=2,column=0,columnspan=4)

lb1From1=Label(frameBottomRight,font=("arial",14,"bold"),text="From",bg="purple",fg="white",relief="sunken",width=7,justify="center")
lb1From1.grid(row=3,column=1)

lb1From2=Label(frameBottomRight,font=("arial",14,"bold"),bg="purple",fg="white",relief="sunken",textvariable=From_Destination,width=7,justify="center")
lb1From2.grid(row=3,column=2)

lb1To1=Label(frameBottomRight,font=("arial",14,"bold"),text="To",bg="purple",fg="white",relief="sunken",width=7,justify="center")
lb1To1.grid(row=4,column=1)

lb1To2=Label(frameBottomRight,font=("arial",14,"bold"),bg="purple",fg="white",relief="sunken",textvariable=To_Destination,width=7,justify="center")
lb1To2.grid(row=4,column=2)

lb1Price1=Label(frameBottomRight,font=("arial",14,"bold"),text="Price",bg="purple",fg="white",relief="sunken",width=7,justify="center")
lb1Price1.grid(row=5,column=1)

lb1Price2=Label(frameBottomRight,font=("arial",14,"bold"),bg="purple",fg="white",relief="sunken",textvariable=Fee_Price,width=7,justify="center")
lb1Price2.grid(row=5,column=2)

lb1sp=Label(frameBottomRight,font=("arial",12,"bold"),bg="yellow",fg="white",relief="sunken",width=34,height=2,justify="center")
lb1sp.grid(row=6,column=0,columnspan=4)

lb1RefNo1=Label(frameBottomRight,font=("arial",10,"bold"),text="Ref No",bg="purple",fg="white",relief="sunken",width=8,justify="center")
lb1RefNo1.place(x=0,y=214)

lb1RefNo2=Label(frameBottomRight,font=("arial",10,"bold"),bg="purple",fg="white",relief="sunken",width=8,justify="center")
lb1RefNo2.place(x=0,y=236)

lb1Time1=Label(frameBottomRight,font=("arial",10,"bold"),text="Time",bg="purple",fg="white",relief="sunken",width=8,justify="center")
lb1Time1.place(x=70,y=214)

lb1Time2=Label(frameBottomRight,font=("arial",10,"bold"),bg="purple",fg="white",relief="sunken",textvariable=time1,width=8,justify="center")
lb1Time2.place(x=70,y=236)


lb1Date1=Label(frameBottomRight,font=("arial",10,"bold"),text="Date",bg="purple",fg="white",relief="sunken",width=8,justify="center")
lb1Date1.place(x=140,y=214)

lb1Date2=Label(frameBottomRight,font=("arial",10,"bold"),bg="purple",fg="white",relief="sunken",textvariable=Date1,width=8,justify="center")
lb1Date2.place(x=140,y=236)

lb1Route1=Label(frameBottomRight,font=("arial",10,"bold"),text="Route",bg="purple",fg="white",relief="sunken",width=7,justify="center",anchor="w")
lb1Route1.place(x=203,y=214)

lb1Route2=Label(frameBottomRight,font=("arial",10,"bold"),bg="purple",fg="white",relief="sunken",width=7,justify="center")
lb1Route2.place(x=203,y=236)
lb1Cancelling1=Label(frameBottomRight,font=("arial",9,"bold"),text="Cancelling",bg="purple",fg="white",relief="sunken",width=8,justify="center")
lb1Cancelling1.grid(row=7,column=3)

lb1Cancelling2=Label(frameBottomRight,font=("arial",9,"bold"),bg="purple",fg="white",relief="sunken",width=8,justify="center")
lb1Cancelling2.grid(row=8,column=3)

def btnTotal(number):
    global operator
    operator=operator + int(number)
    text_Input.set(operator)

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

def iExit():
  qExit=messagebox.askyesno("Quit System","Do You Want to quit?")
  if qExit > 0:
       root.destroy()
       return

def Travel_Cost():
    if  var9.get()=="Punjab"and var1.get()==1 and var5.get()==1:
        Tcost=float(30.8)
        Single=float(var11.get())
        Child_Tax="Rs",str("%.2f"%(Tcost*0.03))
        Child_Fees="Rs",str("%.2f"%(Tcost*Single))
        TotalCost="Rs",str("%.2f"%((Tcost*Single)+(Tcost*0.03)))
        StateTax.set(Child_Tax)
        GSTTax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        Ticketclass.set("Standard")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("YES")
        Adult_Ticket.set("No")
        SeniorCitizen_Ticket.set("no")
        From_Destination.set("India")
        To_Destination.set("Punjab")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        X=random.randint(109,5876)
        randomRef=str(X)
        Receipt_Ref.set("TFL"+randomRef)

    elif(var9.get() == "punjab" and var1.get() == 1 and var5.get() == 1):
        Tcost=float(10.3)
        Single=float(var11.get())
        Adult_Tax="Rs",str("%.2f"%(Tcost*0.03))
        Adult_Fees="Rs",str("%.2f"%(Tcost*Single))
        TotalCost="Rs",str("%.2f"%((Tcost*Single)+(Tcost*0.03)))
        StateTax.set(Adult_Tax)
        GSTTax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Standard")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("no")
        Adult_Ticket.set("yes")
        SeniorCitizen_Ticket.set("no")
        From_Destination.set("India")
        To_Destination.set("punjab")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        X=random.randint(109,5876)
        randomRef=str(X)
        Receipt_Ref.set("TFL"+randomRef)

    elif(var9.get() == "punjab" and var1.get() == 1 and var5.get() == 1):
        Tcost=float(7.3)
        Single=float(var10.get())
        SeniorCitizen_Tax="Rs",str("%.2f"%(Tcost*0.03))
        SeniorCitizen_Fees="Rs",str("%.2f"%(Tcost*Single))
        TotalCost="Rs",str("%.2f"%((Tcost*Single)+(Tcost*0.03)))
        StateTax.set( SeniorCitizen_Tax)
        GSTTax.set( SeniorCitizen_Tax)
        SubTotal.set( SeniorCitizen_Fees)
        Ticketclass.set("Standard")
        TicketPrice.set( SeniorCitizen_Fees)
        Child_Ticket.set("no")
        Adult_Ticket.set("no")
        SeniorCitizen_Ticket.set("yes")
        From_Destination.set("India")
        To_Destination.set("punjab")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        X=random.randint(109,5876)
        randomRef=str(X)
        Receipt_Ref.set("TFL"+randomRef)

def chkbutton_value():
    if(var10.get()==1):
        var12.set("")
        entSingle.configure(state=NORMAL)
    elif var10.get()==0:
        var12.set("0")
        entSingle.configure(state=DISABLED)
    if(var11.get()==1):
        var6.set("")
        entReturn.configure(state=NORMAL)
    elif var11.get()==0:
        var6.set("0")
        entReturn.configure(state=DISABLED)
    if(var10.get()==1):
        var4.set("")
        entReturn.configure(state=NORMAL)
    elif var10.get()==0:
        var4.set("0")
        entReturn.configure(state=DISABLED)


var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = StringVar()
var11 = StringVar()
var12 = StringVar()
StateTax = StringVar()
GSTTax = StringVar()

def Reset():
    StateTax.set("0")
    GSTTax.set("0")
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    StateTax.set("0")
    GSTTax.set("0")
    SubTotal.set("0")
    Total.set("0")
    Ticketclass.set("")
    TicketPrice.set("0")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    SeniorCitizen_Ticket.set("")
    From_Destination.set("")
    To_Destination.set("")
    Fee_Price.set("")


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=IntVar()
var11=IntVar()
var12 = IntVar()
StateTax = StringVar()
GSTTax = StringVar()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")

StateTax=StringVar()
GSTTax=StringVar()
SubTotal=StringVar()
Total=StringVar()
text_Input=StringVar()
operator=""


Date1.set(time.strftime("%d/%m/%y"))
time1.set(time.strftime('%H:%M:%S'))

lb1Class=Label(topLeft1,font=("arial",22,"bold"),text="Class",bg="coral",fg="indigo",bd=8)
lb1Class.grid(row=0,column=0,sticky=W)
chkStandard=Checkbutton(topLeft1,font=("arial",20,"bold"),bg="coral",text="Standard",variable=var1,onvalue=1,offvalue=0)
chkStandard.grid(row=1,column=0,sticky=W)
chkEconomy=Checkbutton(topLeft1,font=("arial",20,"bold"),bg="coral",text="Economy",variable=var2,onvalue=1,offvalue=0)
chkEconomy.grid(row=2,column=0,sticky=W)
chkFirstClass=Checkbutton(topLeft1,font=("arial",20,"bold"),bg="coral",text="First Class",variable=var3,onvalue=1,offvalue=0)
chkFirstClass.grid(row=3,column=0,sticky=W)


lb1Select=Label(topLeft3,font=("arial",18,"bold"),text="Destination Selector",bg="lightgreen",fg="brown",bd=8)
lb1Select.grid(row=0,column=0,sticky=W,columnspan=2)
lb1Destination=Label(topLeft3,font=("arial",18,"bold"),text="Destination",bg="lightgreen",bd=4)
lb1Destination.grid(row=1,column=0,sticky=W)
cboDestination=ttk.Combobox(topLeft3,textvar=var9,state="writeonly",font=("arial",18,"bold"),width=8)
cboDestination["value"]=("","Punjab","Harayana","Himachal Pardesh","Uttrakhand","Madhya Pardesh","Uttra Pardesh","Goa","Jammu Kashmir",)
cboDestination.current(0)
cboDestination.grid(row=1,column=1)

chkChild=Checkbutton(topLeft3,font=("arial",18,"bold"),bg="lightgreen",text="Child",variable=var10,onvalue=1,offvalue=0)
chkChild.grid(row=2,column=0,sticky=W)
chkAdult=Checkbutton(topLeft3,font=("arial",18,"bold"),bg="lightgreen",text="Adult",variable=var11,onvalue=1,offvalue=0)
chkAdult.grid(row=3,column=0,sticky=W)
chkSeniorCitizen=Checkbutton(topLeft3,font=("arial",18,"bold"),bg="lightgreen",text="Senior Citizen",variable=var3,onvalue=1,offvalue=0)
chkSeniorCitizen.grid(row=4,column=0,sticky=W)


lb1Class=Label(topLeft2,font=("arial",22,"bold"),bg="teal",fg="yellow",text="Ticket Type",bd=8)
lb1Class.grid(row=0,column=0,sticky=W)
chkSingle=Checkbutton(topLeft2,font=("arial",20,"bold"),bg="teal",fg="white",text="Single",variable=var4,onvalue=1,offvalue=0,command=chkbutton_value)
chkSingle.grid(row=1,column=0,sticky=W)
entSingle=Entry(topLeft2,font=("arial",22,"bold"),bg="powderblue",textvar=var5,bd=2,width=8,state=DISABLED)
entSingle.grid(row=1,column=1,sticky=W)
chkReturn=Checkbutton(topLeft2,font=("arial",20,"bold"),bg="teal",fg="white",text="Return",variable=var4,onvalue=1,offvalue=0,command=chkbutton_value)
chkReturn.grid(row=2,column=0,sticky=W)
entReturn=Entry(topLeft2,font=("arial",22,"bold"),bg="powderblue",textvariable=var6,bd=2,width=8,state=DISABLED)
entReturn.grid(row=2,column=1,sticky=W)
lb1Comment=Label(topLeft2,font=("arial",20,"bold"),bg="teal",fg="white",text="Comment",bd=8)
lb1Comment.grid(row=3,column=0,sticky=W)
entComment=Entry(topLeft2,font=("arial",20,"bold"),bg="powderblue",textvariable=var7,bd=2,width=8)
entComment.grid(row=3,column=1,sticky=W)


text_Input=StringVar()
txtDisplay=Entry(bottomLeft2,font=("arial",22,"bold"),textvariable=text_Input,bd=8,bg="yellow",justify="right")
txtDisplay.grid(columnspan=4)

btn7=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="7",bg="pink",command=lambda:btnClick(7),width=4).grid(row=2,column=0)
btn8=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="8",bg="pink",command=lambda:btnClick(8),width=4).grid(row=2,column=1)
btn9=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="9",bg="pink",command=lambda:btnClick(9),width=4).grid(row=2,column=2)
Addition=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="+",bg="pink",command=lambda:btnClick("+"),width=4).grid(row=2,column=3)
btn4=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="4",bg="pink",command=lambda:btnClick(4),width=4).grid(row=3,column=0)
btn5=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="5",bg="pink",command=lambda:btnClick(5),width=4).grid(row=3,column=1)
btn6=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="6",bg="pink",command=lambda:btnClick(6),width=4).grid(row=3,column=2)
Substraction=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="-",bg="pink",width=4,command=lambda:btnClick("-")).grid(row=3,column=3)
btn1=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="1",bg="pink",command=lambda:btnClick(1),width=4).grid(row=4,column=0)
btn2=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="2",bg="pink",width=4,command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="3",bg="pink",width=4,command=lambda:btnClick(3)).grid(row=4,column=2)
Multiply=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="*",bg="pink",width=4,command=lambda:btnClick("*")).grid(row=4,column=3)
btn0=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="0",bg="pink",width=4,command=lambda:btnClick(0)).grid(row=5,column=0)
btnclear=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="c",bg="pink",width=4,command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="=",bg="pink",width=4,command=btnEqualsInput).grid(row=5,column=2)
Division=Button(bottomLeft2,padx=8,pady=8,bd=8,fg="purple",font=("arial",14,"bold"),
            text="/",bg="pink",command=lambda:btnClick("/"),width=4).grid(row=5,column=3)


lblStateTax=Label(bottomLeft1,font=("arial",24,"bold"),bg="red",fg="pink",text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=1,column=2)
txtStateTax=Entry(bottomLeft1,font=("arial",16,"bold"),textvariable=StateTax,bd=10,width=25
                  ,bg="powderblue",justify="right")
txtStateTax.grid(row=1,column=3)

lblGSTTax=Label(bottomLeft1,font=("arial",24,"bold"),bg="red",fg="pink",text="GST Tax",bd=16,anchor="w")
lblGSTTax.grid(row=2,column=2)
txtGSTTax=Entry(bottomLeft1,font=("arial",16,"bold"),textvariable=GSTTax,bd=10,width=25
                  ,bg="powderblue",justify="right")
txtGSTTax.grid(row=2,column=3)

lblSubTotal=Label(bottomLeft1,font=("arial",24,"bold"),bg="red",fg="pink",text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=3,column=2)
txtSubTotal=Entry(bottomLeft1,font=("arial",16,"bold"),textvariable=SubTotal,bd=10,width=25
                  ,bg="powderblue",justify="right")
txtSubTotal.grid(row=3,column=3)

lblTotalCost=Label(bottomLeft1,font=("arial",24,"bold"),bg="red",fg="pink",text="Travel_Cost",bd=16,anchor="w")
lblTotalCost.grid(row=4,column=2)
txtTotalCost=Entry(bottomLeft1,font=("arial",16,"bold"),textvariable=Total,bd=10,width=25
                  ,bg="powderblue",justify="right")
txtTotalCost.grid(row=4,column=3)

lb1sp=Label(bottomLeft1,font=("arial",13,"bold"),width=34,height=1,relief="sunken",justify="center")
lb1sp.grid(row=5,column=0,columnspan=4)

lblSpace=Label(bottomLeft1,font=("arial",24,"bold"),text="Payment",fg="purple",bg="pink",bd=16,anchor="w")
lblSpace.grid(row=6,column=2)

lblSpace=Label(bottomLeft2,font=("arial",8,"bold"),text="Amount",bg="purple",fg="powderblue",bd=16,anchor="w")
lblSpace.grid(row=6,columnspan=4)

lblReceipt=Label(frameBottomRight,font=("arial",9,"bold"),bg="orange",text="comment:",bd=2,anchor="w")
lblReceipt.grid(row=11,column=0,sticky=W)

txtReceipt=Text(frameBottomRight,width=40,height=4,bg="purple",bd=8,font=("arial",11,"bold"))
txtReceipt.grid(row=12,column=0,columnspan=4)

lb1Receipt=Label(frameBottomRight,font=("arial",12,"bold"),bd=2,anchor="w")
lb1Receipt.grid(row=8,column=0,sticky=W)

lb1sp=Label(frameBottomRight,font=("arial",13,"bold"),width=34,height=1,relief="sunken",justify="center")
lb1sp.grid(row=9,column=0,columnspan=4)

btnTotal=Button(frameBottomRight,text="Total",padx=2,pady=2,bd=2,fg="white",bg="brown",font=("arial",10,"bold"),width=6,height=1,command=Travel_Cost)
btnTotal.place(x=1,y=283)

btnClear=Button(frameBottomRight,text="Clear",padx=2,pady=2,bd=2,fg="white",bg="brown",font=("arial",10,"bold"),width=6,height=1,command=Reset)
btnClear.place(x=61,y=283)

btnReset=Button(frameBottomRight,text="Reset",padx=2,pady=2,bd=2,fg="white",bg="brown",font=("arial",10,"bold"),width=6,height=1,command=Reset)
btnReset.place(x=121,y=283)

btnBack=Button(frameBottomRight,text="Back",padx=2,pady=2,bd=2,fg="white",bg="brown",font=("arial",10,"bold"),width=6,height=1,command=Reset)
btnBack.place(x=181,y=283)

btnExit=Button(frameBottomRight,text="Exit",padx=2,pady=2,bd=2,fg="white",bg="brown",font=("arial",10,"bold"),width=11,height=1,command=iExit)
btnExit.grid(row=10,column=3)


root.mainloop()
