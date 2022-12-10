from customtkinter import *
from tkinter.messagebox import *

set_appearance_mode("dark")

root = CTk()
root.geometry("500x500")
root.title("PYTHON BANK LTD.")

class ATM:
    def __init__(self, parent):
        self.parent = parent
        self.balance = 0
        self.expression = ""
        self.input_text = StringVar()
        self.expression2 = ""
        self.input_text2 = StringVar()
        self.expression3 = ""
        self.input_text3 = StringVar()
        self.expression4 = ""
        self.input_text4 = StringVar()
        
##################
    def click_Start(self):
        self.win1_frame.pack_forget()
        self.addWindow_2()

    def addWindow_1(self):
        self.win1_frame = CTkFrame(master=self.parent)
        self.win1_frame.pack(fill=BOTH, expand=True)

        self.win1_label =CTkLabel(master=self.win1_frame, text="Welcome To Our ATM Service.",font=("Helvatica", 20))
        self.win1_label.grid(row=0, padx=110, pady=30)

        self.win1_button = CTkButton(master=self.win1_frame, text="Start", command=self.click_Start, width=150, height=50, corner_radius=25, font=("Helvatica", 20))
        self.win1_button.grid(row=1, padx=110)

###########################
    def addWindow_2(self):
        self.win2_frame = CTkFrame(master=self.parent)
        self.win2_frame.pack(expand= True, fill= BOTH)

        self.win2_label = CTkLabel(master=self.win2_frame, text="If you have card then click on YES.", font=("Helvatica", 20))
        self.win2_label.grid(padx=90, pady=10)

        self.win2_button1 = CTkButton(master=self.win2_frame, text="YES", command=self.click_Yes, width=100, height=50, corner_radius=25, font=("Helvatica", 20))
        self.win2_button1.grid(padx=10, pady=10)
        self.win2_button2 = CTkButton(master=self.win2_frame, text="NO", command=self.click_No, width=100, height=50, corner_radius=25, font=("Helvatica", 20))
        self.win2_button2.grid(padx=10, pady=10)

    def click_Yes(self):
        self.win2_frame.pack_forget()
        self.addWindow_3()

    def click_No(self):
        self.parent.quit()

###########################
    def addWindow_3(self):
        self.win3_frame = CTkFrame(master=self.parent)
        self.win3_frame.pack(expand= True, fill= BOTH)

        self.win3_label = CTkLabel(master=self.win3_frame, text="Set a New PIN", font=("helvatica", 30))
        self.win3_label.grid(columnspan=3, padx=10, pady=10)

        self.numPad1()

    def pin_Capture(self):
        self.pin_final = self.pinset_entry1.get()
        if len(self.pin_final) == 4:
            self.win3_frame.pack_forget()
            self.addWindow_4()
        else:
            showwarning("Warning", "Please Set a 4 Digit PIN!!!")



    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_clear1(self):
        self.expression = ""
        self.input_text.set("")


    def numPad1(self):
        numpad_frame1 = CTkFrame(master=self.win3_frame)
        numpad_frame1.grid(padx=25, pady=25)

        self.pinset_entry1 = CTkEntry(master=numpad_frame1, textvariable=self.input_text, font=("helvatica", 30, "bold"), justify=CENTER, corner_radius=20, fg_color="black", width=200)
        self.pinset_entry1.grid(row=0, columnspan=3, padx=10, pady=10, ipadx=80, ipady=20)

        one = CTkButton(master=numpad_frame1, text="1", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(1))
        one.grid(row=2, column=0, padx=5, pady=5)
        two = CTkButton(master=numpad_frame1, text="2", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(2))
        two.grid(row=2, column=1, padx=5, pady=5)
        three = CTkButton(master=numpad_frame1, text="3", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(3))
        three.grid(row=2, column=2, padx=5, pady=5)

        four = CTkButton(master=numpad_frame1, text="4", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(4))
        four.grid(row=3, column=0, padx=5, pady=5)
        five = CTkButton(master=numpad_frame1, text="5", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(5))
        five.grid(row=3, column=1, padx=5, pady=5)
        six = CTkButton(master=numpad_frame1, text="6", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(6))
        six.grid(row=3, column=2, padx=5, pady=5)

        seven = CTkButton(master=numpad_frame1, text="7", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(7))
        seven.grid(row=4, column=0, padx=5, pady=5)
        eight = CTkButton(master=numpad_frame1, text="8", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(8))
        eight.grid(row=4, column=1, padx=5, pady=5)
        nine = CTkButton(master=numpad_frame1, text="9", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click(9))
        nine.grid(row=4, column=2, padx=5, pady=5)

        clear = CTkButton(master=numpad_frame1, text="CLEAR", width=150, height=50, corner_radius=25,font=("helvatica", 20), fg_color="light coral", command=lambda: self.btn_clear1())
        clear.grid(row=5, column=0, padx=5, pady=5)
        zero = CTkButton(master=numpad_frame1, text="0", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(0))
        zero.grid(row=5, column=1, padx=5, pady=5)
        confirm = CTkButton(master=numpad_frame1, text="CONFIRM", width=150, height=50, corner_radius=25, font=("helvatica", 20, "bold"), fg_color='green', command=self.pin_Capture)
        confirm.grid(row=5, column=2, padx=5, pady=5)

    ########################
    def addWindow_4(self):
        self.win4_frame = CTkFrame(master=self.parent)
        self.win4_frame.pack()

        self.win4_label1 = CTkLabel(master=self.win4_frame, text="Enter your PIN", font=("helvatica", 30))
        self.win4_label1.grid(padx=10, pady=10)

        self.numPad2()

    def pin_Matching(self):
        entered_pin = self.win4_entry.get()
        if self.pin_final == entered_pin:
            self.win4_frame.pack_forget()
            self.addWindow_5()
        else:
            showerror("PIN Error", "Please Enter The Correct PIN!!!")

    def btn_click2(self, item):
        self.expression2 = self.expression2 + str(item)
        self.input_text2.set(self.expression2)

    def btn_clear2(self):
        self.expression2 = ""
        self.input_text2.set("")


    def numPad2(self):
        numpad_frame2 = CTkFrame(master=self.win4_frame)
        numpad_frame2.grid(padx=25, pady=25)

        self.win4_entry = CTkEntry(master=numpad_frame2, textvariable=self.input_text2, font=("helvatica", 30, "bold"), justify=CENTER, corner_radius=20, fg_color="black", width=200)
        self.win4_entry.grid(row=0, columnspan=3, padx=10, pady=10, ipadx=80, ipady=20)

        one = CTkButton(master=numpad_frame2, text="1", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(1))
        one.grid(row=1, column=0, padx=5, pady=5)
        two = CTkButton(master=numpad_frame2, text="2", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(2))
        two.grid(row=1, column=1, padx=5, pady=5)
        three = CTkButton(master=numpad_frame2, text="3", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(3))
        three.grid(row=1, column=2, padx=5, pady=5)

        four = CTkButton(master=numpad_frame2, text="4", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(4))
        four.grid(row=2, column=0, padx=5, pady=5)
        five = CTkButton(master=numpad_frame2, text="5", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(5))
        five.grid(row=2, column=1, padx=5, pady=5)
        six = CTkButton(master=numpad_frame2, text="6", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(6))
        six.grid(row=2, column=2, padx=5, pady=5)

        seven = CTkButton(master=numpad_frame2, text="7", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(7))
        seven.grid(row=3, column=0, padx=5, pady=5)
        eight = CTkButton(master=numpad_frame2, text="8", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(8))
        eight.grid(row=3, column=1, padx=5, pady=5)
        nine = CTkButton(master=numpad_frame2, text="9", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(9))
        nine.grid(row=3, column=2, padx=5, pady=5)

        clear = CTkButton(master=numpad_frame2, text="CLEAR", width=150, height=50, corner_radius=25, font=("helvatica", 20), fg_color="light coral", command=lambda: self.btn_clear2())
        clear.grid(row=4, column=0, padx=5, pady=5)
        zero = CTkButton(master=numpad_frame2, text="0", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click2(0))
        zero.grid(row=4, column=1, padx=5, pady=5)
        confirm = CTkButton(master=numpad_frame2, text="CONFIRM", width=150, height=50, corner_radius=25,font=("helvatica", 20, "bold"), fg_color='green', command=self.pin_Matching)
        confirm.grid(row=4, column=2, padx=5, pady=5)


#############################
    def addWindow_5(self):
        self.win5_frame = CTkFrame(master=self.parent)
        self.win5_frame.pack()

        self.win5_label1 = CTkLabel(master=self.win5_frame, text="Choose An Option", font=("helvatica", 30, "italic"))
        self.win5_label1.grid(columnspan=2, row=0, padx=10, pady=10)

        self.win5_button1 = CTkButton(master=self.win5_frame, text="WITHDRAWAL", command=lambda :self.withdrawal(), font=("helvatica", 20), height=50, width=200, corner_radius=10)
        self.win5_button1.grid(column=0, row=1, padx=10, pady=30, sticky=W)

        self.win5_button2 = CTkButton(master=self.win5_frame, text="DEPOSIT", command=lambda :self.deposite(), font=("helvatica", 20), height=50, width=200, corner_radius=10)
        self.win5_button2.grid(column=0, row=2, padx=10, pady=30)

        self.win5_button3 = CTkButton(master=self.win5_frame, text="CHECK BALANCE",  command=lambda :self.check_balance(), font=("helvatica", 20), height=50, width=200, corner_radius=10)
        self.win5_button3.grid(column=1, row=1, padx=10, pady=30)

        self.win5_button4 = CTkButton(master=self.win5_frame, text="EXIT", command=lambda :self.parent.quit(), font=("helvatica", 20), height=50, width=200, corner_radius=10)
        self.win5_button4.grid(column=1, row=2, padx=10, pady=30)


    def withdrawal(self):
        self.win5_frame.pack_forget()
        self.addWindow_5_1()

    def deposite(self):
        self.win5_frame.pack_forget()
        self.addWindow_5_3()

    def check_balance(self):
        self.win5_frame.pack_forget()
        self.addWindow_5_2()

##############################
    def addWindow_5_1(self):
        self.win5_1_frame = CTkFrame(master=self.parent)
        self.win5_1_frame.pack()

        self.win5_1_label1 = CTkLabel(master=self.win5_1_frame, text="Enter an Amount", font=("helvatica", 30, "italic"))
        self.win5_1_label1.grid(padx=10, pady=10)

        self.numPad3()



    def cash_collect(self):
        entered_amount = self.win5_1_entry1.get()
        if int(self.balance) < int(entered_amount):
            showwarning("Warning", f"Insufficient Funds!!!\nYour Balance is Rs.{self.balance}.")
        else:
            self.balance = int(self.balance) - int(entered_amount)
            self.win5_1_frame.pack_forget()
            self.addWindow_5_1_1()

    def btn_click3(self, item):
        self.expression3 = self.expression3 + str(item)
        self.input_text3.set(self.expression3)

    def btn_clear3(self):
        self.expression3 = ""
        self.input_text3.set("")


    def numPad3(self):
        numpad_frame3 = CTkFrame(master=self.win5_1_frame)
        numpad_frame3.grid(padx=25, pady=25)

        self.win5_1_entry1 = CTkEntry(master=numpad_frame3, textvariable=self.input_text3, font=("helvatica", 30, "bold"), justify=CENTER, corner_radius=20, fg_color="black", width=200)
        self.win5_1_entry1.grid(row=0, columnspan=3, padx=10, pady=10, ipadx=80, ipady=20)

        self.win5_1_label2 = CTkLabel(master=numpad_frame3, text="Rs.",font=("helvatica", 30, "italic"), fg_color="black")
        self.win5_1_label2.grid(padx=10, pady=10, row=0, column=0)

        one = CTkButton(master=numpad_frame3, text="1", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(1))
        one.grid(row=1, column=0, padx=5, pady=5)
        two = CTkButton(master=numpad_frame3, text="2", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(2))
        two.grid(row=1, column=1, padx=5, pady=5)
        three = CTkButton(master=numpad_frame3, text="3", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(3))
        three.grid(row=1, column=2, padx=5, pady=5)

        four = CTkButton(master=numpad_frame3, text="4", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(4))
        four.grid(row=2, column=0, padx=5, pady=5)
        five = CTkButton(master=numpad_frame3, text="5", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(5))
        five.grid(row=2, column=1, padx=5, pady=5)
        six = CTkButton(master=numpad_frame3, text="6", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(6))
        six.grid(row=2, column=2, padx=5, pady=5)

        seven = CTkButton(master=numpad_frame3, text="7", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(7))
        seven.grid(row=3, column=0, padx=5, pady=5)
        eight = CTkButton(master=numpad_frame3, text="8", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(8))
        eight.grid(row=3, column=1, padx=5, pady=5)
        nine = CTkButton(master=numpad_frame3, text="9", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(9))
        nine.grid(row=3, column=2, padx=5, pady=5)

        clear = CTkButton(master=numpad_frame3, text="CLEAR", width=150, height=50, corner_radius=25, font=("helvatica", 20), fg_color="light coral", command=lambda: self.btn_clear3())
        clear.grid(row=4, column=0, padx=5, pady=5)
        zero = CTkButton(master=numpad_frame3, text="0", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click3(0))
        zero.grid(row=4, column=1, padx=5, pady=5)
        confirm = CTkButton(master=numpad_frame3, text="CONFIRM", width=150, height=50, corner_radius=25,font=("helvatica", 20, "bold"), fg_color='green', command=lambda :self.cash_collect())
        confirm.grid(row=4, column=2, padx=5, pady=5)


################################
    def addWindow_5_1_1(self):
        self.win5_1_1_frame = CTkFrame(master=self.parent)
        self.win5_1_1_frame.pack()

        self.win5_1_1_label1 = CTkLabel(master=self.win5_1_1_frame, text="Please Collect Your Cash.", font=("helvatica", 22))
        self.win5_1_1_label1.grid(padx=10, pady=10)

        self.win5_1_1_label1 = CTkLabel(master=self.win5_1_1_frame, text=f"Your Account Balance Is Rs.{self.balance}", font=("helvatica", 25, "bold"))
        self.win5_1_1_label1.grid(padx=10, pady=10)

        self.win5_1_1_label1 = CTkLabel(master=self.win5_1_1_frame, text="Thank You For Using Our Services.\nSee You Soon!!!", font=("helvatica", 20))
        self.win5_1_1_label1.grid(padx=10, pady=10)

        self.win5_1_1_button1 = CTkButton(master=self.win5_1_1_frame, text="EXIT", command=lambda: self.parent.quit(), corner_radius=25, width=150, height=50, font=("helvatica", 20))
        self.win5_1_1_button1.grid(padx=10, pady=10)

##################

    def addWindow_5_2(self):
        self.win5_2_frame = CTkFrame(master=self.parent)
        self.win5_2_frame.pack(padx=20, pady=20)

        self.win5_2_label1 = CTkLabel(master=self.win5_2_frame, text=f"Your Account Balance Is Rs.{self.balance}", font=("helvatica", 20))
        self.win5_2_label1.grid(padx=15, pady=15)

        self.win5_2_button1 = CTkButton(master=self.win5_2_frame, text="BACK", command=lambda: self.click_back_5_2(), font=("helvatica", 20), corner_radius=25, width=150, height=50)
        self.win5_2_button1.grid(padx=15, pady=15)

        self.win5_2_button1 = CTkButton(master=self.win5_2_frame, text="EXIT", command=lambda: self.parent.quit(), font=("helvatica", 20), corner_radius=25, width=150, height=50)
        self.win5_2_button1.grid(padx=15, pady=15)

    def click_back_5_2(self):
        self.win5_2_frame.pack_forget()
        self.addWindow_5()

######################
    def click_deposite(self):
        deposite_amount = self.win5_3_entry1.get()
        if deposite_amount.isnumeric():
            self.balance = int(self.balance) + int(deposite_amount)
            self.win5_3_frame.pack_forget()
            self.addWindow_5()
            self.btn_clear4()
        else:
            self.win5_3_label2 = CTkLabel(master=self.win5_3_frame, text=f"Please Enter a Valid Amount.", font=("helvatica", 15))
            self.win5_3_label2.grid(padx=10, pady=10)

    def click_back_5_3(self):
        self.win5_3_frame.pack_forget()
        self.addWindow_5()

    def btn_click4(self, item):
        self.expression4 = self.expression4 + str(item)
        self.input_text4.set(self.expression4)

    def btn_clear4(self):
        self.expression4 = ""
        self.input_text4.set("")

    def addWindow_5_3(self):
        self.win5_3_frame = CTkFrame(master=self.parent)
        self.win5_3_frame.pack()

        self.win5_3_label1 = CTkLabel(master=self.win5_3_frame, text=f"Your Account Balance Is Rs.{self.balance}", font=("helvatica", 20))
        self.win5_3_label1.grid(padx=10, pady=10, columnspan=3, row=0)

        self.numPad4()

    def numPad4(self):
        numpad_frame4 = CTkFrame(master=self.win5_3_frame)
        numpad_frame4.grid(padx=25, pady=25)

        self.win5_3_entry1 = CTkEntry(master=numpad_frame4, textvariable=self.input_text4, font=("helvatica", 30, "bold"), justify=CENTER, corner_radius=20, fg_color="black", width=200)
        self.win5_3_entry1.grid(row=0, columnspan=3, padx=10, pady=10, ipadx=80, ipady=20)

        self.win5_3_label2 = CTkLabel(master=numpad_frame4, text="Rs.",font=("helvatica", 30, "italic"), fg_color="black")
        self.win5_3_label2.grid(padx=10, pady=10, row=0, column=0)

        one = CTkButton(master=numpad_frame4, text="1", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(1))
        one.grid(row=1, column=0, padx=5, pady=5)
        two = CTkButton(master=numpad_frame4, text="2", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(2))
        two.grid(row=1, column=1, padx=5, pady=5)
        three = CTkButton(master=numpad_frame4, text="3", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(3))
        three.grid(row=1, column=2, padx=5, pady=5)

        four = CTkButton(master=numpad_frame4, text="4", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(4))
        four.grid(row=2, column=0, padx=5, pady=5)
        five = CTkButton(master=numpad_frame4, text="5", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(5))
        five.grid(row=2, column=1, padx=5, pady=5)
        six = CTkButton(master=numpad_frame4, text="6", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(6))
        six.grid(row=2, column=2, padx=5, pady=5)

        seven = CTkButton(master=numpad_frame4, text="7", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(7))
        seven.grid(row=3, column=0, padx=5, pady=5)
        eight = CTkButton(master=numpad_frame4, text="8", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(8))
        eight.grid(row=3, column=1, padx=5, pady=5)
        nine = CTkButton(master=numpad_frame4, text="9", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(9))
        nine.grid(row=3, column=2, padx=5, pady=5)

        clear = CTkButton(master=numpad_frame4, text="CLEAR", width=150, height=50, corner_radius=25, font=("helvatica", 20), fg_color="light coral", command=lambda: self.btn_clear4())
        clear.grid(row=4, column=0, padx=5, pady=5)
        zero = CTkButton(master=numpad_frame4, text="0", width=90, height=50, corner_radius=25,font=("helvatica", 30, "bold"), command=lambda: self.btn_click4(0))
        zero.grid(row=4, column=1, padx=5, pady=5)
        deposit = CTkButton(master=numpad_frame4, text="DEPOSIT", width=150, height=50, corner_radius=25, font=("helvatica", 20, "bold"), fg_color='green', command=lambda: self.click_deposite())
        deposit.grid(row=4, column=2, padx=5, pady=5)

        self.win5_3_button2 = CTkButton(master=numpad_frame4, text="BACK", command=lambda: self.click_back_5_3(), corner_radius=25, width=150, height=50, font=("helvatica", 20))
        self.win5_3_button2.grid(padx=10, pady=10, row=5, columnspan=3)

        
        

w1 = ATM(root)
w1.addWindow_1()

root.mainloop()
