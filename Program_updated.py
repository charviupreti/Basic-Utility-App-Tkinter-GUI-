from tkinter import *
import datetime
import pywhatkit
import pytube
import winsound

# By Charvi Upreti 21BCE1440

# To send a whatsapp message


def Sendwhatappmessage():
    # Creating window for sending whatsapp message
    Whatsapp = Toplevel(homepage)
    Whatsapp.geometry("350x200")
    Whatsapp.title("Send a Message")
    # Creating label and enter space for writing the message to be delivered
    L1 = Label(Whatsapp, text="Message")
    L1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    Messagevar = Entry(Whatsapp, width=15)
    Messagevar.grid(row=1, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Creating label and enter space for writing the phone number where the message is to be delivered
    L2 = Label(Whatsapp, text="Number")
    L2.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    Numbervar = Entry(Whatsapp, width=15)
    Numbervar.insert(0,"+91")
    Numbervar.grid(row=2, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Creating label and enter space for writing the hour at which the message is to be delivered
    L3 = Label(Whatsapp, text="Hours")
    L3.grid(row=3, column=1, sticky=W, padx=5, pady=5)
    Hoursvar = Entry(Whatsapp, width=15)
    Hoursvar.grid(row=3, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Creating label and enter space for writing the minute at which the message is to be delivered
    L4 = Label(Whatsapp, text="Minutes")
    L4.grid(row=4, column=1, sticky=W, padx=5, pady=5)
    Minutesvar = Entry(Whatsapp, width=15)
    Minutesvar.grid(row=4, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Button to send the entered values to the sendmessage function to send the message
    Submit = Button(Whatsapp, text="Submit", command=lambda: sendmessage(Messagevar, Numbervar, Hoursvar, Minutesvar))
    Submit.grid(row=5, column=1, sticky=W, padx=5, pady=5)
    # Button to exit from the window
    exit_bttn = Button(Whatsapp, text="Exit Window", command=lambda: exit_app(Whatsapp))
    exit_bttn.grid(row=5, column=3, sticky=E, padx=5, pady=5)
    
def sendmessage(Messagevar, Numbervar, Hoursvar, Minutesvar):
    # Assigning the values from the entered values
    Message = Messagevar.get()
    Number = Numbervar.get()
    Hours = int(Hoursvar.get())
    Minutes = int(Minutesvar.get())
    # Clearing the input enter space after assigning the values
    Minutesvar.delete(0, 'end')
    Numbervar.delete(0, 'end')
    Hoursvar.delete(0, 'end')
    Messagevar.delete(0, 'end')
    WA.append([Message,Number,Hours,Minutes])
    display("Message has been scheduled to be sent")

# To play any random youttube video of a given topic
def PlayYoutube():
    # Creating the window for playing Youtube
    Youtube = Toplevel(homepage)
    Youtube.geometry("300x100")
    Youtube.title("Play a video")
    # Creating label and enter space for input of topic of the video
    L1 = Label(Youtube, text="Topic")
    L1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    Topicvar = Entry(Youtube, width=15)
    Topicvar.grid(row=1, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Button to send the entered values to the Youtubevideo  function to play the video
    Submit = Button(Youtube, text="Submit",command=lambda: Youtubevideo(Topicvar))
    Submit.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    # Button to exit from the window
    exit_bttn = Button(Youtube, text="Exit Window",command=lambda: exit_app(Youtube))
    exit_bttn.grid(row=2, column=3, sticky=E, padx=5, pady=5)
    
def Youtubevideo(Topicvar):
    # Assigning the values from the entered value
    Topic = Topicvar.get()
    # Clearing the input enter space after assigning the value
    Topicvar.delete(0, 'end')
    # Excecuting the playonyt command so that the Youtube video gets played
    try:
        pywhatkit.playonyt(Topic)
    except:
        display("Network Error Occured")


# to start a google search on the web browser
def search():
    # Creating window for performing a search on the google web browser
    Search = Toplevel(homepage)
    Search.geometry("400x100")
    Search.title("Google Search")
    # Creating label and enter space to take input of topic to search for
    L1 = Label(Search, text="Topic")
    L1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    Topicvar = Entry(Search, width=15)
    Topicvar.grid(row=1, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Button to send the entered values to the openwebbrowser function to search for on the google web browser
    Submit = Button(Search, text="Submit",command=lambda: openwebbrowser(Topicvar))
    Submit.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    # Button to exit from the window
    exit_bttn = Button(Search, text="Exit Window",command=lambda: exit_app(Search))
    exit_bttn.grid(row=2, column=3, sticky=E, padx=5, pady=5)
    
def openwebbrowser(Topicvar):
    # Assigning the values from the entered value
    Topic = Topicvar.get()
    # Clearing the input enter space after assigning the values
    Topicvar.delete(0, 'end')
    # Excecuting the search command so that the query is seaached on the web browser
    try:
        pywhatkit.search(Topic)
    except:
        display("An unknown error occured")

# To display text in handwritten format

def results():
    # Creating window for displaying text in handwritten format
    results = Toplevel(homepage)
    results.geometry("300x200")
    results.title("Text to handwriting Converter")
    # Creating label and enter space to take input text to convert
    L1 = Label(results, text="Text")
    L1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    textvar = Entry(results, width=15)
    textvar.grid(row=1, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Creating label and enter space to take input name of file to save the image as
    L1 = Label(results, text="Image name")
    L1.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    namevar = Entry(results, width=15)
    namevar.grid(row=2, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Button to send the entered values to the displayresults function to display first 4 lines of the search results
    Submit = Button(results, text="Submit",command=lambda: displayresults(textvar, namevar))
    Submit.grid(row=3, column=1, sticky=W, padx=5, pady=5)
    # Button to exit from the window
    exit_bttn = Button(results, text="Exit Window",command=lambda: exit_app(results))
    exit_bttn.grid(row=3, column=3, sticky=E, padx=5, pady=5)

def displayresults(textvar, namevar):
    # Assigning the values from the entered value
    text = textvar.get()
    name = namevar.get()+".png"
    # Clearing the input enter space after assigning the value
    textvar.delete(0, 'end')
    namevar.delete(0, 'end')
    # Excecuting the info command so that the search results get printed
    try:
        pywhatkit.text_to_handwriting(text, name, rgb=[0, 0, 0])
        display("Successfully converted")
    except:
        display("An Unknown Error Occured")

# Download a youttube video
def YTvideo():
    # Creating window for Downloading Youtube video
    ytvideo = Toplevel(homepage)
    ytvideo.geometry("400x100")
    ytvideo.title("Download a Video")
    # Creating label and enter space to input of the URL of the video to be downloaded
    L1 = Label(ytvideo, text="Enter URL of video to by downloaded")
    L1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    urlvar = Entry(ytvideo, width=15)
    urlvar.grid(row=1, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Button to send the entered values to the videodownloader function to download the video
    Submit = Button(ytvideo, text="Submit",command=lambda: videodownloader(urlvar))
    Submit.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    # Button to exit from the window
    exit_bttn = Button(ytvideo, text="Exit Window",command=lambda: exit_app(ytvideo))
    exit_bttn.grid(row=2, column=3, sticky=E, padx=5, pady=5)

def videodownloader(urlvar):
    # Assigning the values from the entered value
    url = urlvar.get()
    # Clearing the input enter space after assigning the value
    urlvar.delete(0, 'end')
    # Excecuting the command so that youtube video is downloaded
    try:
        video=pytube.YouTube(url)
        video.streams.get_highest_resolution().download()
        display("Successfully downloaded")
    except:
        display("An Unknown Error Occured")


# To download a youtube playlist
def YTPlaylist():
    # Creating window for Downloading Youtube playlist
    ytplay = Toplevel(homepage)
    ytplay.geometry("450x100")
    ytplay.title("Download a playlist")
    # Creating label and enter space to input of the URL of the playlist to be downloaded
    L1 = Label(ytplay, text="Enter URL of Playlist to be downloaded")
    L1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    urlvar = Entry(ytplay, width=15)
    urlvar.grid(row=1, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Button to send the entered values to the playlistdownloader function to download the playlist
    Submit = Button(ytplay, text="Submit",command=lambda: playlistdownloader(urlvar))
    Submit.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    # Button to exit from the window
    exit_bttn = Button(ytplay, text="Exit Window",command=lambda: exit_app(ytplay))
    exit_bttn.grid(row=2, column=3, sticky=E, padx=5, pady=5)


def playlistdownloader(urlvar):
    # Assigning the values from the entered value
    url = urlvar.get()
    # Clearing the input enter space after assigning the values
    urlvar.delete(0, 'end')
    # Excecuting the command so that youtube playlist is downloaded
    try:
        p = pytube.Playlist(url)
        for video in p.videos:
            video.streams.get_highest_resolution().download()
        display("Successfully downloaded")
    except:
        display("An Unknown Error Occured")


# To set up a simple alarm
def alarm():
    # Creating window for setting an alarm
    clock = Tk()
    clock.title("Alarm Clock")
    clock.geometry("300x200")
    clock.title("Set an alarm")
    # Creating label and enter space to input the time in hours of the alarm to be set
    L1 = Label(clock, text="Hour")
    L1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    hourTime = Entry(clock, width=15)
    hourTime.grid(row=1, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Creating label and enter space to input the time in minutes of the alarm to be set
    L2 = Label(clock, text="Min")
    L2.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    minTime = Entry(clock, width=15)
    minTime.grid(row=2, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Button to send the entered values to the Setalarm function to set an alarm for mentioned time
    submit = Button(clock, text="Submit",
                    command=lambda: Setalarm(hourTime, minTime))
    submit.grid(row=3, column=1, sticky=W, padx=5, pady=5)
    # Button to exit from the window
    exit_bttn = Button(clock, text="Exit Window",command=lambda: exit_app(clock))
    exit_bttn.grid(row=3, column=3, sticky=E, padx=5, pady=5)
    
def Setalarm(hourTime, minTime):
    # Assigning the values from the entered value
    alarmmin = minTime.get()
    alarmhour = hourTime.get()
    # Clearing the input enter space after assigning the values
    minTime.delete(0, 'end')
    hourTime.delete(0, 'end')
    display("Alarm has been set")
    # Excecuting the command so that the alarm is set
    Alarms.append([alarmhour,alarmmin])
    

# To search for webpage url's for a given topic
def webpages():
    # Creating window for searching for webpage url's for a given topic
    webpages = Toplevel(homepage)
    webpages.geometry("300x100")
    webpages.title("Print Searched URL's")
    # Creating label and enter space to input the topic to search for
    L1 = Label(webpages, text="Topic")
    L1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    queryvar = Entry(webpages, width=15)
    queryvar.grid(row=1, column=2, sticky=E, padx=5, pady=5, columnspan=2)
    # Button to send the entered values to the pages function to search for webpage url's for a given topic
    Submit = Button(webpages, text="Submit", command=lambda: pages(queryvar))
    Submit.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    # Button to exit from the window
    exit_bttn = Button(webpages, text="Exit Window", command=lambda: exit_app(webpages))
    exit_bttn.grid(row=2, column=3, sticky=E, padx=5, pady=5)


def pages(queryvar):
    # Assigning the values from the entered value
    query = queryvar.get()
    # Clearing the input enter space after assigning the values
    queryvar.delete(0, 'end')
    # Excecuting the search command so that youtube playlist is downloaded
    ans=[]
    try:
        from googlesearch import search
    except ImportError:
        display("No module named 'google' found")
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        ans.append(j)
    display(ans)

# To exit the window given in the function arguments
def exit_app(tobedestroyed):
    from tkinter import messagebox
    confirm = messagebox.askquestion(
        'Quit Confirmation', 'are you sure you want to quit?')
    if confirm.upper() == "YES":
        tobedestroyed.destroy()
    else:
        pass
#Display pop up when task is executed
def display(todisplay):
    from tkinter import messagebox
    messagebox.showinfo("Info", todisplay)

# Homepage set up
homepage = Tk()
homepage.title("Home Screen")
homepage.geometry("600x250")
# Button to excecute "Send a Whatapp Message"
One = Button(homepage, text=" Send message through Whatsapp ",width=35,command=lambda: Sendwhatappmessage())
One.grid(row=1, column=1, padx=5, pady=5)
# Button to excecute "Play a YouTube Video"
Two = Button(homepage, text="Play a YouTube Video",width=35,command=lambda: PlayYoutube())
Two.grid(row=1, column=2, padx=5, pady=5)
# Button to excecute "Search something on the web browser"
# Here google
Three = Button(homepage, text="Search something on the web browser",width=35,command=lambda: search())
Three.grid(row=2, column=1, padx=5, pady=5)
# Button to excecute "Display text in handwritten format"
Four = Button(homepage, text="Text to handwriting Converter",width=35,command=lambda: results())
Four.grid(row=2, column=2, padx=5, pady=5)
# Button to excecute "Display first few lines from Google search Result"
Five = Button(homepage, text="Download Youtube Video using URL",width=35,command=lambda: YTvideo())
Five.grid(row=3, column=1, padx=5, pady=5)
# Button to excecute "Download Youtube Playlist using URL"
six = Button(homepage, text="Download Youtube Playlist using URL",width=35,command=lambda: YTPlaylist())
six.grid(row=3, column=2, padx=5, pady=5)
# Button to excecute "Set Alarm"
seven = Button(homepage, text="Set up an alarm",width=35, command=lambda: alarm())
seven.grid(row=4, column=1, padx=5, pady=5)
# Button to excecute "Print few URL's From Google Search results"
eight = Button(homepage, text="Print few URL's From Google Search results",width=35,command=lambda: webpages())
eight.grid(row=4, column=2, padx=5, pady=5)
# Button to exit from the window
exit_bttn = Button(homepage, text="Exit app",command=lambda: exit_app(homepage))
exit_bttn.grid(row=5, column=2, padx=5, pady=5)

current = datetime.datetime.now()
current_hr = current.hour
current_minute = current.minute

def Time():
    global current_hr , current_minute
    current = datetime.datetime.now()
    current_hr = current.hour
    current_minute = current.minute
    homepage.after(200, lambda: Time())
    if current_hr>=10 and current_minute>=10:
        clock = Label(homepage,text="Time : {}:{}".format(current_hr,current_minute))
    elif current_hr<10 and current_minute>=10:
        clock = Label(homepage,text="Time : 0{}:{}".format(current_hr,current_minute))
    elif current_hr>=10 and current_minute<10:
        clock = Label(homepage,text="Time : {}:0{}".format(current_hr,current_minute))
    else:
        clock = Label(homepage,text="Time : 0{}:0{}".format(current_hr,current_minute))
        
    clock.grid(row=5, column=1)
Time()


freq = 700
dur = 500
Alarms = []
WA=[]
def background():
    global current_hr , current_minute
    if Alarms!=[]:
        for i in Alarms:
            alarmhour=i[0]
            alarmmin=i[1]
            if current_hr == int(alarmhour) and current_minute == int(alarmmin):
                for i in range(0, 3):
                    winsound.Beep(freq, dur)
                Alarms.remove([alarmhour,alarmmin])
    if WA!=[]:
        for i in WA:
            Message=i[0]
            Number=i[1]
            Hours=i[2]
            Minutes=i[3]
            if current_hr == int(Hours) and current_minute == int(Minutes)-1:
                # Excecuting the sendwhatmsg command so that the message gets delivered
                try:
                    pywhatkit.sendwhatmsg(Number, Message, Hours, Minutes)
                except:
                    # Printing Error Message
                    display("An unknown error occured")                
                WA.remove([Message,Number,Hours,Minutes])
    homepage.after(200, lambda: background())
background()

homepage.mainloop()
