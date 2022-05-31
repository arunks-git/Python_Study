import speech_recognition as sr
import pyttsx3
from netmiko import ConnectHandler

listener = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate' , 180)
speaker.setProperty('voice' ,'com.apple.speech.synthesis.voice.samantha')
listener.energy_threshold = 300
listener.pause_threshold = 0.8

router_list = [{"Name": 'matrix', "IP": '10.10.10.10'},
                   {"Name": 'oxygen', "IP": '20.20.20.20'},
                   {"Name": 'test', "IP": '10.219.38.6'}]

def initial_command():
    try:
        with sr.Microphone() as source:
            global statement
            statement = ' '
            listener.adjust_for_ambient_noise(source)
            print('listening')
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
            speaker.say('Hello..Please share the name of host to connect')
            speaker.runAndWait()
            print("Speak please....")
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
    output = net_connect.send_command('show version')
    print(output)
    speaker.say(f'Connected to {IP} . Please speak the command to check. Say exit to logout')
    speaker.runAndWait()

    con = True
    errors = ['syntax error', 'Invalid command', 'Unknown command']
    while con:
        next_command = initial_command()
        print(next_command)
        try:
            if next_command != 'exit':
                output = net_connect.send_command(next_command)
                print(output)
                if(any(x in output for x in errors)):
                    speaker.say('Sorry i didnt understand, try again')
                    speaker.runAndWait()
            else:
                net_connect.disconnect()
                con = False
        except:
            speaker.say('Sorry i didnt understand, try again')
            speaker.runAndWait()
    speaker.say('Logging out from Host. Good bye')
    speaker.runAndWait()
    exit()


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
            speaker.say('Sorry , I Cant find the host. Good Bye')
            speaker.runAndWait()
            break
        speaker.say('Connecting to Host')
        speaker.runAndWait()
        connect_device(IP1)
    else:
        pass

