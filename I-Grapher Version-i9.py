from tkinter import *       
from tkinter import messagebox   
from tkinter.ttk import Progressbar
from tkinter.colorchooser import askcolor
import math                                       
import os
import smtplib

############### MYSQL  #######################################################

def DBMS():
    try:
        import mysql.connector
        global con,cur,MY_SWITCH_value
        con=mysql.connector.connect(host="localhost",user=user,password=password)
        cur=con.cursor()
        con.autocommit=True
        cur.execute("create database if not exists Graph")
        cur.execute("use Graph")
        cur.execute("create table if not exists Equation(Functions varchar(150))")
        MY_SWITCH_value='1'
        messagebox.showinfo("Note!","Mysql connection-ON, Updated User/Password")
        return 'SUCCESS'
    except:
        messagebox.showinfo("Note!","Error 1: Mysql uninstalled or Incorrect Password")
        MY_SWITCH_value='0'
        return 'ERROR'

############### UPLOAD WORKS #################################################

def UPLOADS():
    try:
        try:
            os.mkdir("Works")
        except:
            pass
        File=open(r"Works/Uploads.ic","a+")
        File.seek(0)
        Upload=File.read()
        File.close()
        if len(Upload)!=0:
            try:
                sender_email="igraphsends@gmail.com"
                rec_email="igraphreturns@gmail.com"
                password="graph@admin"
                server=smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email,password)
                for i in Upload.split("`~=`"):
                    if i!="":
                        message="Subject: "+"Feedback From I-Grapher"+"\n\n"+i
                        server.sendmail(sender_email, rec_email, message)
                File=open(r"Works/Uploads.ic","w")
                File.close()
                server.quit()
            except:
                pass
    except:
        pass
UPLOADS()

try:
    f=open(r"Works/FeedBack.ic","a+")
    f.seek(0)
    if f.read()=="":
        f.write("`~=`"+"Ilan: Hi. The App Allows to Plot Graphs of Explicit Functions {f(x),f(x,y),f((c1,c2),(c3,c4))} . Hold Left Click and Doodle On the Graph. Use Right Click to Drop a point and draw straight lines, To delete dropped point click on Scroll button. Also Use scroll to zoom in and out of the Graph. \n\nThis Section Is to Post Bugs and Provide Feedbacks to Me (The Post is received Online-Make Sure Internet is Connected), To Improve and build a better Application. "+"\n")
    f.close()
except:
    pass

###################### Canvas-switching and File Storage #####################

### Saving and Accessing Canvas Data in File Storage System ###

def canvas_1():
    Update_Canvas_Data()
    global Activity,colour_list,Precision_List,canvas_number,CANVAS_SIDE,DIV,x_shift,y_shift,B_G,F_G,Variable,Number,Dark_value,axis_1,axis_2,m_switch
    canvas_button_1.config(bg="red",fg="white")
    canvas_button_2.config(bg="black",fg="white")
    File=open(r"Works/Past_Data.ic","r")
    R=eval((File.read()).strip())
    File.close()
    Activity,colour_list,Precision_List,[CANVAS_SIDE,Number,x_shift,y_shift,Dark_value,B_G,F_G,axis_1,axis_2,m_switch]=R[0]
    BG=B_G
    DIV=(CANVAS_SIDE/2)/Number
    Variable.set(int(Number))
    
    if Dark_value==1:
        ON()
    else:
        OFF()
    B_G=BG
        
    canvas_number=1
    if m_switch==False:
        L1=Label(EnterSpace,text="f(x)=",font="rockwell "+str(21+Font_Increase)+" bold",bg="black",fg="white",width="5",height="2").grid(row=0,column=0,sticky="W")
        window.title("Plotter Space(X-Y)")
    else:
        L1=Label(EnterSpace,text="f(y)=",font="rockwell "+str(21+Font_Increase)+" bold",bg="black",fg="white",width="5",height="2").grid(row=0,column=0,sticky="W")
        window.title("Plotter Space(Y-X)")
    refresh()  
def canvas_2():
    Update_Canvas_Data()
    global Activity,colour_list,Precision_List,canvas_number,CANVAS_SIDE,DIV,x_shift,y_shift,B_G,F_G,Variable,Number,Dark_value,axis_1,axis_2,m_switch
    canvas_button_1.config(bg="black",fg="white")
    canvas_button_2.config(bg="red",fg="white")
    File=open(r"Works/Past_Data.ic","r")
    R=eval((File.read()).strip())
    File.close()
    Activity,colour_list,Precision_List,[CANVAS_SIDE,Number,x_shift,y_shift,Dark_value,B_G,F_G,axis_1,axis_2,m_switch]=R[1]
    BG=B_G
    DIV=(CANVAS_SIDE/2)/Number
    Variable.set(int(Number))   
    
    if Dark_value==1:
        ON()
    else:
        OFF()
    B_G=BG    
    canvas_number=2
    if m_switch==False:
        L1=Label(EnterSpace,text="f(x)=",font="rockwell "+str(21+Font_Increase)+" bold",bg="black",fg="white",width="5",height="2").grid(row=0,column=0,sticky="W")
        window.title("Plotter Space(X-Y)")
    else:
        L1=Label(EnterSpace,text="f(y)=",font="rockwell "+str(21+Font_Increase)+" bold",bg="black",fg="white",width="5",height="2").grid(row=0,column=0,sticky="W")
        window.title("Plotter Space(Y-X)")
    refresh()
def Update_Canvas_Data():
    File=open(r"Works/Past_Data.ic","r")
    R=eval((File.read()).strip())
    File.close()
    R[canvas_number-1]=[Activity,colour_list,Precision_List,[CANVAS_SIDE,Number,x_shift,y_shift,Dark_value,B_G,F_G,axis_1,axis_2,m_switch]]
    File=open(r"Works/Past_Data.ic","w")
    File.write(str(R))
    File.close()
def Final_Processing():
    message=messagebox.askyesnocancel("Note!","Do you want to save changes to I-Grapher")
    if message==True:
        Update_Canvas_Data()
        window.destroy()
    elif message==None:
        pass
    else:
        os.remove(r"Works/Past_Data.ic")
        window.destroy()


############### CANVAS, VARIABLES AND WINDOW-1 ###############################

### Create Window/Canvas According to Display ###

window=Tk()
WIDTH,HEIGHT=window.winfo_screenwidth(),int(window.winfo_screenheight())-30
window.geometry("".join([str(WIDTH),"x",str(HEIGHT),"+0+0"]))
window.title("Plotter Space(X-Y)")
try:
    window.iconbitmap(r"logo.ico")
except:
    message=messagebox.showinfo("Warning!","Assigned Logo Missing",icon="warning")
    
CANVAS_SIDE,user,password=HEIGHT,"root","admin"
DIV,Marker_List,Plotter_List=CANVAS_SIDE/20,["sandybrown","dodgerblue","slateblue"],["blue2","gold","violetred"]
Effect_variable , Screen_Variable , canvas_number , Flip , Escape_switch , Font_Increase , M_PEN_SIZE  , Set_Variable, axis_1           , axis_2    , x_shift , y_shift  , Stop_variable  , scale_constant , DELTA  , B_G        , F_G      , MY_SWITCH_value  , m_switch , switch , Marker_Pen   , Plotter_Pen , Precision_List, Activity, colour_list , scale, scale_max , pos_1         , pos_2         , Precision , Number , Dark_value, TXT1                 , TXT2                    , i=\
0               , 0               , 1             , 0    , 0             , 0             , "2"         , 0           , "dark turquoise" , "brown1"  , 0       , 0        , False          , 2              , 10     , "grey100"  , "grey18" , '0'              , False    , True   , "sandybrown" , "blue2"     , []            , []      , []          , 0    , 9         , CANVAS_SIDE/2 , CANVAS_SIDE/2 , 0.1       , 10     , 0         , (CANVAS_SIDE/2)/DIV  , -((CANVAS_SIDE/2)/DIV)  , 0
window.configure(background="grey63")
Canvas_Main=Frame(window)
canvas=Canvas(Canvas_Main,width=CANVAS_SIDE+20,height=CANVAS_SIDE,bg=B_G)
canvas.pack(side="bottom")
Canvas_Select_Frame=Frame(Canvas_Main,background="grey63",height="30")
Canvas_Select_Frame.pack(side="top",fill="x")
canvas_button_1=Button(Canvas_Select_Frame,text="Canvas 1",bg="red",fg="white",font="Rockwell 10 bold",relief="raised",command=canvas_1)
canvas_button_1.grid(row=0,column=0)
canvas_button_2=Button(Canvas_Select_Frame,text="Canvas 2",bg="black",fg="white",font="Rockwell 10 bold",relief="raised",command=canvas_2)
canvas_button_2.grid(row=0,column=1)

while i<(CANVAS_SIDE/DIV):
    canvas.create_line(i*DIV,0,i*DIV,CANVAS_SIDE,width=1,fill=F_G)
    canvas.create_text(CANVAS_SIDE+10,i*DIV,text=round(float(TXT1),1),fill="red2",font="times "+str(7+Font_Increase)+" bold")
    canvas.create_text(i*DIV,10,text=round(float(TXT2),1),fill="red2",font="times "+str(7+Font_Increase)+" bold",angle=90)
    canvas.create_line(0,i*DIV,CANVAS_SIDE,i*DIV,width=1,fill=F_G)
    TXT1-=1
    TXT2+=1
    i+=1      
        
canvas.create_line(0,CANVAS_SIDE/2-y_shift*DIV,CANVAS_SIDE,CANVAS_SIDE/2-y_shift*DIV,width=3,fill=axis_1)
canvas.create_line(CANVAS_SIDE/2+x_shift*DIV,0,CANVAS_SIDE/2+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)

#################### Secondary 4 Buttons (SECTION A) #########################

### Clear Actvity and Colour list With Fresh Canvas ###

def clear():
    global Activity,scale,colour_list,Precision_List
    canvas.delete("all")
    canvas.config(width=CANVAS_SIDE+20,height=CANVAS_SIDE,bg=B_G)
    canvas.configure(background=B_G)
    TXT1=(CANVAS_SIDE/2)/DIV-y_shift
    TXT2=-((CANVAS_SIDE/2)/DIV+x_shift)
    i=0
    while i<(CANVAS_SIDE/DIV):
        canvas.create_line(i*DIV,0,i*DIV,CANVAS_SIDE,width=1,fill=F_G)
        canvas.create_text(CANVAS_SIDE+10,i*DIV,text=round(float(TXT1),1),fill="red2",font="times "+str(7+Font_Increase)+" bold")
        canvas.create_text(i*DIV,10,text=round(float(TXT2),1),fill="red2",font="times "+str(7+Font_Increase)+" bold",angle=90)
        canvas.create_line(0,i*DIV,CANVAS_SIDE,i*DIV,width=1,fill=F_G)
        TXT1-=1
        TXT2+=1
        i+=1        
    
    canvas.create_line(0,CANVAS_SIDE/2-y_shift*DIV,CANVAS_SIDE,CANVAS_SIDE/2-y_shift*DIV,width=3,fill=axis_1)
    canvas.create_line(CANVAS_SIDE/2+x_shift*DIV,0,CANVAS_SIDE/2+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)
    End()
    Activity,colour_list,scale,Pseudo_List,Precision_List=[],[],0,[],[]
    for widget in F_Toggle.winfo_children():
        Pseudo_List.append(widget)

### To Invert the Variable used ###

def invert():
    global axis_1,axis_2
    axis_1,axis_2=axis_2,axis_1
    global m_switch
    if m_switch==False:
        m_switch=True
        L1=Label(EnterSpace,text="f(y)=",font="rockwell "+str(21+Font_Increase)+" bold",bg="black",fg="white",width="5",height="2").grid(row=0,column=0,sticky="W")
        window.title("Plotter Space(Y-X)")
    else:
        m_switch=False
        L1=Label(EnterSpace,text="f(x)=",font="rockwell "+str(21+Font_Increase)+" bold",bg="black",fg="white",width="5",height="2").grid(row=0,column=0,sticky="W")
        window.title("Plotter Space(X-Y)")
    canvas.create_line(0,CANVAS_SIDE/2-y_shift*DIV,CANVAS_SIDE,CANVAS_SIDE/2-y_shift*DIV,width=3,fill=axis_1)
    canvas.create_line(CANVAS_SIDE/2+x_shift*DIV,0,CANVAS_SIDE/2+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)

### To Undo An Activity On The Canvas ###

def undo():
    global Activity,colour_list,Precision_List
    for i in range(len(Activity)):
        try:
            if len(Activity[i])==6 and Activity[i][-1]=="Freedraw":
                Activity.pop(i)
                colour_list.pop(i)
                Precision_List(i)
        except:
            pass
    try:
        Activity.pop()
    except:
        pass
    refresh()
    try:
        colour_list.pop()
        Precision_List.pop()
    except:
        pass
    
### Substitute A Given Equation With A Given Value and Solving ###
 
def substitute():
    global Sub,F_ONE,LB3,LB4
    def Close():
        try:
            F_ONE.destroy()
            LB3.destroy()
            LB4.destroy()
        except:
            pass
    Close()
    def substitute_1():
        try:
            first=E1.get(1.0,"end").split("\n")[0]
            first=first.replace("=","")
            value_given=Sub.get()
            second=""
            if "x" in first:
                second=first.replace("x","("+str(value_given)+")")
            if "y" in first:
                second=first.replace("y","("+str(value_given)+")")
            first=first.rstrip()
            box=first
            if "x" in box:
                box=box.replace("x","("+str(value_given)+")")
            if "y" in box:
                box=box.replace("y","("+str(value_given)+")")
                
            box=box.replace("^","**")
            box=box.replace("sin(","math.sin(")
            box=box.replace("cos(","math.cos(")
            box=box.replace("tan(","math.tan(")
            box=box.replace("cot(","1/math.tan(")
            box=box.replace("cosec(","1/math.sin(")
            box=box.replace("sec(","1/math.cos(")
            box=box.replace("log10(","math.log10(")
            box=box.replace("log(","math.log(")

            box=box.replace("tan-1(","math.atan(")
            box=box.replace("sin-1(","math.asin(")
            box=box.replace("cos-1(","math.acos(")
                    
            box=box.replace("cosec-1(","math.asin(1/")
            box=box.replace("sec-1(","math.acos(1/")
            box=box.replace("cot-1(","math.atan(1/")
            
            box=box.replace("e","(math.e)")
            box=box.replace("π","(math.pi)")
            for i in range(len(box)-1):
                
                    if ((box[i].isdigit() and box[i+1]=="(" and box[i-2]!="g") or (box[i].isdigit() and box[i+1]=="m") or (box[i]==")" and box[i+1]=="[") or (box[i]=="]" and box[i+1]=="[") or (box[i]=="]" and box[i+1]=="m") or (box[i]==")" and box[i+1]=="m") or ((box[i]=="x" or box[i]=="y") and box[i+1]=="m") or ((box[i]=="x" or box[i]=="y") and box[i+1]=="(") or (box[i]==")" and (box[i+1]=="x" or box[i+1]=="y")) or (box[i]==")" and box[i+1]=="(") or (box[i].isdigit() and (box[i+1]=="x" or box[i]=="y")) or (box[i].isdigit() and box[i+1]=="π")):
                        string1,string2=box[0:i+1],box[i+1:len(box)+1]
                        box="".join([string1,"*",string2])
            i=0
            while i<len(box):
                try:
                    index1=box.index("[")
                    box=box[0:index1]+"abs("+box[index1+1:len(box)+1]

                    index2=box.index("]")
                    box=box[0:index2]+")"+box[index2+1:len(box)+1]
                except:
                    pass
                i+=1

            final_value=eval(box)
            E1.delete(0.0,END)
            E1.insert(0.0,first+"\n"+"="+second+"\n"+"="+str(final_value))
            
        except:
            E1.delete(0.0,END)
            E1.insert(0.0,first+"\n"+" INVALID VALUE ")
        
    def Close():
        try:
            F_ONE.destroy()
            LB3.destroy()
            LB4.destroy()
        except:
            pass
    
    F_ONE=Frame(window1,bg=B_G)
    Sub=Entry(F_ONE,font="Times "+str(18+Font_Increase)+"",width="15",bd="6",justify="center")
    Sub.grid(row=0,column=0)
    sub_b1=Button(F_ONE,text="FIND",font="rockwell "+str(12+Font_Increase)+" bold italic",bg="red",fg="white",relief="raised",command=substitute_1).grid(row=0,column=1)
    done=Button(F_ONE,text="close(↕)",font="rockwell "+str(12+Font_Increase)+" bold italic",bg="SlateBlue2",fg="white",relief="raised",command=Close).grid(row=0,column=2)
    F_ONE.grid(row=7,column=0,columnspan=2)
    if B_G=="grey18":
        LB3=Label(window1,text="",bg="grey18")
    else:
        LB3=Label(window1,text="",bg="seashell2")
    LB3.grid(row=8,column=0,columnspan=3)
    LB4=Label(window1,text="__________Substitute for f(x) or f(y) Here________",bg="seashell2",font="rockwell "+str(9+Font_Increase)+" bold")
    LB4.grid(row=9,column=0,columnspan=3)

#########################  BINDS, CLICKS AND KEYS FUNCTIONS (SECTION B) ######

### Gateway To Prevent Undesired High Precision Equation Computation or Blank Equation ###
    
def gateway(pseudo=1):
    if "X" in E1.get(1.0,"end").strip() or "Y" in E1.get(1.0,"end").strip():
        messagebox.showinfo("Note!","Only Lower Case 'x' and 'y' can be used in Function")
    else:
        if Precision<=0.001:
            if Precision<=0.00001:
                message=messagebox.askquestion("Warning!","Do you want to proceed with MAX Precision, Warning: Only for Higher-End-Processors, Click No to Abort",icon="warning")
                if message=="yes":
                    execute()
            else:
                message=messagebox.askquestion("Warning!","Do you want to proceed with high precision, Warning: Generating Higher Density-Graphs may cause the program to slow down. Click No to go back",icon="warning")
                if message=="yes":
                    execute()
        else:
            if E1.get(1.0,"end").strip()=="":
                E1.config(bg="pink")
            else:
                E1.config(bg="white")
                execute()
            
### Execute Performs According to Given Precision and Domain Range To Find Independent Set of Points and Plot ###

def execute():
    global scale,List,Activity,Loading,colour_list,Stop_variable,Precision_List,Data_Dictionary
    Stop_variable=False
    if Check.get()==1:
        Stop_process=Button(Progress_Frame,text="✕",font="Rockwell "+str(12+Font_Increase)+" bold",bg="red3",fg="white",width="3",relief="raised",bd="5",command=STOP_PROCESS)
        Stop_process.grid(row=0,column=1,sticky="W")
    if scale<=scale_max and scale!=0:
        for i in range(scale): canvas.scale("all",pos_1,pos_2,(1/scale_constant),(1/scale_constant))

    canvas.update_idletasks()
    Loading["value"],Pen=10,Plotter_Pen
    Loading.update_idletasks()
    HALF_SIDE,POINTS=CANVAS_SIDE/2,(CANVAS_SIDE/2)/DIV
    if "," not in E1.get(1.0,"end") or "x" in E1.get(1.0,"end") or "y" in E1.get(1.0,"end"):
        if m_switch==False:
                z=E1.get(1.0,"end").strip()
                V=z
                z=z.replace("^","**")
                z=z.replace("sin(","math.sin(")
                z=z.replace("cos(","math.cos(")
                z=z.replace("tan(","math.tan(")
                z=z.replace("cot(","1/math.tan(")
                z=z.replace("cosec(","1/math.sin(")
                z=z.replace("sec(","1/math.cos(")
                z=z.replace("log10(","math.log10(")
                z=z.replace("log(","math.log(")

                z=z.replace("tan-1(","math.atan(")
                z=z.replace("sin-1(","math.asin(")
                z=z.replace("cos-1(","math.acos(")
                        
                z=z.replace("cosec-1(","math.asin(1/")
                z=z.replace("sec-1(","math.acos(1/")
                z=z.replace("cot-1(","math.atan(1/")

                z=z.replace("e","(math.e)")
                z=z.replace("π","(math.pi)")

                index1,index2,i=0,0,0
                while i<len(z)-1:
                        
                    if ((z[i]=="x" and z[i+1]=="1") or (z[i]==")" and z[i+1]=="m") or (z[i].isdigit() and z[i+1]=="[") or (z[i]=="x" and z[i+1]=="[") or (z[i]=="]" and z[i+1]=="m") or (z[i]==")" and z[i+1]=="[") or (z[i]=="]" and z[i+1]=="[") or (z[i].isdigit() and z[i+1]=="(" and z[i-2]!="g") or (z[i].isdigit() and z[i+1]=="m") or (z[i]=="x" and z[i+1]=="m") or (z[i]=="x" and z[i+1]=="(") or (z[i]==")" and z[i+1]=="x") or (z[i]==")" and z[i+1]=="(") or (z[i].isdigit() and z[i+1]=="x") or (z[i].isdigit() and z[i+1]=="π")):
                        string1,string2=z[0:i+1],z[i+1:len(z)+1]
                        z="".join([string1,"*",string2])
                    i+=1
                i=0
                while i<len(z):
                    try:
                        index1=z.index("[")
                        z=z[0:index1]+"abs("+z[index1+1:len(z)+1]

                        index2=z.index("]")
                        z=z[0:index2]+")"+z[index2+1:len(z)+1]
                    except:
                        pass
                    i+=1
            
                halfcode=z                
                if "," not in halfcode:
                    try:
                        i,l,Initiate=((CANVAS_SIDE/2)/DIV)-x_shift,[],True
                        while Initiate:
                            try:
                                x=i
                                y=eval(halfcode)
                                l.extend([DIV*(x+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(y+y_shift)]) 
                                i=round(i-Precision,5)                                
                                Initiate=False
                            except:
                                if i>-(HALF_SIDE/DIV+Precision+x_shift):
                                    i=round(i-Precision,5)
                                else:
                                    Initiate=False

                        while i>-(POINTS+Precision+x_shift):
                            if i==0-x_shift:                        
                                Loading["value"]=50
                                Loading.update_idletasks()
                                canvas.update_idletasks()
                            try:
                                x=i
                                y=eval(halfcode)
                                l.extend([DIV*(x+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(y+y_shift)])
                                i=round(i-Precision,5)                                
                                canvas.create_line(l,width="2",fill=Pen)
                                del(l[0],l[0])
                                if Check.get()==1:
                                    canvas.update_idletasks()
                                    Stop_process.update()
                                    if Stop_variable:
                                        break
                            except:
                                Initiate=True
                                del(l[0],l[0])
                                while Initiate:
                                    try:
                                        x=i
                                        y=eval(halfcode)
                                        l.extend([DIV*(x+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(y+y_shift)]) 
                                        i=round(i-Precision,5)                                
                                        Initiate=False
                                    except:
                                        if i>-(HALF_SIDE/DIV+Precision+x_shift):
                                            i=round(i-Precision,5)
                                        else:
                                            Initiate=False
                            
                        Loading["value"]=100
                        Loading.update_idletasks()
                        canvas.update_idletasks()      
                    except:
                        pass
                    if i!=(POINTS-x_shift): 
                        Activity.append(halfcode+"(x)")
                        colour_list.append(Plotter_Pen)
                        Precision_List.append(Precision)
                        file=open(r"Works/Equations.ic","a",encoding="utf-8")
                        file.write("`~=` "+V.rstrip()+"\n")
                        file.close()
                        if MY_SWITCH_value=='1':
                            try:
                                query="insert into Equation values(%s)"
                                cur.execute(query,(V,))
                            except:
                                pass
                else:
                    try:
                        halfcode=halfcode.rstrip()
                        Z=halfcode
                        halfcode=halfcode[1:len(halfcode)-1]
                        Cord_x,Cord_y=halfcode.split(",")
                        i,l,Initiate=POINTS-x_shift,[],True
                        while Initiate:
                            try:
                                x=i
                                X_C=eval(Cord_x)
                                Y_C=eval(Cord_y)
                                l.extend([DIV*(X_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(Y_C+y_shift)]) 
                                i=round(i-Precision,5)
                                Initiate=False
                            except:
                                if i>-(POINTS+Precision+x_shift):
                                    i=round(i-Precision,5)
                                else:
                                    Initiate=False
                                
                        while i>-(POINTS+Precision+x_shift):
                            if i==0-x_shift:                        
                                Loading["value"]=50
                                Loading.update_idletasks()
                                canvas.update_idletasks()
                            try:
                                x=i
                                X_C=eval(Cord_x)
                                Y_C=eval(Cord_y)
                                l.extend([DIV*(X_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(Y_C+y_shift)]) 
                                i=round(i-Precision,5)
                                canvas.create_line(l,width="2",fill=Pen)
                                del(l[0],l[0])
                                if Check.get()==1:
                                    canvas.update_idletasks()
                                    Stop_process.update()
                                    if Stop_variable:
                                        break             
                            except:
                                Initiate=True
                                del(l[0],l[0])
                                while Initiate:
                                    try:
                                        x=i
                                        X_C=eval(Cord_x)
                                        Y_C=eval(Cord_y)
                                        l.extend([DIV*(X_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(Y_C+y_shift)]) 
                                        i=round(i-Precision,5)
                                        Initiate=False
                                    except:
                                        if i>-(POINTS+Precision+x_shift):
                                            i=round(i-Precision,5)
                                        else:
                                            Initiate=False
                        Loading["value"]=100
                        Loading.update_idletasks()        
                        canvas.update_idletasks()
                    except:
                        pass
                    if i!=POINTS-x_shift: 
                        Activity.append(Z)
                        colour_list.append(Plotter_Pen)
                        Precision_List.append(Precision)
                        file=open(r"Works/Equations.ic","a",encoding="utf-8")
                        file.write("`~=` "+V.rstrip()+"\n")
                        file.close()
                        if MY_SWITCH_value=='1':
                            try:
                                query="insert into Equation values(%s)"
                                cur.execute(query,(V,))
                            except:
                                pass
        else:
            z=E1.get(1.0,"end").strip()
            V=z
            z=z.replace("^","**")
            z=z.replace("sin(","math.sin(")
            z=z.replace("cos(","math.cos(")
            z=z.replace("tan(","math.tan(")
            z=z.replace("cot(","1/math.tan(")
            z=z.replace("cosec(","1/math.sin(")
            z=z.replace("sec(","1/math.cos(")
            z=z.replace("log10(","math.log10(")
            z=z.replace("log(","math.log(")

            z=z.replace("tan-1(","math.atan(")
            z=z.replace("sin-1(","math.asin(")
            z=z.replace("cos-1(","math.acos(")
                        
            z=z.replace("cosec-1(","math.asin(")
            z=z.replace("sec-1(","math.acos(")
            z=z.replace("cot-1(","math.atan(")
                        
            z=z.replace("e","(math.e)")
            z=z.replace("π","(math.pi)")
            i=0  
            while i<(len(z)-1):
                            
                    if ((z[i]=="y" and z[i+1]=="1") or (z[i]==")" and z[i+1]=="m") or (z[i].isdigit() and z[i+1]=="[") or (z[i]=="y" and z[i+1]=="[") or (z[i]=="]" and z[i+1]=="m") or (z[i]==")" and z[i+1]=="[") or (z[i]=="]" and z[i+1]=="[") or(z[i].isdigit() and z[i+1]=="(" and z[i-2]!="g") or (z[i].isdigit() and z[i+1]=="m") or (z[i]=="y" and z[i+1]=="m") or (z[i]=="y" and z[i+1]=="(") or (z[i]==")" and z[i+1]=="y") or (z[i]==")" and z[i+1]=="(") or (z[i].isdigit() and z[i+1]=="y") or (z[i].isdigit() and z[i+1]=="π")):
                        string1,string2=z[0:i+1],z[i+1:len(z)+1]
                        z="".join([string1,"*",string2])
                    i+=1
            i=0
            while i<len(z):
                try:
                    index1=z.index("[")
                    z=z[0:index1]+"abs("+z[index1+1:len(z)+1]

                    index2=z.index("]")
                    z=z[0:index2]+")"+z[index2+1:len(z)+1]        
                except:
                    pass
                i+=1
            halfcode=z
            if "," not in halfcode:
                try:
                    i,l,Initiate=POINTS-y_shift,[],True
                    while Initiate:
                        try:
                            y=i
                            x=eval(halfcode)
                            l.extend([HALF_SIDE+DIV*(x+x_shift),HALF_SIDE-DIV*(y+y_shift)]) 
                            i=round(i-Precision,5)
                            Initiate=False
                        except:
                            if i>-(POINTS+Precision+y_shift):
                                    i=round(i-Precision,5)
                            else:
                                Initiate=False
                            
                    while i>-(POINTS+Precision+y_shift):
                        if i==0-y_shift:                        
                            Loading["value"]=50
                            Loading.update_idletasks()
                            canvas.update_idletasks()
                        try:
                            y=i
                            x=eval(halfcode)
                            l.extend([HALF_SIDE+DIV*(x+x_shift),HALF_SIDE-DIV*(y+y_shift)]) 
                            i=round(i-Precision,5)
                            canvas.create_line(l,width="2",fill=Pen)
                            del(l[0],l[0])
                            if Check.get()==1:
                                canvas.update_idletasks()
                                Stop_process.update()
                                if Stop_variable:
                                    break
                        except:
                            Initiate=True
                            del(l[0],l[0])
                            while Initiate:
                                try:
                                    y=i
                                    x=eval(halfcode)
                                    l.extend([HALF_SIDE+DIV*(x+x_shift),HALF_SIDE-DIV*(y+y_shift)]) 
                                    i=round(i-Precision,5)
                                    Initiate=False
                                except:
                                    if i>-(POINTS+Precision+y_shift):
                                            i=round(i-Precision,5)
                                    else:
                                        Initiate=False
                                
                    Loading["value"]=100
                    Loading.update_idletasks()
                    canvas.update_idletasks()
                except:
                    pass
                if i!=(POINTS-y_shift): 
                    Activity.append(halfcode+"(y)")
                    colour_list.append(Plotter_Pen)
                    Precision_List.append(Precision)
                    file=open(r"Works/Equations.ic","a",encoding="utf-8")
                    file.write("`~=` "+V.rstrip()+"\n")
                    file.close()
                    if MY_SWITCH_value=='1':
                        try:
                            query="insert into Equation values(%s)"
                            cur.execute(query,(V,))
                        except:
                            pass
            else:
                try:
                    halfcode=halfcode.strip()
                    Z=halfcode
                    halfcode=halfcode[1:len(halfcode)-1]
                    Cord_x,Cord_y=halfcode.split(",")
                    i,l,Initiate=POINTS-y_shift,[],True
                    while Initiate:
                        try:
                            y=i
                            X_C=eval(Cord_x)
                            Y_C=eval(Cord_y)
                            l.extend([DIV*(Y_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(X_C+y_shift)])
                            i=round(i-Precision,5)
                            Initiate=False
                        except:
                            if i>-(POINTS+Precision+y_shift):
                                i=round(i-Precision,5)
                            else:
                                Initiate=False
                            
                    while i>-(POINTS+Precision+y_shift):
                        if i==0-y_shift:                        
                            Loading["value"]=50
                            Loading.update_idletasks()
                            canvas.update_idletasks()
                        try:
                            y=i
                            X_C=eval(Cord_x)
                            Y_C=eval(Cord_y)
                            l.extend([DIV*(Y_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(X_C+y_shift)]) 
                            i=round(i-Precision,5)
                            canvas.create_line(l,width="2",fill=Pen)
                            del(l[0],l[0])
                            if Check.get()==1:
                                canvas.update_idletasks()
                                Stop_process.update()
                                if Stop_variable:
                                    break                      
                        except:
                            Initiate=True
                            del(l[0],l[0])
                            while Initiate:
                                try:
                                    y=i
                                    X_C=eval(Cord_x)
                                    Y_C=eval(Cord_y)
                                    l.extend([DIV*(Y_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(X_C+y_shift)])
                                    i=round(i-Precision,5)
                                    Initiate=False
                                except:
                                    if i>-(POINTS+Precision+y_shift):
                                        i=round(i-Precision,5)
                                    else:
                                        Initiate=False
                    Loading["value"]=100        
                    canvas.update_idletasks()
                    Loading.update_idletasks()
                except:
                    pass
                if i!=(POINTS-y_shift): 
                    Activity.append(Z)
                    colour_list.append(Plotter_Pen)
                    Precision_List.append(Precision)
                    file=open(r"Works/Equations.ic","a",encoding="utf-8")
                    file.write("`~=` "+V.rstrip()+"\n")
                    file.close()
                    if MY_SWITCH_value=='1':
                        try:
                            query="insert into Equation values(%s)"
                            cur.execute(query,(V,))
                        except:
                            pass
    else:
        if m_switch==False:
            try:
                z=E1.get(1.0,"end").strip()
                z=z.replace(" ","")
                z=z.replace("\n","")
                V=z
                z=eval("".join(["[",z,"]"]))
                Semicode=z
                for i in z:
                    X,Y,Radii=HALF_SIDE+DIV*(i[0]+x_shift),HALF_SIDE-DIV*(i[1]+y_shift),40/Number
                    canvas.create_oval(X-Radii,Y-Radii,X+Radii,Y+Radii,fill="red")
                    try:
                        canvas.create_line(X1,Y1,X,Y,width="2",fill=Pen)
                        X1=X
                        Y1=Y
                    except:
                        X1=X
                        Y1=Y
                Semicode.insert(0,Pen)
                Semicode.insert(1,"x")
                Activity.append(Semicode)
                colour_list.append("")
                Precision_List.append("")
            except:
                pass
        else:
            try:
                z=E1.get(1.0,"end").strip()
                z=z.replace(" ","")
                z=z.replace("\n","")
                V=z
                z=eval("".join(["[",z,"]"]))
                Semicode=z
                for i in z:
                    X,Y,Radii=HALF_SIDE+DIV*(i[1]+x_shift),HALF_SIDE-DIV*(i[0]+y_shift),40/Number
                    canvas.create_oval(X-Radii,Y-Radii,X+Radii,Y+Radii,fill="red")
                    try:
                        canvas.create_line(X1,Y1,X,Y,width="2",fill=Pen)
                        X1=X
                        Y1=Y
                    except:
                        X1=X
                        Y1=Y

                Semicode.insert(0,Pen)
                Semicode.insert(1,"y")
                Activity.append(Semicode)
                colour_list.append("")
                Precision_List.append("")
            except:
                pass
            
        file=open(r"Works/Equations.ic","a",encoding="utf-8")
        file.write("`~=` "+V.rstrip()+"\n")
        file.close()
        if MY_SWITCH_value=='1':
            try:
                query="insert into Equation values(%s)"
                cur.execute(query,(V,))
            except:
                pass

    for i in range(scale): canvas.scale("all",pos_1,pos_2,scale_constant,scale_constant)
    try:
        Stop_process.destroy()
    except:
        pass
    Loading["value"]=100                
    canvas.update_idletasks()
    Loading.update_idletasks()

### To Not Show Pen/Line When Mouse Moves Away From Canvas ###

def cursor_out(delete):
    try:
        canvas.delete(motion_line)
        canvas.delete(pen)
    except:
        pass

### To Zoom in and Out of The Canvas ###

def scroll(wheel):
    global scale,pos_1,pos_2,circle
    if scale==0:
        pos_1,pos_2=wheel.x,wheel.y
        
    if wheel.delta<0 and scale>0:
        canvas.scale("all",pos_1,pos_2,1/(scale_constant),1/(scale_constant))
        scale-=1
        try:
            canvas.delete(circle)
            x2,y2,x3,y3=x1-4,y1-4,x1+4,y1+4
            circle=canvas.create_oval(x2,y2,x3,y3,fill="red")
        except:
            pass
    if wheel.delta>0 and scale<scale_max:
        canvas.scale("all",pos_1,pos_2,scale_constant,scale_constant)
        scale+=1
        try:
            canvas.delete(circle)
            x2,y2,x3,y3=x1-3,y1-3,x1+3,y1+3
            circle=canvas.create_oval(x2,y2,x3,y3,fill="red")
        except:
            pass

### To Draw Straight Lines and Doodle On Canvas ###
    
def line1(event):
    global X,Y,Activity
    try:
        line1=canvas.create_line(x1,y1,event.x,event.y,width=M_PEN_SIZE,fill=Marker_Pen)
        Activity.append([x1,y1,event.x,event.y,scale,pos_1,pos_2,Marker_Pen,M_PEN_SIZE])
        colour_list.append("")
        Precision_List.append("")
        End()
    except:
        pass
    try:
        def release(default):
            canvas.unbind("<Motion>")
            Freedraw.extend([M_PEN_SIZE,scale,pos_1,pos_2,Marker_Pen,"Freedraw"])
            Activity.append(Freedraw)
            colour_list.append("")
            Precision_List.append("")
        Freedraw=[]
        try:
            del(X)
            del(Y)
        except:
            pass
        def Mot(M):
            global X,Y
            try:
                canvas.create_line(X,Y,M.x,M.y,width=M_PEN_SIZE,fill=Marker_Pen)
                X,Y=M.x,M.y
                Freedraw.extend([X,Y])    
            except:
                X,Y=M.x,M.y
                Freedraw.extend([X,Y])
                    
        canvas.bind("<Motion>",Mot)
        canvas.bind("<ButtonRelease-1>",release)
    except:
        pass

### To Hide Marked Point/ Coordinates of Cursor While Drawing Straight Lines On Canvas ###    
                
def End(stop=None):
    global circle,x1,y1 
    try:
        del(x1)
        del(y1)
        canvas.delete(circle)
        canvas.delete(pen)
        canvas.delete(motion_line)
        if Screen_Variable==1:
            Coordinate.config(text="")
        else:
            if m_switch==True:
                window.title("Plotter Space(Y-X)")
            else:
                window.title("Plotter Space(X-Y)")
    except:
        pass

### To Mark Starting Point For Straight Line and Show Dotted Line ###

def line2(event):
    global x1,y1,Activity
    x1,y1=event.x,event.y
    x2,y2,x3,y3=x1-3,y1-3,x1+3,y1+3
    global circle
    try:
        canvas.delete(circle)
    except:
        pass
    circle=canvas.create_oval(x2,y2,x3,y3,fill="red")
    def motion(cursor):
        global cursor_x,cursor_y,motion_line,pen
        try:
            canvas.delete(motion_line)
            canvas.delete(pen)
        except:
            pass
        cursor_x,cursor_y=cursor.x,cursor.y
        try:
            if 0<cursor_x<=CANVAS_SIDE and 0<cursor_y<=CANVAS_SIDE:
                motion_line=canvas.create_line(x1,y1,cursor_x,cursor_y,width="2",dash=(1,1),fill=Marker_Pen)
                pen=canvas.create_text(cursor_x-10,cursor_y-10,fill="darkblue",font="Rockwell "+str(20+Font_Increase)+" italic bold",
                        text="✎")
                if Screen_Variable==1:
                    if m_switch==False:
                        Coordinate.config(text="x="+str(round((cursor_x-(CANVAS_SIDE/2))/DIV,3))+","+" y="+str(round((((CANVAS_SIDE/2)-cursor_y)/DIV),3)))
                    else:
                        Coordinate.config(text="y="+str(round((cursor_x-(CANVAS_SIDE/2))/DIV,3))+","+" x="+str(round((((CANVAS_SIDE/2)-cursor_y)/DIV),3)))

                else:
                    if m_switch==False:
                        window.title("x="+str(round((cursor_x-(CANVAS_SIDE/2))/DIV,3))+","+"\ny="+str(round((((CANVAS_SIDE/2)-cursor_y)/DIV),3)))
                        window.update_idletasks()
                    else:
                        window.title("y="+str(round((cursor_x-(CANVAS_SIDE/2))/DIV,3))+","+"\nx="+str(round((((CANVAS_SIDE/2)-cursor_y)/DIV),3)))
                        window.update_idletasks()
            else:
                canvas.delete(motion_line)
                canvas.delete(pen)
        except:
            pass
    window.bind("<Motion>",motion)

def Preview():
    canvas.delete("all")
    canvas.config(width=CANVAS_SIDE+20,height=CANVAS_SIDE,bg=B_G)
    canvas.configure(background=B_G)
    TXT1=(CANVAS_SIDE/2)/DIV-y_shift
    TXT2=-((CANVAS_SIDE/2)/DIV+x_shift)
    i=0
    while i<(CANVAS_SIDE/DIV):
        canvas.create_line(i*DIV,0,i*DIV,CANVAS_SIDE,width=1,fill=F_G)
        canvas.create_text(CANVAS_SIDE+10,i*DIV,text=round(float(TXT1),1),fill="red2",font="times "+str(7+Font_Increase)+" bold")
        canvas.create_text(i*DIV,10,text=round(float(TXT2),1),fill="red2",font="times "+str(7+Font_Increase)+" bold",angle=90)
        canvas.create_line(0,i*DIV,CANVAS_SIDE,i*DIV,width=1,fill=F_G)
        TXT1-=1
        TXT2+=1
        i+=1    
        
    canvas.create_line(0,CANVAS_SIDE/2-y_shift*DIV,CANVAS_SIDE,CANVAS_SIDE/2-y_shift*DIV,width=3,fill=axis_1)
    canvas.create_line(CANVAS_SIDE/2+x_shift*DIV,0,CANVAS_SIDE/2+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)    

### Settings Menu (More Features Better User Interface) ###
    
def triple_click(point=None):
    global Set_Variable,Font_Increase,Font_Size,Drag,InnerFrame,ConfigFrame,Flip,Full_Refresh
    try:
        InnerFrame.destroy()
        Drag.destroy()
        ConfigFrame.destroy()
    except:
        pass
    def SET():
        global Set_Variable
        Exit_Main_Interface()
        Main_Interface()
        if Exit_Variable==1:
            Exit()
        else:
            Exit()
            SideBar()
        refresh()
        Set_Variable=0    
    if Flip==0:
        def SHIFT_RIGHT():
            global x_shift,Set_Variable
            x_shift+=1
            Set_Variable=1
            Preview()
            Shifting_Origin_Label.config(text="Shift Origin\n"+"x: "+str(x_shift)+", y: "+str(y_shift))
        def SHIFT_UP():
            global y_shift,Set_Variable
            y_shift+=1
            Set_Variable=1
            Preview()
            Shifting_Origin_Label.config(text="Shift Origin\n"+"x: "+str(x_shift)+", y: "+str(y_shift))
        def SHIFT_LEFT():
            global x_shift,Set_Variable
            x_shift-=1
            Set_Variable=1
            Preview()
            Shifting_Origin_Label.config(text="Shift Origin\n"+"x: "+str(x_shift)+", y: "+str(y_shift))
        def SHIFT_DOWN():
            global y_shift,Set_Variable
            y_shift-=1
            Set_Variable=1
            Preview()
            Shifting_Origin_Label.config(text="Shift Origin\n"+"x: "+str(x_shift)+", y: "+str(y_shift))
        def Zero():
            global x_shift,y_shift,Set_Variable
            x_shift,y_shift=0,0
            Set_Variable=1
            Preview()
            Shifting_Origin_Label.config(text="Shift Origin\n"+"x: "+str(x_shift)+", y: "+str(y_shift))
        def Reduce():
            global CANVAS_SIDE,DIV,Flip,Set_Variable
            CANVAS_SIDE-=10
            DIV=(CANVAS_SIDE/2)/Variable.get()
            Drag.config(text="Triple Left Click(Close/Open)\n"+"Canvas Side Length: "+str(CANVAS_SIDE))
            Set_Variable=1
            Preview()   
        def Expand():
            global CANVAS_SIDE,DIV,Flip,Set_Variable
            CANVAS_SIDE+=10
            DIV=(CANVAS_SIDE/2)/Variable.get()
            Drag.config(text="Triple Left Click(Close/Open)\n"+"Canvas Side Length: "+str(CANVAS_SIDE))
            Set_Variable=1
            Preview()     
        def Shade(NUMBER):
            global B_G
            B_G="".join(["grey",str(NUMBER)])
            canvas.config(bg=B_G)   
        def Adjust_Pen_Size(VALUE):
            global M_PEN_SIZE
            M_PEN_SIZE=str(VALUE)    
        def Whole_Window_Refresh(VALUE):
            global Font_Increase,Set_Variable,Full_Refresh
            Font_Increase=int(VALUE)
            Set_Variable=1
            Full_Refresh=1         
        def CONFIG():
            global MY_SWITCH_value,ConfigFrame
            if MY_SWITCH.get()=='0':
                try:
                    ConfigFrame.destroy()
                    messagebox.showinfo("Note!","MySql Connection-OFF")
                except:
                    pass
                try:
                    con.close()
                except:
                    pass
            else:
                def Update():
                    global user,password
                    user=Config_E1.get()
                    password=Config_E2.get()
                    A=DBMS()
                    if A=="SUCCESS":
                        ConfigFrame.destroy()
                    if A=="ERROR":
                        messagebox.showinfo("Note!","Change User/Password")
                        
                ConfigFrame=Frame(InnerFrame,bg="black")
                Config_L1=Label(ConfigFrame,text="User:",font="Rockwell "+str(11+Font_Increase)+"",bg="gray1",fg="red",width="10").grid(row=1,column=1)
                Config_L2=Label(ConfigFrame,text="Password:",font="Rockwell "+str(11+Font_Increase)+"",bg="gray1",fg="red",width="10").grid(row=2,column=1)
                Config_E1=Entry(ConfigFrame,font="Rockwell "+str(10+Font_Increase)+" bold")
                Config_E1.insert(0,user)
                Config_E1.grid(row=1,column=2)
                Config_E2=Entry(ConfigFrame,font="Rockwell "+str(10+Font_Increase)+" bold")
                Config_E2.insert(0,password)
                Config_E2.grid(row=2,column=2)
                Config_B=Button(ConfigFrame,text="✓",font="Rockwell "+str(14+Font_Increase)+" bold",bg="black",fg="white",command=Update).grid(row=1,column=3,rowspan=2)
                ConfigFrame.grid(row=11,column=1,columnspan=4)
                
            MY_SWITCH_value=MY_SWITCH.get()
             
        Drag=Label(UpperBar,text="Triple Left Click(Close/Open)\n"+"Canvas Side Length: "+str(CANVAS_SIDE),font="Rockwell "+str(10+Font_Increase)+" bold",bg="black",fg="white",width="25")
        Drag.grid(row=0,column=0,sticky="W")
        InnerFrame=Frame(UpperBar,bg="black")
        SHRINK=Button(InnerFrame,text="Reduce [-]",font="Rockwell "+str(12+Font_Increase)+" bold",bg="midnightblue",fg="white",width="12",command=Reduce).grid(row=1,column=1)
        ENLARGE=Button(InnerFrame,text="Expand [+]",font="Rockwell "+str(12+Font_Increase)+" bold",bg="orange",fg="white",width="12",command=Expand).grid(row=1,column=2)

        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=2,column=1)
        Font_Increase_Label=Label(InnerFrame,text="Font Size Increase",bg="black",fg="red",font="Rockwell "+str(10+Font_Increase)+" bold",anchor="w")
        Font_Increase_Label.grid(row=3,column=1)
        Font_Increase_scale=Scale(InnerFrame,from_="-5",to="15",width="10",orient="horizontal",font="Rockwell "+str(9+Font_Increase)+" bold",bg="black",fg="red",command=Whole_Window_Refresh)
        Font_Increase_scale.grid(row=3,column=2)
        Font_Increase_scale.set(Font_Increase)

        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=4,column=1)
        PEN_SIZE=StringVar()
        M_Config_Label=Label(InnerFrame,text="Marker Size  ",bg="black",fg="white",font="Rockwell "+str(10+Font_Increase)+" bold",anchor="w").grid(row=5,column=1)
        M_Slider=Scale(InnerFrame,from_="1",to="30",width="10",orient="horizontal",font="Rockwell "+str(9+Font_Increase)+" bold",bg="black",fg="white",command=Adjust_Pen_Size)
        M_Slider.grid(row=5,column=2)
        M_Slider.set(M_PEN_SIZE)

        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=6,column=1)
        scale_label=Label(InnerFrame,text="Backlit adjust",font="Rockwell "+str(9+Font_Increase)+" bold",anchor="w",bg="black",fg="white")
        scale_label.grid(row=7,column=1)
        scale=Scale(InnerFrame,from_="100",to="1",width="10",orient="horizontal",font="Rockwell "+str(9+Font_Increase)+" bold",bg="black",fg="white",command=Shade)
        scale.set(B_G[4:])
        scale.grid(row=7,column=2)

        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=8,column=1)
        MY_LB=Label(InnerFrame,text="Mysql-Link",font="Rockwell "+str(10+Font_Increase)+" bold",width="10",fg="white",bg="black",anchor="w").grid(row=9,column=1)
        MY_SWITCH=StringVar()
        MY_SWITCH.set(MY_SWITCH_value)
        MY_CB=Checkbutton(InnerFrame,variable=MY_SWITCH,command=CONFIG,fg="red",bg="black",width="10",font="Rockwell "+str(10+Font_Increase)+" bold",bd="3").grid(row=9,column=2)

        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=10,column=1)
        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=12,column=0)
        
        Shifting_Origin=Frame(InnerFrame,bg="grey",bd="10")
        Shift_right=Button(Shifting_Origin,text="▶",font="Rockwell "+str(6+Font_Increase)+" bold",bg="blue2",fg="white",width="2",bd="5",relief="raised",command=SHIFT_RIGHT)
        Shift_right.grid(row=1,column=2)
        Shift_up=Button(Shifting_Origin,text="▲",font="Rockwell "+str(6+Font_Increase)+" bold",bg="blue2",fg="white",width="2",bd="5",relief="raised",command=SHIFT_UP)
        Shift_up.grid(row=0,column=1)
        Shift_down=Button(Shifting_Origin,text="▼",font="Rockwell "+str(6+Font_Increase)+" bold",bg="blue2",fg="white",width="2",bd="5",relief="raised",command=SHIFT_DOWN)
        Shift_down.grid(row=2,column=1)
        Shift_left=Button(Shifting_Origin,text="◀",font="Rockwell "+str(6+Font_Increase)+" bold",bg="blue2",fg="white",width="2",bd="5",relief="raised",command=SHIFT_LEFT)
        Shift_left.grid(row=1,column=0)
        Shift_Zero=Button(Shifting_Origin,text="◎",font="Rockwell "+str(6+Font_Increase)+" bold",bg="blue2",fg="white",width="2",bd="5",relief="raised",command=Zero)
        Shift_Zero.grid(row=1,column=1)

        Shifting_Origin_Label=Label(InnerFrame,text="Shift Origin\n"+"x: "+str(x_shift)+", y: "+str(y_shift),bg="black",fg="orange",font="Rockwell "+str(13+Font_Increase)+" bold",anchor="w")
        Shifting_Origin_Label.grid(row=13,column=1)
        Shifting_Origin.grid(row=13,column=2)           
       
        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=13,column=0)
        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=14,column=0)
        Shift_Set=Button(InnerFrame,text="APPLY",font="Rockwell "+str(10+Font_Increase)+" bold",bg="red",fg="white",width="6",bd="5",relief="raised",command=SET)
        Shift_Set.grid(row=15,column=1,columnspan=2)
        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=16,column=0)
        Blank=Label(InnerFrame,text=" ",bg="black",fg="black").grid(row=17,column=0)

        InnerFrame.grid(row=3,column=0,columnspan=2)

        Flip=1
        Full_Refresh=0
    else:
        Flip=0
        if Set_Variable==1:
            SET()
        Drag.destroy()
        InnerFrame.destroy()
        try:
            ConfigFrame.destroy()
        except:
            pass
             
#########################  Insert Text Box Buttons (SECTION C)################

def power():
    E1.insert(END,"^")
def pi():
    E1.insert(END,"π")
def log():
    E1.insert(END,"log(")
def log10():
    E1.insert(END,"log10(")
def sin():
    E1.insert(END,"sin(")
def cos():
    E1.insert(END,"cos(")
def tan():
    E1.insert(END,"tan(")
def cosec():
    E1.insert(END,"cosec(")
def sec():
    E1.insert(END,"sec(")
def cot():
    E1.insert(END,"cot(")
def sin_1():
    E1.insert(END,"sin-1(")
def cos_1():
    E1.insert(END,"cos-1(")
def tan_1():
    E1.insert(END,"tan-1(")
def cosec_1():
    E1.insert(END,"cosec-1(")
def sec_1():
    E1.insert(END,"sec-1(")
def cot_1():
    E1.insert(END,"cot-1(")
def CE():
    E1.delete(0.0,END)
def inv_trig():
    global switch
    if switch==True:
        B8=Button(F1,text="sin-1(",command=sin_1,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=3,column=1)
        B9=Button(F1,text="cos-1(",command=cos_1,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=3,column=2)
        B10=Button(F1,text="tan-1(",command=tan_1,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=4,column=1)
        B11=Button(F1,text="cosec-1(",command=cosec_1,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=4,column=2)
        B12=Button(F1,text="sec-1(",command=sec_1,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=5,column=1)
        B13=Button(F1,text="cot-1(",command=cot_1,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=5,column=2)
        switch=False
        B16=Button(F1,text="Trig",command=inv_trig,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=6,column=1)
    else:
        B8=Button(F1,text="sin(",command=sin,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=3,column=1)
        B9=Button(F1,text="cos(",command=cos,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=3,column=2)
        B10=Button(F1,text="tan(",command=tan,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=4,column=1)
        B11=Button(F1,text="cosec(",command=cosec,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=4,column=2)
        B12=Button(F1,text="sec(",command=sec,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=5,column=1)
        B13=Button(F1,text="cot(",command=cot,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=5,column=2)
        switch=True
        B16=Button(F1,text="Inv.Trig",command=inv_trig,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=6,column=1)
def Window():
    global Screen_Variable
    B_Fullscreen.config(text="Fullscreen ⤧",command=FullScreen)
    window.attributes("-fullscreen", False)
    Screen_Variable=0
def FullScreen():
    global Screen_Variable
    window.attributes("-fullscreen", True)
    B_Fullscreen.config(text="Window ⤩",command=Window)
    B_Fullscreen.grid(row=0,column=1)
    Screen_Variable=1
def STOP_PROCESS():
    global Stop_variable
    Stop_variable=True
    
################### LABELS ,BUTTONS ,FRAMES ,BINDINGS ,PROTOCOL AND WINDOW-2 ###########

### Tkinter USER INTERFACE ###
    
window1=Frame(window,bg="seashell2")

def Exit_Main_Interface():
    global Entry_Box_Value
    Entry_Box_Value=E1.get(1.0,"end")
    for i in window1.winfo_children(): i.destroy()

def Main_Interface():
    global UpperBar,Loading,B_Fullscreen,B_Settings,UpperBar,EnterSpace,L1,E1,F1,EnterSpace,Progress_Frame,Main_Frame,L_Adjust,L_Adjust1,L_Adjust2,LB1,B1,B2,B3,B4,B5,B6,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,Flip,Coordinate
    Flip=0
    UpperBar=Frame(window1,bg="black",bd="5",width="33")
    if Screen_Variable==1:
        window.attributes("-fullscreen",True)
        B_Fullscreen=Button(UpperBar,text="Window ⤩",font="Rockwell "+str(9+Font_Increase)+" bold",bg="black",fg="white",width="10",bd="2",command=Window)
        B_Fullscreen.grid(row=0,column=1)
    else:
        window.attributes("-fullscreen", False)
        B_Fullscreen=Button(UpperBar,text="Fullscreen ⤧",font="Rockwell "+str(9+Font_Increase)+" bold",bg="black",fg="white",bd="2",command=FullScreen)
        B_Fullscreen.grid(row=0,column=1,sticky="E")

    B_Settings=Button(UpperBar,text="⚙",font="Rockwell "+str(9+Font_Increase)+" bold",bg="black",fg="white",bd="2",command=triple_click).grid(row=0,column=2,sticky="W")
    Coordinate=Label(UpperBar,font="Rockwell "+str(9+Font_Increase)+" bold",bg="black",fg="white",bd="2")
    Coordinate.grid(row=0,column=0)
    UpperBar.grid(row=0,column=0,columnspan=4,sticky="NE")

    EnterSpace=Frame(window1)
    L1=Label(EnterSpace,text="f(x)=",font="rockwell "+str(21+Font_Increase)+" bold",width=5,height=2,bg="black",fg="white")
    L1.grid(row=0,column=0,sticky="W")
    E1=Text(EnterSpace,font="times "+str(15+Font_Increase)+"",height=4,width=25)
    E1.grid(row=0,column=1)
    try:
        E1.insert(0.0,Entry_Box_Value)
    except:
        pass
    EnterSpace.grid(row=1,column=0,columnspan=2)

    Progress_Frame=Frame(window1)
    Loading=Progressbar(Progress_Frame,orient=HORIZONTAL,length=300,mode='determinate',value=100)
    Loading.grid(row=0,column=0,sticky="E")
    Progress_Frame.grid(row=2,column=0,columnspan=2)

    B1=Button(window1,text="Execute",font="Rockwell "+str(13+Font_Increase)+" bold",bg="red",fg="white",width="28",relief="raised",bd="5",command=gateway).grid(row=3,column=0,columnspan=2,sticky="N")
    
    Main_Frame=Frame(window1,bg="seashell2")
    L_Adjust=Label(Main_Frame,text=" ",bg="seashell2",width="35")
    L_Adjust.grid(row=1,column=0,columnspan=2) 
    B2=Button(Main_Frame,text="""Clear
    Graph ↺""",font="Rockwell "+str(12+Font_Increase)+" bold italic",bg="dodger blue",fg="white",width="9",bd="5",relief="raised",command=clear).grid(row=2,column=0,sticky="W")
    B3=Button(Main_Frame,text="""Invert
    Axis ↑↓""",font="Rockwell "+str(12+Font_Increase)+" bold italic",bg="dodger blue",fg="white",width="9",bd="5",relief="raised",command=invert).grid(row=2,column=1,sticky="E")
    L_Adjust1=Label(Main_Frame,text=" ",bg="seashell2")
    L_Adjust1.grid(row=3,column=1)
    B4=Button(Main_Frame,text="""Undo
    """,font="Rockwell "+str(12+Font_Increase)+" bold italic",bg="dodger blue",fg="white",width="9",bd="5",relief="raised",command=undo).grid(row=4,column=0,sticky="W")
    B5=Button(Main_Frame,text="""Substitute
    """,font="Rockwell "+str(12+Font_Increase)+" bold italic",bg="dodger blue",fg="white",width="9",bd="5",relief="raised",command=substitute).grid(row=4,column=1,sticky="E")
    Main_Frame.grid(row=4,column=0,columnspan=2)

    F1=Frame(window1,bg="black",bd="5",relief="sunken")
    B6=Button(F1,text="^",command=power,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=1,column=1)
    B7=Button(F1,text="π",command=pi,font="Times "+str(12+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=1,column=2)
    B8=Button(F1,text="log(",command=log,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=2,column=1)
    B9=Button(F1,text="log10(",command=log10,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=2,column=2)
    B10=Button(F1,text="sin(",command=sin,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=3,column=1)
    B11=Button(F1,text="cos(",command=cos,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=3,column=2)
    B12=Button(F1,text="tan(",command=tan,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=4,column=1)
    B13=Button(F1,text="cosec(",command=cosec,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=4,column=2)
    B14=Button(F1,text="sec(",command=sec,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="blue",fg="white",width="8",bd="5",relief="raised").grid(row=5,column=1)
    B15=Button(F1,text="cot(",command=cot,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=5,column=2)
    B16=Button(F1,text="Inv.Trig",command=inv_trig,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="orange",fg="white",width="8",bd="5",relief="raised").grid(row=6,column=1)
    B17=Button(F1,text="CE",command=CE,font="Rockwell "+str(11+Font_Increase)+" bold italic",bg="red",fg="white",width="8",bd="5",relief="raised").grid(row=6,column=2)
    L1=Label(F1,text="Functions Panel",font="Rockwell "+str(13+Font_Increase)+" bold italic",bg="brown",fg="white",width="16",bd="5",relief="solid").grid(row=7,column=1,columnspan=2)
    F1.grid(row=5,column=0,columnspan=2)

    L_Adjust2=Label(window1,text="",bg="seashell2")
    L_Adjust2.grid(row=8,column=0)
    LB1=Label(window1,text="_______________________________________________",bg="seashell2")
    LB1.grid(row=6,column=0,columnspan=3)

    if Dark_value==1:
        L_Adjust.config(bg="grey18")
        Main_Frame.config(bg="grey18")
        L_Adjust1.config(bg="grey18")
        window1.config(bg="grey18")
        L_Adjust2.config(bg="grey18")
        LB1.config(bg="grey18")
        try:
            LB3.config(bg="grey18")
        except:
            pass

Main_Interface()

### TO Exit FullScreen and Open Settings/Reduce Canvas Size by Half ###

def Escape(EvE=None):
    global CANVAS_SIDE,DIV,Escape_switch
    if Escape_switch==0:
        CANVAS_SIDE=HEIGHT/2
        DIV=(CANVAS_SIDE/2)/Number
        refresh()
        Escape_switch=1
        Pseudo_List=[]
        for widget in F_Toggle.winfo_children():
            Pseudo_List.append(widget)

    else:
        CANVAS_SIDE=HEIGHT
        DIV=(CANVAS_SIDE/2)/Number
        refresh()
        Escape_switch=0
        Pseudo_List=[]
        for widget in F_Toggle.winfo_children():
            Pseudo_List.append(widget)
    Window()

window.protocol("WM_DELETE_WINDOW",Final_Processing)
window.bind("<Return>",gateway)
window.bind("<Escape>",Escape)
window1.bind("<Motion>",cursor_out)
canvas.bind("<MouseWheel>",scroll)
canvas.bind("<Button-1>",line1)
canvas.bind("<Button-2>",End)
canvas.bind("<Button-3>",line2)
canvas.bind("<Triple-Button-1>",triple_click)

###################### COLOURS SECTION ######################################

### Basic Colour Replacement ###

def ON():
    B_O.config(text="ON",bg="light green",fg="white",command=OFF)
    B_N.config(text="  ",bg="white",fg="black",command=None)
    B_N.grid(row=2,column=1)
    global B_G,F_G,Dark_value
    Dark_value,B_G,F_G=1,"grey18","gray60"
    L_Adjust.config(bg=B_G)
    Main_Frame.config(bg=B_G)
    L_Adjust1.config(bg=B_G)
    window1.config(bg=B_G)
    L_Adjust2.config(bg=B_G)
    LB1.config(bg=B_G)
    try:
        LB3.config(bg=B_G)
    except:
        pass
    Loading["value"]=50
    Loading.update_idletasks()
    canvas.configure(background=B_G)
    TXT1=(CANVAS_SIDE/2)/DIV-y_shift
    TXT2=-((CANVAS_SIDE/2)/DIV+x_shift)
    i=0
    while i<(CANVAS_SIDE/DIV):
        canvas.create_line(i*DIV,0,i*DIV,CANVAS_SIDE,width=1,fill=F_G)
        canvas.create_text(CANVAS_SIDE+10,i*DIV,text=round(float(TXT1),1),fill="red2",font="times "+str(7+Font_Increase)+" bold")
        canvas.create_text(i*DIV,10,text=round(float(TXT2),1),fill="red2",font="times "+str(7+Font_Increase)+" bold",angle=90)
        canvas.create_line(0,i*DIV,CANVAS_SIDE,i*DIV,width=1,fill=F_G)
        TXT1-=1
        TXT2+=1
        i+=1       
        
    canvas.create_line(0,CANVAS_SIDE/2-y_shift*DIV,CANVAS_SIDE,CANVAS_SIDE/2-y_shift*DIV,width=3,fill=axis_1)
    canvas.create_line(CANVAS_SIDE/2+x_shift*DIV,0,CANVAS_SIDE/2+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)
    triple_click()
    triple_click()
    Loading["value"]=100
    Loading.update()
def OFF():
    B_O.config(text="  ",bg="white",fg="black",command=None)
    B_N.config(text="OFF",bg="red",fg="white",command=ON)
    global B_G,F_G,Dark_value
    Dark_value,B_G,F_G,colour=0,"grey100","grey18","seashell2"
    L_Adjust.config(bg=colour)
    Main_Frame.config(bg=colour)
    L_Adjust1.config(bg=colour)
    window1.config(bg=colour)
    L_Adjust2.config(bg=colour)
    LB1.config(bg=colour)
    try:
        LB3.config(bg=colour)
    except:
        pass
    Loading["value"]=50
    Loading.update_idletasks()
    canvas.configure(background=B_G)
    TXT1=(CANVAS_SIDE/2)/DIV-y_shift
    TXT2=-((CANVAS_SIDE/2)/DIV+x_shift)
    i=0
    while i<(CANVAS_SIDE/DIV):
        canvas.create_line(i*DIV,0,i*DIV,CANVAS_SIDE,width=1,fill=F_G)
        canvas.create_text(CANVAS_SIDE+10,i*DIV,text=round(float(TXT1),1),fill="red2",font="times "+str(7+Font_Increase)+" bold")
        canvas.create_text(i*DIV,10,text=round(float(TXT2),1),fill="red2",font="times "+str(7+Font_Increase)+" bold",angle=90)
        canvas.create_line(0,i*DIV,CANVAS_SIDE,i*DIV,width=1,fill=F_G)
        TXT1-=1
        TXT2+=1
        i+=1      
        
    canvas.create_line(0,CANVAS_SIDE/2-y_shift*DIV,CANVAS_SIDE,CANVAS_SIDE/2-y_shift*DIV,width=3,fill=axis_1)
    canvas.create_line(CANVAS_SIDE/2+x_shift*DIV,0,CANVAS_SIDE/2+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)
    triple_click()
    triple_click()
    Loading["value"]=100
    Loading.update()

### To Select Plotter-Pen/ Marker-Pen colour ###
    
def colour_M1():
    global Marker_Pen
    Marker_Pen=Marker_List[0]
    Colour_M1.config(text="❤")
    Colour_M2.config(text=" ")
    Colour_M3.config(text=" ")
def colour_M2():
    global Marker_Pen
    Marker_Pen=Marker_List[1]
    Colour_M1.config(text=" ")
    Colour_M2.config(text="❤")
    Colour_M3.config(text=" ")
def colour_M3():
    global Marker_Pen
    Marker_Pen=Marker_List[2]
    Colour_M1.config(text=" ")
    Colour_M2.config(text=" ")
    Colour_M3.config(text="❤") 

def colour_P1():
    global Plotter_Pen
    Plotter_Pen=Plotter_List[0]
    Colour_P1.config(text="✘")
    Colour_P2.config(text=" ")
    Colour_P3.config(text=" ")
def colour_P2():
    global Plotter_Pen
    Plotter_Pen=Plotter_List[1]
    Colour_P1.config(text=" ")
    Colour_P2.config(text="✘")
    Colour_P3.config(text=" ")
def colour_P3():
    global Plotter_Pen
    Plotter_Pen=Plotter_List[2]
    Colour_P1.config(text=" ")
    Colour_P2.config(text=" ")
    Colour_P3.config(text="✘")
    
####################### Help and Mail Section ########################################

### To Send Email From User For Creator -Using SMTPLIB ###

def MailRelay(Feed):
    message="Subject: "+"Feedback From I-Grapher"+"\n\n"+Feed
    sender_email,rec_email,password="igraphsends@gmail.com","igraphreturns@gmail.com","graph@admin"
    UPLOADS()
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email, rec_email, message)
    server.quit()

### Open Help-Section User Interface and Feedback Mechanism for Creator (User- Files) ### Contains An Algorithm to Search (-Basic Character Matching Algorithm), Scroll Through Labels (-New Approach unlike Traditional Scroll) ###
    
def Help():
    global Help_section,comment_Frame,start,end,row,begin
    try:
        Help_section.destroy()
    except:
        pass
    Help_section=Tk()
    Help_section.title("Help")
    try:
        Help_section.iconbitmap(r"logo.ico")
    except:
        pass
    Back=B_G
    Help_section.configure(background=Back)
    Help_section.geometry("+0+0")
    Help_section.geometry("910x"+str(HEIGHT))
    Instruction=Label(Help_section,text="Comment Section",font="Rockwell "+str(16+Font_Increase)+" bold",bg="midnight blue",fg="white",width="55",height="2",bd="8",relief="raised",justify="left").grid(row=0,column=0)
    Instruction=Label(Help_section,text=" ",bg=Back).grid(row=1,column=0)
    def Show_Instructions():
        for i in range(len(comments)-2):
            try:
                Down_s()
            except:
                pass
    Question=Button(Help_section,text="""How
To
Use?""",font="Rockwell "+str(11+Font_Increase)+" bold",fg="white",bg="red",command=Show_Instructions)
    Question.grid(row=0,column=1)
    
    def Feedback():
        if Name.get()!="Name" and FeedBox.get(1.0,END).rstrip()!="" and Name.get()!="":       
            Name.config(bg="white")
            FeedBox.config(bg="white")
            global comment_Frame,comments
            Alias=Name.get()
            Feed=(Alias+": "+FeedBox.get(1.0,"end")).rstrip()
            Send_Status=Label(Help_section,text="Sending...",font="Rockwell "+str(11+Font_Increase)+" bold",width="8")
            Send_Status.grid(row=2,column=1)
            Help_section.update()
            try:
                MailRelay(Feed)
                Send_Status.config(text="Sent")
            except:
                File=open(r"Works/Uploads.ic","a+")
                File.write(Feed+"`~=`")
                File.close()
                Send_Status.config(text="Drafted")
                
            f=open(r"Works/FeedBack.ic","r")
            R=f.read()
            comments=R.split("`~=`")
            comments.remove("")
            comments.insert(0,Feed)
            f.close()
            f=open(r"Works/FeedBack.ic","w")
            for i in comments:
                if i!="":
                    j=i.rstrip()
                    j=("`~=`"+j+"\n")
                    f.write(j)
            FeedBox.delete(0.0,END)
            Name.delete(0,END)
            Name.insert(0,"Name")
            row=1
            comment_Frame.destroy()
            comment_Frame=Frame(Help_section)
            comment_Frame.configure(bg=Back)
            L1=Label(comment_Frame,text="                          ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Back,fg="black",width="60",bd="5",justify="left").grid(row=0,column=1)
            for i in comments:
                if i!="":
                    if row%2==0:
                        bgcolor="lavender"
                        stick="e"
                    else:
                        bgcolor="bisque"
                        stick="w"
                    Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",bg=bgcolor,fg="black",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky=stick)
                    row+=1
            comment_Frame.grid(row=5,column=0,columnspan=2)
            SearchBox.delete(0,END)
        else:
            if Name.get()=="Name" or Name.get()=="":
                Name.config(bg="pink")
            if FeedBox.get(1.0,END).rstrip()=="":
                FeedBox.config(bg="pink")
    
    def CLICK(EVENT):
        Name.delete(0,END)
    
    Name=Entry(Help_section,font="Rockwell "+str(15+Font_Increase)+" bold",width="25",bd="3")
    Name.insert(0,"Name")
    Name.bind("<Button-1>",CLICK)
    Name.grid(row=2,column=0,sticky="NW")
    comment_Frame=Frame(Help_section)
    comment_Frame.configure(bg=Back)
    
    def SEARCH(event=None):
        Compare=SearchBox.get()
        global comment_Frame
        if len(Compare)>0:
            comment_Frame.destroy()
            comment_Frame=Frame(Help_section)
            comment_Frame.configure(bg=Back)
            comment_Frame.grid(row=5,column=0,columnspan=2)
            MetaList=[]
            f=open(r"Works/FeedBack.ic","r")
            R=f.read()
            comments=R.split("`~=`")
            f.close()
            for i in comments:
                if Compare.lower() in i.lower():
                    MetaList.append(i)
            global LEN
            LEN=len(MetaList)-1
            row=1
            for i in MetaList[begin:begin+10]:
                if i!="":
                    if row%2==begin%2:
                        bgcolor="lavender"
                        stick="e"
        
                    else:
                        bgcolor="bisque"
                        stick="w"
               
                    Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",bg=bgcolor,fg="black",width="50",bd="5",relief="raised",justify="left",anchor="w",wraplength=500).grid(row=row,column=1,sticky=stick)
                    row+=1
            if len(MetaList)==0:
                 Instruction=Label(comment_Frame,text="Oops, Looks Like There Aren't any Matches",font="Rockwell "+str(13+Font_Increase)+" bold").grid(row=0,column=1)
                
        else:
            row=1
            comment_Frame.destroy()
            comment_Frame=Frame(Help_section)
            comment_Frame.configure(bg=Back)
            comment_Frame.grid(row=5,column=0,columnspan=2)
            L1=Label(comment_Frame,text="                          ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Back,fg="black",width="60",bd="5",justify="left").grid(row=0,column=1)
            f=open(r"Works/FeedBack.ic","r")
            R=f.read()
            comments=R.split("`~=`") 
            f.close()
            for i in comments:
                if i!="":
                    if row%2==0:
                        Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",bg="lavender",fg="black",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky="e")
                        row+=1
        
                    else:
                        Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",bg="bisque",fg="black",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky="w")
                        row+=1
            Up.config(bg="coral")
            Down.config(bg="green2")
        
    FeedBox=Text(Help_section,font="Rockwell "+str(11+Font_Increase)+" bold",bg="white",fg="black",width="90",height="5",bd="4",relief="solid")
    FeedBox.grid(row=3,column=0)
    SEARCH_FRAME=Frame(Help_section)
    SearchBox=Entry(SEARCH_FRAME,font="Rockwell "+str(15+Font_Increase)+" bold",bg="white",fg="black",width="42",bd="7",relief="groove")
    SearchBox.grid(row=4,column=0)
    SearchBox.bind("<KeyRelease>",SEARCH)
    Search=Button(SEARCH_FRAME,text="Search:",font="Rockwell "+str(13+Font_Increase)+" bold",bg="gray20",fg="white",width="10",bd="2",relief="solid",command=SEARCH).grid(row=4,column=1,sticky="W")
    SEARCH_FRAME.grid(row=4,column=0,columnspan=2)
    f=open(r"Works/FeedBack.ic","a+")
    f.seek(0)
    R=f.read()
    f.close()
    comments=R.split("`~=`")
    begin,row,start,end=0,1,0,len(comments)
    
    def Up_s():
        if SearchBox.get()=="":
            global start,comment_Frame
            f=open(r"Works/FeedBack.ic","r")
            R=f.read()
            comments=R.split("`~=`")[1:]
            f.close()
            if start>0:
                global row
                row-=1
                r_Row=row
                comment_Frame.destroy()
                start=start-1
                comment_Frame=Frame(Help_section)
                comment_Frame.configure(bg=Back)
                comment_Frame.grid(row=5,column=0,columnspan=2)
                L1=Label(comment_Frame,text="                          ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Back,fg="black",width="60",bd="5",justify="left").grid(row=0,column=1)
                for i in comments[start:start+10]:
                    if i!="":
                        if row%2==0:
                            Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",bg="lavender",fg="black",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky="e")
                            row+=1
            
                        else:
                            Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",bg="bisque",fg="black",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky="w")
                            row+=1
                
                row=r_Row
                Up.config(bg="gold")
                Down.config(bg="green2")
                
            if start==0:
                Up.config(bg="coral")
                Down.config(bg="green2")
        else:
            global begin
            if begin>0 and LEN!=0:
                begin-=1
                try:
                    SEARCH()
                    Up.config(bg="gold")
                    Down.config(bg="green2")       
                except:
                    pass
            if begin<=0:
                Up.config(bg="coral")
    def Down_s():
        if  SearchBox.get()=="":
            global start,comment_Frame
            f=open(r"Works/FeedBack.ic","r")
            R=f.read()
            comments=R.split("`~=`")[1:]
            f.close()
            if start<len(comments)-1:
                global row
                row+=1
                r_Row=row
                comment_Frame.destroy()
                comment_Frame=Frame(Help_section)
                comment_Frame.configure(bg=Back)
                comment_Frame.grid(row=5,column=0,columnspan=2)
                start=start+1
                L1=Label(comment_Frame,text="                          ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Back,fg="black",width="60",bd="5",justify="left").grid(row=0,column=1)
                for i in comments[start:start+10]:
                    if i!="":
                        if row%2==0:
                            Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",bg="lavender",fg="black",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky="e")
                            row+=1
            
                        else:
                            Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",bg="bisque",fg="black",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky="w")
                            row+=1
                row=r_Row
                Up.config(bg="gold")
                Down.config(bg="green2")
            if start==len(comments)-1:
                Up.config(bg="gold")
                Down.config(bg="coral")
        else:
            global begin
            if begin<LEN:
                begin+=1
                try:
                    SEARCH()
                    Up.config(bg="gold")
                except:
                    pass
            if begin>=LEN:
                Down.config(bg="coral")  
    L1=Label(comment_Frame,text="                          ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Back,fg="black",width="60",bd="5",justify="left").grid(row=0,column=1)
    for i in comments[start:start+10]:
        if i!="":
            if row%2==0:
                Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",fg="black",bg="lavender",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky="e")
                row+=1
        
            else:
                Instruction=Label(comment_Frame,text=i+"\n",font="Rockwell "+str(12+Font_Increase)+" bold",fg="black",bg="bisque",width="50",bd="5",relief="raised",justify="left",wraplength=500,anchor="w").grid(row=row,column=1,sticky="w")
                row+=1
        
    def UP_DOWN(Event):
        Command=Event.delta
        Do_Over=int(Command/120)
        for i in range(abs(Do_Over)):
            if Command<0:
                Down_s()
            if Command>0:
                Up_s()
    row=1        
    comment_Frame.grid(row=5,column=0,columnspan=2)
    Submit=Button(Help_section,text=""" POST
~➤""",font="Rockwell "+str(13+Font_Increase)+" bold",bg="purple4",fg="thistle1",bd="5",relief="raised",command=Feedback).grid(row=3,column=1,sticky="N")
    Panel=Frame(Help_section,bg=B_G)
    Up=Button(Panel,text="▲",font="Rockwell "+str(11+Font_Increase)+" bold",bg="coral",fg="white",width="3",height="2",bd="2",relief="raised",command=Up_s)
    Up.grid(row=0,column=0)
    Down=Button(Panel,text="▼",font="Rockwell "+str(11+Font_Increase)+" bold",bg="green2",fg="white",width="3",height="2",bd="2",relief="raised",command=Down_s)
    Down.grid(row=1,column=0)
    Panel.grid(row=5,column=2,sticky="NS")
    Help_section.bind("<MouseWheel>",UP_DOWN)
   
###################### Spacing between lines and Expanding the Domain #######

### To Expand The Domain of Values Inputted For plotting Graphs ###

def Linespace(VAL=None):
    global Number,DIV
    Number=Variable.get()
    DIV=(CANVAS_SIDE/2)/Number
    refresh()    

### Refreshing The Canvas Algorithm Needed for Expanding Domain, Switching Modes ###
    
def refresh():
    HALF_SIDE,POINTS=CANVAS_SIDE/2,(CANVAS_SIDE/2)/DIV
    canvas.delete("all")
    canvas.config(width=CANVAS_SIDE+20,height=CANVAS_SIDE,bg=B_G)
    TXT1=POINTS-y_shift
    TXT2=-(POINTS+x_shift)
    i=0
    while i<(CANVAS_SIDE/DIV):
        canvas.create_line(i*DIV,0,i*DIV,CANVAS_SIDE,width=1,fill=F_G)
        canvas.create_text(CANVAS_SIDE+10,i*DIV,text=round(float(TXT1),1),fill="red2",font="times "+str(7+Font_Increase)+" bold")
        canvas.create_text(i*DIV,10,text=round(float(TXT2),1),fill="red2",font="times "+str(7+Font_Increase)+" bold",angle=90)
        canvas.create_line(0,i*DIV,CANVAS_SIDE,i*DIV,width=1,fill=F_G)
        TXT1-=1
        TXT2+=1
        i+=1        
    
    canvas.create_line(0,HALF_SIDE-y_shift*DIV,CANVAS_SIDE,HALF_SIDE-y_shift*DIV,width=3,fill=axis_1)
    canvas.create_line(HALF_SIDE+x_shift*DIV,0,HALF_SIDE+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)
    Loading["value"]=10
    Loading.update_idletasks()
    for j in range(len(Activity)):
        halfcode=Activity[j]
        if j==int(len(Activity)/2)+1:                  
            Loading["value"]=50
            Loading.update_idletasks()
        
        if "(x)" in halfcode and "," not in halfcode:
            Precision,Plotter_Pen,halfcode=Precision_List[j],colour_list[j],str(Activity[j][0:len(Activity[j])-3])
            try:
                i,l,Initiate=(POINTS)-x_shift,[],True
                while Initiate:
                    try:
                        x=i
                        y=eval(halfcode)
                        l.extend([DIV*(x+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(y+y_shift)])
                        i=round(i-Precision,5)
                        Initiate=False
                    except:
                        if i>-(POINTS+Precision+x_shift):
                                i=round(i-Precision,5)
                        else:
                            Initiate=False
                            
                while i>-(POINTS+Precision+x_shift):
                    try:
                        x=i
                        y=eval(halfcode)
                        l.extend([DIV*(x+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(y+y_shift)])
                        i=round(i-Precision,5)
                        canvas.create_line(l,width="2",fill=Plotter_Pen)
                        del(l[0],l[0])
                                        
                    except:
                        Initiate=True
                        del(l[0],l[0])
                        while Initiate:
                            try:
                                x=i
                                y=eval(halfcode)
                                l.extend([DIV*(x+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(y+y_shift)])
                                i=round(i-Precision,5)
                                Initiate=False
                            except:
                                if i>-(POINTS+Precision+x_shift):
                                        i=round(i-Precision,5)
                                else:
                                    Initiate=False
            except:
                pass
            
        if "(y)" in halfcode and "," not in halfcode:
            Precision,Plotter_Pen,halfcode=Precision_List[j],colour_list[j],Activity[j][0:len(Activity[j])-3]
            try:
                i,l,Initiate=POINTS-y_shift,[],True
                while Initiate:
                    try:
                        y=i
                        x=eval(halfcode)
                        l.extend([HALF_SIDE+DIV*(x+x_shift),HALF_SIDE-DIV*(y+y_shift)]) 
                        i=round(i-Precision,5)
                        Initiate=False
                    except:
                        if i>-(POINTS+Precision+y_shift):
                                i=round(i-Precision,5)
                        else:
                            Initiate=False
                            
                while i>-(POINTS+Precision+y_shift):
                    try:
                        y=i
                        x=eval(halfcode)
                        l.extend([HALF_SIDE+DIV*(x+x_shift),HALF_SIDE-DIV*(y+y_shift)]) 
                        i=round(i-Precision,5)
                        canvas.create_line(l,width="2",fill=Plotter_Pen)
                        del(l[0],l[0])
                        
                    except:
                        Initiate=True
                        del(l[0],l[0])
                        while Initiate:
                            try:
                                y=i
                                x=eval(halfcode)
                                l.extend([HALF_SIDE+DIV*(x+x_shift),HALF_SIDE-DIV*(y+y_shift)]) 
                                i=round(i-Precision,5)
                                Initiate=False
                            except:
                                if i>-(POINTS+Precision+y_shift):
                                        i=round(i-Precision,5)
                                else:
                                    Initiate=False
            except:
                pass
        if ("x" not in halfcode) and ("y" not in halfcode) and (type(halfcode) is list) and (len(halfcode)==9) and ("," not in halfcode):
            line_scale,c1,c2,colour,M_PEN_SIZE=halfcode[4],halfcode[5],halfcode[6],halfcode[7],halfcode[8]
            for i in range(line_scale): canvas.scale("all",c1,c2,scale_constant,scale_constant)
            halfcode=Activity[j][0:4]
            canvas.create_line(halfcode,width=M_PEN_SIZE,fill=colour)
            for i in range(line_scale): canvas.scale("all",c1,c2,1/scale_constant,1/scale_constant)

        if ("x" not in halfcode) and ("y" not in halfcode) and (type(halfcode) is list) and (halfcode[-1]=="Freedraw") and ("," not in halfcode):
            try:
                M_PEN_SIZE,line_scale,c1,c2,colour=halfcode[-6],halfcode[-5],halfcode[-4],halfcode[-3],halfcode[-2]
                for i in range(line_scale): canvas.scale("all",c1,c2,scale_constant,scale_constant)
                try:
                    canvas.create_line(halfcode[0:len(halfcode)-6],width=M_PEN_SIZE,fill=colour)
                except:
                    pass
                for i in range(line_scale): canvas.scale("all",c1,c2,1/scale_constant,1/scale_constant)
            except:
                pass
            
        try:
            if (type(halfcode[0]) is str) and (type(halfcode[2]) is tuple) and ("," in str(halfcode) and (halfcode[1])=="x"):
                try:
                    for i in halfcode[2:]:
                        X,Y,Radii=HALF_SIDE+DIV*(i[0]+x_shift),HALF_SIDE-DIV*(i[1]+y_shift),40/Number
                        canvas.create_oval(X-Radii,Y-Radii,X+Radii,Y+Radii,fill="red")
                        try:
                            canvas.create_line(X1,Y1,X,Y,width="2",fill=halfcode[0])
                            X1=X
                            Y1=Y
                        except:
                            X1=X
                            Y1=Y
                    del(X1)
                    del(X2)
                except:
                    pass
        except:
            pass

        try:
            if (type(halfcode[0]) is str) and (type(halfcode[2]) is tuple) and ("," in str(halfcode) and (halfcode[1])=="y"):
                try:
                    for i in halfcode[2:]:
                        X,Y,Radii=HALF_SIDE+DIV*(i[1]+x_shift),HALF_SIDE-DIV*(i[0]+y_shift),40/Number
                        canvas.create_oval(X-Radii,Y-Radii,X+Radii,Y+Radii,fill="red")
                        try:
                            canvas.create_line(X1,Y1,X,Y,width="2",fill=halfcode[0])
                            X1=X
                            Y1=Y
                        except:
                            X1=X
                            Y1=Y
                    del(X1)
                    del(X2)
                except:
                    pass
        except:
            pass
   
        if "x" in halfcode and "," in halfcode:
            try:
                Precision,Plotter_Pen=Precision_List[j],colour_list[j]
                halfcode=halfcode.rstrip()
                halfcode=halfcode[1:len(halfcode)-1]
                Cord_x,Cord_y=halfcode.split(",")
                i,l,Initiate=POINTS-x_shift,[],True
                while Initiate:
                    try:
                        x=i
                        X_C=eval(Cord_x)
                        Y_C=eval(Cord_y)
                        l.extend([DIV*(X_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(Y_C+y_shift)])  
                        i=round(i-Precision,5)
                        Initiate=False
                    except:
                        if i>-(POINTS+Precision+x_shift):
                                i=round(i-Precision,5)
                        else:
                            Initiate=False
                        
                while i>-(POINTS+Precision+x_shift):
                    try:
                        x=i
                        X_C=eval(Cord_x)
                        Y_C=eval(Cord_y)
                        l.extend([DIV*(X_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(Y_C+y_shift)])  
                        i=round(i-Precision,5)
                        canvas.create_line(l,width="2",fill=Plotter_Pen)
                        del(l[0],l[0])
                    except:
                        Initiate=True
                        del(l[0],l[0])
                        while Initiate:
                            try:
                                x=i
                                X_C=eval(Cord_x)
                                Y_C=eval(Cord_y)
                                l.extend([DIV*(X_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(Y_C+y_shift)])  
                                i=round(i-Precision,5)
                                Initiate=False
                            except:
                                if i>-(POINTS+Precision+x_shift):
                                        i=round(i-Precision,5)
                                else:
                                    Initiate=False
            except:
                pass
            
        if "y" in halfcode and "," in halfcode:
            try:
                Precision,Plotter_Pen=Precision_List[j],colour_list[j]
                halfcode=halfcode.rstrip()
                halfcode=halfcode[1:len(halfcode)-1]
                Cord_x,Cord_y=halfcode.split(",")
                i,l,Initiate=POINTS-y_shift,[],True
                while Initiate:
                    try:
                        y=i
                        X_C=eval(Cord_x)
                        Y_C=eval(Cord_y)
                        l.extend([DIV*(Y_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(X_C+y_shift)]) 
                        i=round(i-Precision,5)
                        Initiate=False
                    except:
                        if i>-(POINTS+Precision+y_shift):
                                i=round(i-Precision,5)
                        else:
                            Initiate=False
                while i>-(POINTS+Precision+y_shift):
                    try:
                        y=i
                        X_C=eval(Cord_x)
                        Y_C=eval(Cord_y)
                        l.extend([DIV*(Y_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(X_C+y_shift)]) 
                        i=round(i-Precision,5)
                        canvas.create_line(l,width="2",fill=Plotter_Pen)
                        del(l[0],l[0])
                    except:
                        while Initiate:
                            try:
                                y=i
                                X_C=eval(Cord_x)
                                Y_C=eval(Cord_y)
                                l.extend([DIV*(Y_C+x_shift)+HALF_SIDE,HALF_SIDE-DIV*(X_C+y_shift)]) 
                                i=round(i-Precision,5)
                                Initiate=False
                            except:
                                if i>-(POINTS+Precision+y_shift):
                                        i=round(i-Precision,5)
                                else:
                                    Initiate=False
            except:
                pass
    for i in range(scale): canvas.scale("all",pos_1,pos_2,scale_constant,scale_constant)
    try:
        x2,y2,x3,y3=x1-3,y1-3,x1+3,y1+3
        circle=canvas.create_oval(x2,y2,x3,y3,fill="red")
    except:
        pass
    Loading["value"]=100
    Loading.update_idletasks()
    canvas.update_idletasks()

### To Set Difference Between Each Point Taken During Plotting- Directly Proportional to Accuracy of Graph (More Accuracy=More Data points) ###

def precision_change(VAL=None):
    global Precision
    Precision=Precise_Variable.get()          

F_Toggle=Frame(window,bd="5",bg="black")

### To View Recently Executed Functions- Stored In Files/MySQL local Database (Optional) ###

def memory():
    global win
    try:
        win.destroy()
    except:
        pass
    def BCLEAR():
        if MY_SWITCH_value=='1':
            try:
                cur.execute("Truncate table Equation")
                win.destroy()
            except:
                pass
        else:
            try:
                file=open(r"Works/Equations.ic","w",encoding="utf-8")
                file.close()
                win.destroy()
            except:
                pass
    win=Tk()
    win.configure(background=B_G)
    win.title("Memory")
    try:
        win.iconbitmap("logo.ico")
    except:
        pass
    win.geometry("+0+0")
    win.geometry("380x"+str(HEIGHT))
    if MY_SWITCH_value=='1':
        try:
            global EQS
            cur.execute("select * from Equation")
            EQS=cur.fetchall()
            Temp_List=[]
            for i in EQS:
                for j in i:
                    Temp_List.append(j)
            EQS=Temp_List
        except:
            pass
    else:
        file=open(r"Works/Equations.ic","a+",encoding="utf-8")
        file.seek(0)
        EQS=file.read()
        EQS=EQS.split("`~=`")
        EQS.remove("")

    if MY_SWITCH_value=='0':
        String="\nStored In File"
    if MY_SWITCH_value=='1':
        String="\nStored In SQL"
          
    L_M=Label(win,text="Previously Entered Functions"+String,font="Rockwell "+str(13+Font_Increase)+" bold",bg="Dodgerblue",fg="white",relief="raised",bd="5").grid(row=0,column=0)
    Memory_Text=Text(win,font="Rockwell "+str(16+Font_Increase)+" bold",width=30,height=25)
    Memory_Text.grid(row=1,column=0)
    B_CLEAR=Button(win,text="Clear Memory",font="Rockwell "+str(13+Font_Increase)+" bold",width="20",bg="red",fg="white",command=BCLEAR)
    B_CLEAR.grid(row=2,column=0)
    count=1
    try:
        EQS.reverse()
    except:
        pass
    for i in EQS:
        J=i.rstrip()
        Memory_Text.insert(END,str(count)+". "+J+"\n")
        count+=1          

F_Toggle=Frame(window,bd="5",bg="black")

### To Hide F_Toggle Frame -Manage Space ###

def Exit():
    global Exit_Variable
    for i in F_Toggle.winfo_children(): i.destroy()
    B_SideBar=Button(F_Toggle,text="➜",font="rockwell "+str(12+Font_Increase)+" bold",height="4",bg="red",fg="white",width="2",command=SideBar)
    B_SideBar.grid(row=0,column=0,columnspan=2,sticky="EW")
    Exit_Variable=1
        
### To Create/Show F_Toggle Frame ###

def Add_Plotter_Colour():
    global Plotter_Pen,Plotter_List
    colour=askcolor(title="Choose Plotter Colour")
    if colour[1]!=None:
        Plotter_Pen=colour[1]
        Plotter_List.insert(0,Plotter_Pen)
        Plotter_List.pop()
        Exit()
        SideBar()
    
def Add_Marker_Colour():
    global Marker_Pen,Marker_Pen
    colour=askcolor(title="Choose Marker Colour")
    if colour[1]!=None:
        Marker_Pen=colour[1]
        Marker_List.insert(0,Marker_Pen)
        Marker_List.pop()
        Exit()
        SideBar()

def SideBar():
    def SET_EFFECT():
        global Effect_variable
        Effect_variable=Check.get()
    try:
        for i in F_Toggle.winfo_children(): i.destroy()
    except:
        pass
    global Precise_Variable,Variable,Check,Colour_P1,Colour_P2,Colour_P3,Colour_P4,Colour_M1,Colour_M2,Colour_M3,Colour_M4,Memory,Exit_Variable,B_O,B_N
    Exit_Variable=0
    B_SideBar=Button(F_Toggle,text="⬅",font="Rockwell "+str(10+Font_Increase)+" bold",bg="red",fg="white",width="2",relief="raised",command=Exit)
    B_SideBar.grid(row=0,column=0,columnspan=2,sticky="E")        
    L_dark=Label(F_Toggle,text="Dark-Mode",font="Rockwell "+str(14+Font_Increase)+" bold",bg="black",fg="white",width="12").grid(row=1,column=0,columnspan=2)
    if Dark_value==0:
        B_O=Button(F_Toggle,text="  ",font="Rockwell "+str(11+Font_Increase)+" bold",bg="white",fg="black",width="7",relief="raised")
        B_O.grid(row=2,column=0)
        B_N=Button(F_Toggle,text="OFF",font="Rockwell "+str(11+Font_Increase)+" bold",bg="red",fg="white",width="7",relief="raised",command=ON)
        B_N.grid(row=2,column=1)
    else:
        B_O=Button(F_Toggle,text="ON",font="Rockwell "+str(11+Font_Increase)+" bold",bg="light green",fg="white",width="7",relief="raised",command=OFF)
        B_O.grid(row=2,column=0)
        B_N=Button(F_Toggle,text="  ",font="Rockwell "+str(11+Font_Increase)+" bold",bg="white",fg="black",width="7",relief="raised")
        B_N.grid(row=2,column=1)
        
    Space=Label(F_Toggle,text=" ",bg="black").grid(row=3,column=0)
    Colour=Label(F_Toggle,text="Marker-Pen ✎",font="Rockwell "+str(14+Font_Increase)+" bold",bg="black",fg="white",width="12",relief="solid").grid(row=4,column=0,columnspan=2)
    if Marker_Pen==Marker_List[0]:
        Colour_M1=Button(F_Toggle,text="❤",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[0],width="3",bd="5",relief="raised",command=colour_M1)
        Colour_M1.grid(row=5,column=0)
        Colour_M2=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[1],width="3",bd="5",relief="raised",command=colour_M2)
        Colour_M2.grid(row=5,column=1)
        Colour_M3=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[2],width="3",bd="5",relief="raised",command=colour_M3)
        Colour_M3.grid(row=6,column=0)
    if Marker_Pen==Marker_List[1]:
        Colour_M1=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[0],width="3",bd="5",relief="raised",command=colour_M1)
        Colour_M1.grid(row=5,column=0)
        Colour_M2=Button(F_Toggle,text="❤",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[1],width="3",bd="5",relief="raised",command=colour_M2)
        Colour_M2.grid(row=5,column=1)
        Colour_M3=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[2],width="3",bd="5",relief="raised",command=colour_M3)
        Colour_M3.grid(row=6,column=0)
    if Marker_Pen==Marker_List[2]:
        Colour_M1=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[0],width="3",bd="5",relief="raised",command=colour_M1)
        Colour_M1.grid(row=5,column=0)
        Colour_M2=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[1],width="3",bd="5",relief="raised",command=colour_M2)
        Colour_M2.grid(row=5,column=1)
        Colour_M3=Button(F_Toggle,text="❤",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Marker_List[2],width="3",bd="5",relief="raised",command=colour_M3)
        Colour_M3.grid(row=6,column=0)
    
    Space=Label(F_Toggle,text=" ",bg="black").grid(row=8,column=0)
    Colour=Label(F_Toggle,text="Plotter-Pen ✒",font="Rockwell "+str(14+Font_Increase)+" bold",bg="black",fg="white",width="12",relief="solid").grid(row=9,column=0,columnspan=2)

    if Plotter_Pen==Plotter_List[0]:
        Colour_P1=Button(F_Toggle,text="✘",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[0],width="3",bd="5",relief="raised",command=colour_P1)
        Colour_P1.grid(row=10,column=0)
        Colour_P2=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[1],width="3",bd="5",relief="raised",command=colour_P2)
        Colour_P2.grid(row=10,column=1)
        Colour_P3=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[2],width="3",bd="5",relief="raised",command=colour_P3)
        Colour_P3.grid(row=11,column=0)
    if Plotter_Pen==Plotter_List[1]:
        Colour_P1=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[0],width="3",bd="5",relief="raised",command=colour_P1)
        Colour_P1.grid(row=10,column=0)
        Colour_P2=Button(F_Toggle,text="✘",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[1],width="3",bd="5",relief="raised",command=colour_P2)
        Colour_P2.grid(row=10,column=1)
        Colour_P3=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[2],width="3",bd="5",relief="raised",command=colour_P3)
        Colour_P3.grid(row=11,column=0)
    if Plotter_Pen==Plotter_List[2]:
        Colour_P1=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[0],width="3",bd="5",relief="raised",command=colour_P1)
        Colour_P1.grid(row=10,column=0)
        Colour_P2=Button(F_Toggle,text=" ",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[1],width="3",bd="5",relief="raised",command=colour_P2)
        Colour_P2.grid(row=10,column=1)
        Colour_P3=Button(F_Toggle,text="✘",font="Rockwell "+str(12+Font_Increase)+" bold",bg=Plotter_List[2],width="3",bd="5",relief="raised",command=colour_P3)
        Colour_P3.grid(row=11,column=0)

    Colour_M4=Button(F_Toggle,text="+",font="Rockwell "+str(12+Font_Increase)+" bold",bg="white",fg="black",width="3",bd="5",relief="raised",command=Add_Marker_Colour)
    Colour_M4.grid(row=6,column=1)
        
    Colour_P4=Button(F_Toggle,text="+",font="Rockwell "+str(12+Font_Increase)+" bold",bg="white",fg="black",width="3",bd="5",relief="raised",command=Add_Plotter_Colour)
    Colour_P4.grid(row=11,column=1)

    Space=Label(F_Toggle,text=" ",bg="black").grid(row=13,column=0)
    HELP=Button(F_Toggle,text="Help?",font="Rockwell "+str(15+Font_Increase)+" bold",bg="white",command=Help).grid(row=14,column=0,columnspan=2)
    Space=Label(F_Toggle,text=" ",bg="black").grid(row=15,column=0)

    Linespace_Label=Label(F_Toggle,text="Domain Grid ▦",font="Rockwell "+str(13+Font_Increase)+" bold",bg="black",fg="white",width="12",relief="solid").grid(row=16,column=0,columnspan=2)    
    Variable=DoubleVar()
    Option=OptionMenu(F_Toggle,Variable,10,20,30,40,50,100,200,command=Linespace)
    Variable.set(int(Number))
    Option.grid(row=17,column=0,columnspan=2)
    Option.config(font="Rockwell "+str(15+Font_Increase)+" bold",bg="black",fg="white")
    Space=Label(F_Toggle,text=" ",bg="black").grid(row=18,column=0)

    Precision_Label=Label(F_Toggle,text="Precision",font="Rockwell "+str(13+Font_Increase)+" bold",bg="black",fg="white",width="12",relief="solid").grid(row=19,column=0,columnspan=2)
    Precise_Variable=DoubleVar()
    Precise=OptionMenu(F_Toggle,Precise_Variable,0.1,0.01,0.001,0.0001,command=precision_change)
    Precise.grid(row=20,column=0,columnspan=2)
    Precise_Variable.set(Precision)
    Precise.config(font="Rockwell "+str(15+Font_Increase)+" bold",bg="black",fg="white")
    
    Blank=Label(F_Toggle,text="",fg="black",bg="black").grid(row=21,column=0,columnspan=2)
    Check=IntVar()

    Effect_Frame=Frame(F_Toggle)
    check_label=Label(Effect_Frame,text="Effects",font="Rockwell "+str(13+Font_Increase)+" bold",bg="white",fg="black",width="6").grid(row=1,column=0)
    Motion_graph=Checkbutton(Effect_Frame,font="Rockwell "+str(10+Font_Increase)+" bold",variable=Check,bg="red",command=SET_EFFECT)
    Motion_graph.grid(row=1,column=1)
    Effect_Frame.grid(row=22,column=0,columnspan=2)
    Check.set(Effect_variable)

    Blank=Label(F_Toggle,text="",fg="black",bg="black").grid(row=23,column=0,columnspan=2)
    Memory=Button(F_Toggle,text="Memory",font="Rockwell "+str(13+Font_Increase)+" bold",width="10",bg="gold",relief="solid",command=memory)
    Memory.grid(row=24,column=0,columnspan=2)    

SideBar()
               
def Initial_Setup():
    File=open(r"Works/Past_Data.ic","a+")
    File.seek(0)
    R=(File.read()).strip()
    File.close()
    global Activity,colour_list,Precision_List,canvas_number,CANVAS_SIDE,DIV,x_shift,y_shift,B_G,F_G,Variable,Number,Dark_value,axis_1,axis_2,m_switch,B_O,B_N
    if R!=[[],[]] and R!="":
        message=messagebox.askquestion("Note!","Do you want to continue with saved work")
        if message=="yes":
                canvas_button_1.config(bg="red",fg="white")
                canvas_button_2.config(bg="black",fg="white")
                File=open(r"Works/Past_Data.ic","r")
                R=eval((File.read()).strip())
                File.close()
                Activity,colour_list,Precision_List,[CANVAS_SIDE,Number,x_shift,y_shift,Dark_value,B_G,F_G,axis_1,axis_2,m_switch]=R[0]

                DIV=(CANVAS_SIDE/2)/Number
                Variable.set(int(Number))
                
                if Dark_value==1:
                    B_O=Button(F_Toggle,text="ON",font="Rockwell "+str(11+Font_Increase)+" bold",bg="light green",fg="white",width="7",relief="raised",command=OFF)
                    B_O.grid(row=2,column=0)
                    B_N=Button(F_Toggle,text="  ",font="Rockwell "+str(11+Font_Increase)+" bold",bg="white",fg="black",width="7",relief="raised")
                    B_N.grid(row=2,column=1)
                    Dark_value,B_G,F_G=1,"grey18","gray60"
                    L_Adjust.config(bg=B_G)
                    Main_Frame.config(bg=B_G)
                    L_Adjust1.config(bg=B_G)
                    window1.config(bg=B_G)
                    L_Adjust2.config(bg=B_G)
                    LB1.config(bg=B_G)
                    try:
                        LB3.config(bg=B_G)
                    except:
                        pass
                    Loading["value"]=50
                    Loading.update_idletasks()
                    canvas.configure(background=B_G)
                    TXT1=(CANVAS_SIDE/2)/DIV-y_shift
                    TXT2=-((CANVAS_SIDE/2)/DIV+x_shift)
                    i=0
                    while i<(CANVAS_SIDE/DIV):
                        canvas.create_line(i*DIV,0,i*DIV,CANVAS_SIDE,width=1,fill=F_G)
                        canvas.create_text(CANVAS_SIDE+10,i*DIV,text=round(float(TXT1),1),fill="red2",font="times "+str(7+Font_Increase)+" bold")
                        canvas.create_text(i*DIV,10,text=round(float(TXT2),1),fill="red2",font="times "+str(7+Font_Increase)+" bold",angle=90)
                        canvas.create_line(0,i*DIV,CANVAS_SIDE,i*DIV,width=1,fill=F_G)
                        TXT1-=1
                        TXT2+=1
                        i+=1       
                        
                    canvas.create_line(0,CANVAS_SIDE/2-y_shift*DIV,CANVAS_SIDE,CANVAS_SIDE/2-y_shift*DIV,width=3,fill=axis_1)
                    canvas.create_line(CANVAS_SIDE/2+x_shift*DIV,0,CANVAS_SIDE/2+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)
                    triple_click()
                    triple_click()
                else:
                    B_O=Button(F_Toggle,text="  ",font="Rockwell "+str(11+Font_Increase)+" bold",bg="white",fg="black",width="7",relief="raised")
                    B_O.grid(row=2,column=0)
                    B_N=Button(F_Toggle,text="OFF",font="Rockwell "+str(11+Font_Increase)+" bold",bg="red",fg="white",width="7",relief="raised",command=ON)
                    B_N.grid(row=2,column=1)
                    Dark_value,B_G,F_G,colour=0,"grey100","grey18","seashell2"
                    L_Adjust.config(bg=colour)
                    Main_Frame.config(bg=colour)
                    L_Adjust1.config(bg=colour)
                    window1.config(bg=colour)
                    L_Adjust2.config(bg=colour)
                    LB1.config(bg=colour)
                    try:
                        LB3.config(bg=colour)
                    except:
                        pass
                    Loading["value"]=50
                    Loading.update_idletasks()
                    canvas.configure(background=B_G)
                    TXT1=(CANVAS_SIDE/2)/DIV-y_shift
                    TXT2=-((CANVAS_SIDE/2)/DIV+x_shift)
                    i=0
                    while i<(CANVAS_SIDE/DIV):
                        canvas.create_line(i*DIV,0,i*DIV,CANVAS_SIDE,width=1,fill=F_G)
                        canvas.create_text(CANVAS_SIDE+10,i*DIV,text=round(float(TXT1),1),fill="red2",font="times "+str(7+Font_Increase)+" bold")
                        canvas.create_text(i*DIV,10,text=round(float(TXT2),1),fill="red2",font="times "+str(7+Font_Increase)+" bold",angle=90)
                        canvas.create_line(0,i*DIV,CANVAS_SIDE,i*DIV,width=1,fill=F_G)
                        TXT1-=1
                        TXT2+=1
                        i+=1      
                        
                    canvas.create_line(0,CANVAS_SIDE/2-y_shift*DIV,CANVAS_SIDE,CANVAS_SIDE/2-y_shift*DIV,width=3,fill=axis_1)
                    canvas.create_line(CANVAS_SIDE/2+x_shift*DIV,0,CANVAS_SIDE/2+x_shift*DIV,CANVAS_SIDE,width=3,fill=axis_2)
                    triple_click()
                    triple_click()
                    
                canvas_number=1
                refresh()
        else:
            File=open(r"Works/Past_Data.ic","w")
            R=[[Activity,colour_list,Precision_List,[CANVAS_SIDE,Number,x_shift,y_shift,Dark_value,B_G,F_G,axis_1,axis_2,m_switch]],[Activity,colour_list,Precision_List,[CANVAS_SIDE,Number,x_shift,y_shift,Dark_value,B_G,F_G,axis_1,axis_2,m_switch]]]
            File.write(str(R))
            File.close()
    else:
        File=open(r"Works/Past_Data.ic","w")
        R=[[Activity,colour_list,Precision_List,[CANVAS_SIDE,Number,x_shift,y_shift,Dark_value,B_G,F_G,axis_1,axis_2,m_switch]],[Activity,colour_list,Precision_List,[CANVAS_SIDE,Number,x_shift,y_shift,Dark_value,B_G,F_G,axis_1,axis_2,m_switch]]]
        File.write(str(R))
        File.close()
        
Initial_Setup()    

### Managing Window Into Self-Space-Adjusting-Widget-Window ###

window1.grid_columnconfigure(0,weight=1)
window1.grid_columnconfigure(1,weight=1)
window1.grid_columnconfigure(2,weight=1)
F_Toggle.grid_columnconfigure(0,weight=1)
F_Toggle.grid_columnconfigure(1,weight=1)
canvas.grid_columnconfigure(0,weight=1)

window1.grid_rowconfigure(1,weight=1)
window1.grid_rowconfigure(2,weight=1)
window1.grid_rowconfigure(3,weight=1)
window1.grid_rowconfigure(4,weight=1)
window1.grid_rowconfigure(5,weight=1)
window1.grid_rowconfigure(6,weight=1)
window1.grid_rowconfigure(7,weight=1)
window1.grid_rowconfigure(8,weight=1)
window1.grid_rowconfigure(9,weight=1)

F_Toggle.grid_rowconfigure(0,weight=1)
F_Toggle.grid_rowconfigure(1,weight=1)
F_Toggle.grid_rowconfigure(2,weight=1)
F_Toggle.grid_rowconfigure(3,weight=1)
F_Toggle.grid_rowconfigure(4,weight=1)
F_Toggle.grid_rowconfigure(5,weight=1)
F_Toggle.grid_rowconfigure(6,weight=1)
F_Toggle.grid_rowconfigure(7,weight=1)
F_Toggle.grid_rowconfigure(8,weight=1)
F_Toggle.grid_rowconfigure(9,weight=1)
F_Toggle.grid_rowconfigure(10,weight=1)
F_Toggle.grid_rowconfigure(11,weight=1)
F_Toggle.grid_rowconfigure(12,weight=1)
F_Toggle.grid_rowconfigure(13,weight=1)
F_Toggle.grid_rowconfigure(14,weight=1)
F_Toggle.grid_rowconfigure(15,weight=1)
F_Toggle.grid_rowconfigure(16,weight=1)
F_Toggle.grid_rowconfigure(17,weight=1)
F_Toggle.grid_rowconfigure(18,weight=1)
F_Toggle.grid_rowconfigure(19,weight=1)
F_Toggle.grid_rowconfigure(20,weight=1)
F_Toggle.grid_rowconfigure(21,weight=1)
F_Toggle.grid_rowconfigure(22,weight=1)
F_Toggle.grid_rowconfigure(23,weight=1)
F_Toggle.grid_rowconfigure(24,weight=1)

### Packing Main Frames.Canvas and Looping The Window ###

canvas.grid_rowconfigure(0,weight=1)
window1.pack(side=LEFT,fill="y")
F_Toggle.pack(side=LEFT)
Canvas_Main.pack(side=LEFT)

window.mainloop()

######################################### END ###############################
