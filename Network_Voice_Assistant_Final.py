from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
import threading
import speech_recognition as sr
import pyttsx3
from netmiko import ConnectHandler
from subprocess import call

listener = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate' , 180)
speaker.setProperty('voice' ,'com.apple.speech.synthesis.voice.samantha')
listener.energy_threshold = 300
listener.pause_threshold = 0.8

router_list = [{"Name": 'matrix', "IP": '10.10.10.10'},
				   {"Name": 'oxygen', "IP": '20.20.20.20'},
				   {"Name": 'test', "IP": '10.219.38.6'}]


def print_msg(msg):
	Label(root, text=msg , background="yellow").grid(row=6, column=1)


def initial_command():
	try:
		with sr.Microphone() as source:
			global statement
			statement = ' '
			listener.adjust_for_ambient_noise(source)
			print('listening')
			print_msg('      LISTENING MODE       ')
			voice = listener.listen(source,phrase_time_limit=4)
			statement = listener.recognize_google(voice)
			statement = statement.lower()
			print(statement)
			if statement == ' ':
				pass
			else:
				return statement

	except:
		pass
	return statement


def connect_command():
	try:
		with sr.Microphone() as source:
			listener.adjust_for_ambient_noise(source)
#           speaker.say('Hello..Please share the name of host to connect')
#           speaker.runAndWait()
			phrase = 'Hello..Please share the name of host to connect'
			call(['python3', 'test.py', phrase])
			print("Speak please....")
			print_msg('SPEAK THE HOST NAME..')
			voice = listener.listen(source, timeout=6, phrase_time_limit=4)
			host = listener.recognize_google(voice)
			return host
	except:
		print("Cant recognize the command")

def connect_device(IP):
	device_test = {
		'device_type': 'juniper',
		'host': IP,
		'username': 'labroot',
		'password': 'lab123',
		'port': 22,
	}

	net_connect = ConnectHandler(**device_test)
	cmd_out = net_connect.send_command('show version')
	output(cmd_out)
#   speaker.say(f'Connected to {IP} . Please speak the command to check. Say exit to logout')
#   speaker.runAndWait()
	msg = 'Connected to Host. Please instruct the command. Say exit to logout'
	Label(root, text=msg).grid(row=5, column=1)
	phrase = f'Connected to {IP} . Please speak the command to check. Say exit to logout'
	call(['python3', 'test.py', phrase])

	con = True
	errors = ['syntax error', 'Invalid command', 'Unknown command']
	while con:
		next_command = initial_command()
		print(next_command)
		try:
			if next_command != 'exit':
				cmd_out = net_connect.send_command(next_command)
				output(cmd_out)
				if(any(x in cmd_out for x in errors)):
					#speaker.say('Sorry i didnt understand, try again')
					#speaker.runAndWait()
					phrase = 'Sorry i didnt understand, try again'
					call(['python3', 'test.py', phrase])
			else:
				net_connect.disconnect()
				con = False
		except:
			#speaker.say('Sorry i didnt understand, try again')
			#speaker.runAndWait()
			phrase = 'Sorry i didnt understand, try again'
			call(['python3', 'test.py', phrase])
	#speaker.say('Logging out from Host. Good bye')
	#speaker.runAndWait()
	phrase = 'Logging out from Host. Good bye'
	call(['python3', 'test.py', phrase])
	exit()



def output(data1):
	text.insert(END , chars=data1)
	text.see(END)

def take_command():
	while True:
		command = initial_command()
		print(command)
		if 'juni' in command:
			host1 = connect_command()
			print(host1)
			for r in router_list:
				if r["Name"] == host1:
					IP1 = r["IP"]
					break
			else:
#				speaker.say('Sorry , I Cant find the host. Good Bye')
#				speaker.runAndWait()
				phrase = 'Sorry,I Cant find the host. Good Bye'
				call(['python3', 'test.py', phrase])
				break
#			speaker.say('Connecting to Host')
#			speaker.runAndWait()
			phrase = "Connecting to Host"
			call(['python3', 'test.py', phrase])
			connect_device(IP1)
		else:
			pass


root = Tk()
Frame(root, height=100).grid(row=0)
root.title("Juni -  Voice Assistant for Network Device")

img = Image.open("/Users/arunks/Downloads/juni_image.jpeg")
photo=ImageTk.PhotoImage(img)

plabel=Label(image=photo).place(x=220 , y=0)

Frame(root, height=100).grid(row=4)


#entry_dev = Entry(root)
#entry_dev.grid(row=1, column=1)
#entry_dev.insert(END, 'test')
#Label(root, text='Login:').grid(row=2, column=0)
#entry_user = Entry(root)
#entry_user.grid(row=2, column=1)
#entry_user.insert(END, 'test1')
#Label(root, text='Password:').grid(row=3, column=0)
#entry_pw = Entry(root, show='*')
#entry_pw.grid(row=3, column=1)
#entry_pw.insert(END, 'test3')

frame = Frame(root, width=800, height=700)
frame.grid(row=7, column=0, columnspan=4)
frame.grid_propagate(False)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
text = Text(frame, borderwidth=3)
text.config(font=('courier', 11), wrap='none')
text.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

scrollbarY = Scrollbar(frame, command=text.yview)
scrollbarY.grid(row=0, column=1, sticky='nsew')
text['yscrollcommand'] = scrollbarY.set
scrollbarX = Scrollbar(frame, orient=HORIZONTAL, command=text.xview)
scrollbarX.grid(row=1, column=0, sticky='nsew')
text['xscrollcommand'] = scrollbarX.set


threading.Thread(target=take_command).start()
root.mainloop()