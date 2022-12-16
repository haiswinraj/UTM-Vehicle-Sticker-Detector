from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Style
from tkinter.ttk import Progressbar
import sys
import LoginScreen as login

i = 0


class LoadingScreen:
	def __init__(self, window):
		self.window = window
		window_height = 430
		window_width = 530

		screen_width = self.window.winfo_screenwidth()
		screen_height = self.window.winfo_screenheight()

		x_cordinate = int((screen_width/2) - (window_width/2))
		y_cordinate = int((screen_height/2) - (window_height/2))

		self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

		# self.window.eval('tk::PlaceWindow . center')
		self.window.wm_attributes('-topmost', True)           
		self.window.wm_attributes('-alpha', 1)
		self.window.overrideredirect(1)
		self.window.config(background='white')

		self.exit_btn = Button(self.window, text='X', command=self.exit_window, font=("yu gothic ui", 13, 'bold'), fg='#780808', bg='white', bd=0, activebackground = 'white')

		self.exit_btn.place(x=490, y=0)

		self.welcome_label = Label(self.window, text='WELCOME TO', font=("yu gothic ui", 13, 'bold'), fg='#780808', bg='white')
		self.welcome_label.place(x=195, y=15)
		self.welcome_label2 = Label(self.window, text='UTM VEHICLE STICKER DETECTION SYSTEM', font=("yu gothic ui", 13, 'bold'), fg='#780808', bg='white')
		self.welcome_label2.place(x=90, y=45)

		self.image = Image.open('assets/UTM-LOGO.png')
		newsize = (200, 200)
		self.image = self.image.resize(newsize)
		photo = ImageTk.PhotoImage(self.image)
		self.bg_label = Label(self.window, image=photo, bg='white')
		self.bg_label.image = photo
		self.bg_label.place(x=150, y=100)

		self.style = Style()
		self.style.theme_use('clam') 
		self.style.configure("1.Horizontal.TProgressbar", troughcolor ='#780808', background='#ffa90a')
		self.progress_label = Label(self.window, text='Loading ...', font=("yu gothic ui", 13, 'bold'), fg='#780808', bg='white')
		self.progress_label.place(x=210, y=325)

		self.progress = Progressbar(self.window, style='1.Horizontal.TProgressbar', orient=HORIZONTAL, length=500, mode='determinate')
		self.progress.place(x=15, y=350)
		self.loadBar()

	def exit_window(self):
		sys.exit(self.window.destroy())

	def top(self):
		win = Toplevel(self.window)
		login.LoginScreen(win)
		self.window.withdraw()
		win.deiconify()

	def loadBar(self):
		global i 

		if i <= 10:
			self.progress_label.after(100, self.loadBar)
			self.progress['value'] = 10*i
			i += 1
		else:
			self.top()

def page():
	window = Tk()
	LoadingScreen(window)
	window.resizable(True, True)
	window.mainloop()


if __name__ == '__main__':
	page()