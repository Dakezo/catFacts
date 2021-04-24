import os
import requests
import tkinter as tk
from functools import partial
from twilio.rest import Client


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
        self.buttons["Send"].grid(row=1, column=0, padx=20, pady=20)
        self.buttons["Send"]["text"] = "Send Cat Facts"

        self.buttons["Reset"] = tk.Button(self, borderwidth=10, command=partial(self.actions, "Reset"))
        self.buttons["Reset"].grid(row=1, column=2, padx=20, pady=20)
        self.buttons["Reset"]["text"] = "Reset Cat Facts"

        self.buttons["I'm Feeling Lucky"] = tk.Button(self, borderwidth=10, command=partial(self.actions, "Sike this don't do shit"))
        self.buttons["I'm Feeling Lucky"].grid(row=1, column=1, padx=20, pady=20)
        self.buttons["I'm Feeling Lucky"]["text"] = "I'm Feeling Lucky"

        self.fields["Digis"] = tk.Text(self, height=2, width=40)
        self.fields["Digis"].grid(row=0, column=1, columnspan=3, padx=20, pady=20)

        self.labels["Digis"] = tk.Label(self, borderwidth=10)
        self.labels["Digis"].grid(row=0, column=0, padx=20, pady=20)
        self.labels["Digis"]["text"] = "This for the Digis"

    def actions(self, action):
        return_variable = action
        if(action == "Send"):
            print(self.fields["Digis"].get("1.0", tk.END))
            self.create_sms(self.get_cat_facts(), str(self.fields["Digis"].get("1.0", tk.END)))
        if (action == "Reset"):
            print(self.get_cat_facts())
        if (action == "I'm Feeling Lucky"):
            print(self.fields["I'inm Feeling Lucky"].get("1.0", tk.END))

    def create_sms(self, text, phone_number):
        account_sid = "ACbd13656fb018e71092b5c0eb82e6a371"
        auth_token = "dea57a59754bea5bd4f758fce3cbb24d"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body= text,
            from_='+16099007521',
            to=phone_number
        )

        print(message.sid)

    def get_cat_facts(self):
        return requests.get(url="https://catfact.ninja/fact").json()["fact"]


root = tk.Tk(className="Cat Facts")
root.geometry("525x525")
app = gui_stuff(master=root)
app.mainloop()