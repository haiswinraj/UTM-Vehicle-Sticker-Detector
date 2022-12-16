from datetime import datetime
from tkinter import *
from tkinter import ttk
import DetailsScreen as details
from controller.Database import mydb
from controller.HistoryController import HistoryController as HC


class HistoryScreen:
    def __init__(self, window):
        self.window = window

        window_height = 640
        window_width = 1100

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.resizable(0, 0)
        self.window.state('normal')
        self.window.title('STICKER HISTORY')
        self.window.config(background='#780808')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("yu gothic ui", 11, "bold"))

        # 1. SEARCH FUNTIONALITIES ============================================================================================================================================================================================

        self.username_label = Label(self.window, text = "Search by license plate number", bg = "#780808", fg="white", font=("yu gothic ui", 13))
        self.username_label.place(x = 9, y = 10)

        self.search_entry = Entry(self.window, highlightthickness = 0, relief = FLAT, bg = "white", fg="black", font=("yu gothic ui ", 12))
        self.search_entry.place(x = 11, y = 40, width = 310)

        self.login = Button(self.window, text = 'Search', font = ("yu gothic ui", 9, "bold"), width=10, bd=0, bg='#ffa90a', cursor='hand2', activebackground='#ffa90a', fg='white', command=self.search)
        self.login.place(x = 330, y = 40)

        self.u_label = Label(self.window, text=" ", bg="#780808", fg="white", font=("yu gothic ui", 9, "bold"))
        self.u_label.place(x=410, y=40)

        self.login = Button(self.window, text = 'All', font = ("yu gothic ui", 9, "bold"), width=5, bd=0, bg='#ffa90a', cursor='hand2', activebackground='#ffa90a', fg='white', command=self.showAll)
        self.login.place(x = 1040, y = 40)

        # 2. TABLE ============================================================================================================================================================================================================

        self.scrollbarx = Scrollbar(self.window, orient = HORIZONTAL)
        self.scrollbary = Scrollbar(self.window, orient = VERTICAL)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 13))  # Modify the font of the headings

        self.my_tree = ttk.Treeview(self.window, style="mystyle.Treeview")
        self.my_tree.place(relx = 0.01, rely = 0.128, width = 1050, height = 510)
        self.my_tree.configure(yscrollcommand = self.scrollbary.set, xscrollcommand = self.scrollbarx.set)
        self.my_tree.configure(selectmode = "extended")

        self.scrollbary.configure(command = self.my_tree.yview)
        self.scrollbarx.configure(command = self.my_tree.xview)

        self.scrollbary.place(x = 1061, y = 82, width = 22, height = 510)
        self.scrollbarx.place(x = 12, y = 592, width = 1070, height = 22)

        self.my_tree.configure(
            columns=(
                "Serial No",
                "Car",
                "No Plate",
                "Date",
                "Time",
                "Status"
            )
        )

        self.my_tree.heading("#0", text="Owner", anchor=W)
        self.my_tree.heading("Serial No", text="Serial No", anchor=W)
        self.my_tree.heading("Car", text="Car", anchor=W)
        self.my_tree.heading("No Plate", text="No Plate", anchor=W)
        self.my_tree.heading("Date", text="Date", anchor=W)
        self.my_tree.heading("Time", text="Time", anchor=W)
        self.my_tree.heading("Status", text="Status", anchor=W)

        self.my_tree.column('#0', stretch=NO, minwidth=0, width=150)
        self.my_tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.my_tree.column('#2', stretch=NO, minwidth=0, width=180)
        self.my_tree.column('#3', stretch=NO, minwidth=0, width=160)
        self.my_tree.column('#4', stretch=NO, minwidth=0, width=160)
        self.my_tree.column('#5', stretch=NO, minwidth=0, width=160)
        self.my_tree.column('#6', stretch=NO, minwidth=0, width=160)
        self.serial_key = ""

        self.my_tree.bind("<Double-1>", self.clicker)

        self.showAll()

    def clicker(self, e):
        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')
        win = Toplevel(self.window)

        history_controller = HC()
        details.DetailsScreen(win, values, history_controller)
        # win.grab_set()

    def search(self):

        search = self.search_entry.get()

        mycursor = mydb.cursor(buffered=True)

        mycursor.execute("SELECT * FROM History WHERE vehicle_no='" + search + "' ORDER BY history_id desc" )

        rowcount = mycursor.rowcount

        print(rowcount)

        if rowcount > 0:
            i = 0

            for record in self.my_tree.get_children():
                self.my_tree.delete(record)

            for row in mycursor:
                self.my_tree.insert(parent='', index='end', text=row[8].upper(), iid=i, values=(row[4], row[2], row[3], row[5], row[6], row[7].upper()))
                i+=1
        else:
            self.u_label.config(text="Try again")

    def showAll(self):

        if len(self.my_tree.get_children()) > 0:
            for record in self.my_tree.get_children():
                self.my_tree.delete(record)

        mycursor = mydb.cursor(buffered=True)

        print(datetime.date(datetime.now()).strftime("%Y-%m-%d"))

        current_date = datetime.date(datetime.now()).strftime("%Y-%m-%d")

        mycursor.execute("SELECT * FROM History WHERE date='" + current_date + "' ORDER BY history_id desc")

        i = 0

        for row in mycursor:
            self.my_tree.insert(parent='', index='end', text=row[8].upper(), iid=i, values=(row[4], row[2], row[3], row[5], row[6], row[7].upper()))
            i+=1

       