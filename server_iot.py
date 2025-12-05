from tkinter import *
from tkinter import ttk
############NETWORK############
import socket
import threading
from datetime import datetime

serverip = '192.168.1.10'
port = 8500

def server():
    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        server.bind((serverip,port))
        server.listen(5)
        print('waiting...')

        client, addr = server.accept()
        print('connected from...',addr)

        data = client.recv(1024).decode('utf-8')
        print('Data: ',data)
        # DATA: A_TV = Clinet: A, T=Get Time, V=Volume
        try:
            CL,TX = data.split('_')
            if CL == 'A':
                t = v_time1.get()
                v = v_volume1.get()
                if TX == 'TV':
                    text = 'Time: {} Volume: {}'.format(t,v)
                elif TX == 'RTC':
                    tt = datetime.now().strftime('%H:%M:%S')
                    text = 'Server Time: {}'.format(tt)
                else:
                    text = 'no data'
            elif CL == 'B':
                t = v_time2.get()
                v = v_volume2.get()
                if TX == 'TV':
                    text = 'Time: {} Volume: {}'.format(t,v)
                elif TX == 'RTC':
                    tt = datetime.now().strftime('%H:%M:%S')
                    text = 'Server Time: {}'.format(tt)
                else:
                    text = 'no data'
            elif CL == 'C':
                t = v_time3.get()
                v = v_volume3.get()
                if TX == 'TV':
                    text = 'Time: {} Volume: {}'.format(t,v)
                elif TX == 'RTC':
                    tt = datetime.now().strftime('%H:%M:%S')
                    text = 'Server Time: {}'.format(tt)
                else:
                    text = 'no data'
            elif CL == 'D':
                t = v_time4.get()
                v = v_volume4.get()
                if TX == 'TV':
                    text = 'Time: {} Volume: {}'.format(t,v)
                elif TX == 'RTC':
                    tt = datetime.now().strftime('%H:%M:%S')
                    text = 'Server Time: {}'.format(tt)
                else:
                    text = 'no data'
            else:
                text = 'no data'
            

        except:
            text = 'no data'

        client.send(text.encode('utf-8'))
        client.close()

def server_run():
    task1 = threading.Thread(target=server)
    task1.start()


GUI = Tk()
GUI.geometry('800x800')
GUI.title('IoT Server')

#######################
v_time1 = StringVar()
v_time1.set('15.00')
v_volume1 = StringVar()
v_volume1.set('10m.')
#---------
v_time2 = StringVar()
v_time2.set('15.20')
v_volume2 = StringVar()
v_volume2.set('10m.')
#---------
v_time3 = StringVar()
v_time3.set('15.30')
v_volume3 = StringVar()
v_volume3.set('10m.')
#---------
v_time4 = StringVar()
v_time4.set('15.40')
v_volume4 = StringVar()
v_volume4.set('10m.')
#######################
F1 = Frame(GUI)
F1.place(x=50,y=50)

L = Label(F1,text='A',font=(None,20,'bold'))
L.pack()

icon1 = PhotoImage(file='icon_rice_small.png')
IC1 = Label(F1,image=icon1)
IC1.pack()

E11 = ttk.Entry(F1,textvariable=v_time1)
E11.pack()

E12 = ttk.Entry(F1,textvariable=v_volume1)
E12.pack()
###############
F2 = Frame(GUI)
F2.place(x=350,y=50)

L = Label(F2,text='B',font=(None,20,'bold'))
L.pack()

# icon1 = PhotoImage(file='icon_rice_small.png')
IC2 = Label(F2,image=icon1)
IC2.pack()

E11 = ttk.Entry(F2,textvariable=v_time2)
E11.pack()

E12 = ttk.Entry(F2,textvariable=v_volume2)
E12.pack()

###############
F3 = Frame(GUI)
F3.place(x=50,y=400)

L = Label(F3,text='C',font=(None,20,'bold'))
L.pack()

# icon1 = PhotoImage(file='icon_rice_small.png')
IC2 = Label(F3,image=icon1)
IC2.pack()

E11 = ttk.Entry(F3,textvariable=v_time3)
E11.pack()

E12 = ttk.Entry(F3,textvariable=v_volume3)
E12.pack()

###############
F4 = Frame(GUI)
F4.place(x=350,y=400)

L = Label(F4,text='D',font=(None,20,'bold'))
L.pack()

# icon1 = PhotoImage(file='icon_rice_small.png')
IC2 = Label(F4,image=icon1)
IC2.pack()

E11 = ttk.Entry(F4,textvariable=v_time4)
E11.pack()

E12 = ttk.Entry(F4,textvariable=v_volume4)
E12.pack()


server_run()

GUI.mainloop()