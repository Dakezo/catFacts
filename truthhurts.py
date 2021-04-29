import os
import requests
import tkinter as tk
from functools import partial
from twilio.rest import Client
from api import account_sid, auth_token
import threading
import random
import time


class gui_stuff(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.buttons = dict()
        self.labels = dict()
        self.fields = dict()
        self.master = master
        self.pack()
        self.init_ui()

    def init_ui(self):
        self.buttons["Send"] = tk.Button(self, borderwidth=10, command=partial(self.actions, "Send"))
        self.buttons["Send"].grid(row=2, column=0, padx=20, pady=20)
        self.buttons["Send"]["text"] = "Send Cat Facts"

        self.buttons["Reset"] = tk.Button(self, borderwidth=10, command=partial(self.actions, "Reset"))
        self.buttons["Reset"].grid(row=2, column=2, padx=20, pady=20)
        self.buttons["Reset"]["text"] = "Reset Cat Facts"

        self.buttons["I'm Feeling Lucky"] = tk.Button(self, borderwidth=10, command=partial(self.actions, "I'm Feeling Lucky"))
        self.buttons["I'm Feeling Lucky"].grid(row=2, column=1, padx=20, pady=20)
        self.buttons["I'm Feeling Lucky"]["text"] = "I'm Feeling Lucky"

        self.fields["Digis"] = tk.Text(self, height=2, width=40)
        self.fields["Digis"].grid(row=0, column=1, columnspan=3, padx=20, pady=20)

        self.labels["Digis"] = tk.Label(self, borderwidth=10)
        self.labels["Digis"].grid(row=0, column=0, padx=20, pady=20)
        self.labels["Digis"]["text"] = "This for the Digis:"

        self.fields["How Many"] = tk.Text(self, height=2, width=40)
        self.fields["How Many"].grid(row=1, column=1, columnspan=3, padx=20, pady=20)

        self.labels["How Many"] = tk.Label(self, borderwidth=10)
        self.labels["How Many"].grid(row=1, column=0, padx=20, pady=20)
        self.labels["How Many"]["text"] = "How Many you going to send:"

    def actions(self, action):
        return_variable = action
        counter = 1
        if(action == "Send"):
            if(self.fields["Digis"].get("1.0", tk.END) ==""):
                sms_loop = threading.Thread(name='threaded_sms_loop', target=self.threaded_sms_loop)
                sms_loop.start()
            else:
                print("Shits Broke. Open a ticket with Support.")

        if (action == "Reset"):
            self.fields["Digis"].delete("1.0", tk.END)
            self.fields["How Many"].delete("1.0", tk.END)


        if (action == "I'm Feeling Lucky"):
            print(self.fields["Digis"].get("1.0", tk.END))
            #print(self.fields["I'm Feeling Lucky"].get("1.0", tk.END))
            self.create_new_window()

    def threaded_sms_loop(self):
        if (self.fields["How Many"].get("1.0", tk.END) == ""):
            counter = 1
            print(self.fields["Digis"].get("1.0", tk.END))
            self.create_sms(self.get_cat_facts(), str(self.fields["Digis"].get("1.0", tk.END)))
        else:
            counter = int(self.fields["How Many"].get("1.0", tk.END))
            for x in range(0, counter):
                try:
                    time.sleep(random.randint(0,5))
                    print(self.fields["Digis"].get("1.0", tk.END))
                    self.create_sms(self.get_cat_facts(), str(self.fields["Digis"].get("1.0", tk.END)))
                except Exception as e:
                    print(e)

    def create_sms(self, text, phone_number):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body= text,
            from_='+16099007521',
            to=phone_number
        )

        print(message.sid)

    def get_cat_facts(self):
        return requests.get(url="https://catfact.ninja/fact").json()["fact"]

    def create_new_window(self):
        newWindow = tk.Toplevel(self.master)
        newWindow.title("Get Fukt")
        newWindow.geometry('600x200')
        tk.Label(newWindow,text="Sike this shit don't work!").pack()

root = tk.Tk(className="Cat Facts")
root.geometry("600x600")
app = gui_stuff(master=root)
app.mainloop()