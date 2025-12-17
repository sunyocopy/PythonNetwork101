from tkinter import *
from tkinter import ttk
###########SERVER############
import socket
import threading

def server():
    while True:
        # ********************************* #
        serverip = '192.168.1.10' # IP ของ John
        port = 8500 # PORT ของ John
        # ********************************* #
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        server.bind((serverip,port))
        server.listen(5)
        print('waiting...')

        client, addr = server.accept()
        print('connected from...',addr)

        data = client.recv(1024).decode('utf-8')
        print('Data: ',data)
        ## add msg to msg_list ##
        t = 'Robert: {}'.format(data)
        msg_list.append(t)

        # update data in main gui
        tt = ''
        count = 14 - len(msg_list)
        for i in range(count):
            tt = tt + ' \n'

        for ms in msg_list[-14:]:
            tt = tt + ms +'\n'
        
        v_msg_text.set(tt)

        client.send('we got your message!'.encode('utf-8'))
        client.close()


def server_run():
    task1 = threading.Thread(target=server)
    task1.start()


GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมแชท - John')

L = Label(GUI,text='John',font=(None,20),fg='blue').pack()

F1 = Frame(GUI)
F1.place(x=50,y=400)

v_textbox = StringVar()
E1 = ttk.Entry(F1,textvariable=v_textbox,font=('Angsana New',15),width=40)
E1.grid(row=0,column=0)


msg_list = []

def send_message_to_server(msg):
    # ********************************* #
    serverip = '192.168.1.10' # IP ของ Robert
    port = 8600 # PORT ของ Robert
    # ********************************* #

    data = msg

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((serverip,port))
    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ',data_server)
    server.close()

def send_message(event=None):
    msg = v_textbox.get()
    msg_text = 'John: {}'.format(msg)
    msg_list.append(msg_text)
    print(msg_list)
    tt = ''
    # add space
    count = 14 - len(msg_list)
    for i in range(count):
        tt = tt + ' \n'

    for ms in msg_list[-14:]:
        tt = tt + ms +'\n'
    
    v_msg_text.set(tt)
    v_textbox.set('')

    ############SEND MESSAGE TO OTHER SERVER##############
    task = threading.Thread(target=send_message_to_server,args=[msg])
    task.start()

E1.bind('<Return>',send_message)

B1 = ttk.Button(F1,text='send',command=send_message)
B1.grid(row=0,column=1,ipadx=20,ipady=8,padx=10)


v_msg_text = StringVar()
messages = ttk.Label(GUI,textvariable=v_msg_text,font=(None,15))
messages.place(x=50,y=50)

server_run()

GUI.mainloop()