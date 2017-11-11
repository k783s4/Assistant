import speech_recognition as sr
import pyautogui
import subprocess
r = sr.Recognizer()

#defining global variable

#end

def understand():
    with sr.Microphone() as source:
        aud = r.listen(source)
        try:
            return r.recognize_google(aud)
        except LookupError:
            return "Could not understand"

def slect():
    command = understand()                                                      #save what the user is saying
    commands = command.split("and")                                             #split in case there is more than one command (ex. press "x" and close window)
    print(commands)
    return commands
#-------------------------------------------------------------------------------
#                      SPACE FOR COMMANDS

def press(x):
    try:
        if " " not in x:
            pyautogui.press(x)
        else:
            xs = x.split(" ")
            pyautogui.hotkey(xs)                                                          #emulate a key press
    except:
        print("Whoops, %s is not a valid Argument!!" % (x))
def write(x):
    pyautogui.typewrite(x)
def search(x):
    x = x.replace("slash","/")
    x = x.replace(" ","")
    subprocess.call('Start "" "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe" ' + x, shell = True)

#                      END SPACE FOR COMMANDS
#-------------------------------------------------------------------------------

commands = slect()
for i in range(0,len(commands)):                                                #repeat the amount of commands
    #try:
        print("%s(%s)" %(commands[i].split(" ", 1)[0], commands[i].split(" ", 1)[1]))
        possibles = globals().copy()
        possibles.update(locals())
        if " " in commands[i]:                                                  #if the command contains an argument
            possibles.get(commands[i].split(" ", 1)[0])(commands[i].split(" ", 1)[1])#call the command function with the right parameters
        else:
            possibles.get(commands[i])()                                        #in case the command does not require an argument
    #except:                                                                     #catch in case there is no function available for the command or there was a misunderstanding
    #    print("Command for %s not found" % (commands[i]))                       #ERROR MESSAGES
