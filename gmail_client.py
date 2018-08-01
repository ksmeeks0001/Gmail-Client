from tkinter import*
import smtplib


class Gmail_Client():
    """GUI gmail app"""

    def __init__(self):

        #root and variables
        self.root = Tk()
        self.root.geometry('600x550')
        self.root.title('GMAIL CLIENT')
        self.header = 'GMAIL CLIENT' + '\n' * 8
        #email variables
        self.client = smtplib.SMTP('smtp.gmail.com' , 587)
        self.client.ehlo()
        self.client.starttls()
        self.user = ''
        self.password = None
        self.recepient = ''
        self.message = "Subject: \n"

        #login frame
        self.login_frame = Frame(self.root)
        self.app_label = Label(self.login_frame, text=self.header,
                               font='CASTELLAR')
        self.user_label = Label(self.login_frame , text='Email Address',
                                font='Elephant')
        self.user_entry = Entry(self.login_frame, width=30, font='Simsun')
        self.pass_label = Label(self.login_frame, text='Password',
                                font='Elephant')
        self.pass_entry = Entry(self.login_frame, width=30, font='Simsun')
        self.login_button = Button(self.login_frame, text='LOGIN',
                                   font='Elephant', command=self.log_in)
        self.login_status = StringVar()
        self.login_status.set('')
        self.login_status_label = Label(self.login_frame,
                                        textvariable= self.login_status,
                                        font = ('Elephant', 10),
                                        fg = 'red')
        #pack
        self.login_frame.pack()
        self.app_label.pack()
        self.user_label.pack()
        self.user_entry.pack()
        self.pass_label.pack()
        self.pass_entry.pack()
        self.login_status_label.pack()
        self.login_button.pack(side=RIGHT)               
        

        self.root.mainloop()

    def log_in(self):
        """Pressing login button"""
        try:
            #set user and password variables
            self.user = self.user_entry.get()
            self.password = self.pass_entry.get()
            #attempt login
            self.client.login(self.user , self.password)
            #unpack login frame and pack compose frame
            self.login_frame.pack_forget()

            #compose frame
            self.compose_frame = Frame(self.root)
            #self.compose_frame.pack()
        
            self.from_text = 'From: ' + self.user
            self.from_label = Label(self.compose_frame, text=self.from_text,
                                font='Elephant')
            self.recepient_frame = Frame(self.compose_frame) 
            self.recepient_label = Label(self.recepient_frame,text='To:' ,
                                     font='Elephant')
            self.recepient_entry = Entry(self.recepient_frame,
                                     width=30, font='Simsun')
            self.message_label = Label(self.compose_frame,text='Message:\t\t\t\t\t',
                                   font='Elephant')
            self.message_entry = Text(self.compose_frame, font='Simsun')
            self.send_button = Button(self.compose_frame, text='SEND',
                                  font='Elephant',command=self.send)
            self.sent_message = StringVar()
            self.sent_message.set('')
            self.sent_message_label = Label(self.compose_frame,
                                            textvariable = self.sent_message,
                                            fg = 'blue', font = ('Elephant', 11))
                

            self.from_label.pack()
            self.recepient_frame.pack()
            self.recepient_label.pack(side=LEFT)
            self.recepient_entry.pack(side=RIGHT)
            self.message_label.pack()
            self.message_entry.pack()
            self.sent_message_label.pack()
            self.send_button.pack(side=RIGHT)


            self.compose_frame.pack()             

        except:
           self.login_status.set('Username or Password not correct \nTry again')
           

    def send(self):
        try:
            self.recepient = self.recepient_entry.get()
            self.message += self.message_entry.get(1.0,END+"-1c")

            self.client.sendmail(self.user, self.recepient, self.message)
            self.sent_message.set('Message Sent Successfully')

            self.recepient_entry.delete(0, 'end')
            self.message_entry.delete('1.0', END)
        except:
            self.sent_message.set('Send Failure')
        



app = Gmail_Client()

        
