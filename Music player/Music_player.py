def unmutemusic():
    global currentvol
    root.unMuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(currentvol)



def mutemusic():
    global currentvol
    root.MuteButton.grid_remove()
    root.unMuteButton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)


def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='Playing......')

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100


    # pass
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100


    # pass

def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stop Music......')
    # pass

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Pause......')


def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.MuteButton.grid()
    ProgressbarMusicLabel.grid()

    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.set_volume(0.4)
    mixer.music.play()
    AudioStatusLabel.configure(text='Playing......')

    Song = MP3(ad)
    totalsonglength = int(Song.info.length)
    ProgressbarMusic['maximum'] = totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progressbarmusictick():
        CurrentSongLength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = CurrentSongLength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()





def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='C:/Users/man19/Downloads/Music',
                                        title='Select Audio File',filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
        dd = filedialog.askopenfilename(title='Select Audio File',filetype=(('MP3','*.mp3'),('WAV','*.wav')))

    audiotrack.set(dd)

def createwidthes():
    global implay,imbrowse,imbrowse,imvolumeup,imvolumedown,imend,impause,imresume,immute,imunmute
    global AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel

    ###################### Images register###########################
    implay = PhotoImage(file='play.png')
    impause = PhotoImage(file='pause.png')
    imbrowse = PhotoImage(file='browsing.png')
    imvolumeup = PhotoImage(file='volume-up.png')
    imend = PhotoImage(file='end.png')
    imresume = PhotoImage(file='end.png')
    immute = PhotoImage(file='mute.png')
    imunmute = PhotoImage(file='play.png')

    imvolumedown = PhotoImage(file='volume-down.png')
    #########################Size of image change##############################
    implay = implay.subsample(20, 20)
    impause = impause.subsample(20, 20)
    imbrowse = imbrowse.subsample(20, 20)
    imvolumeup = imvolumeup.subsample(20, 20)
    imend = imend.subsample(20, 20)
    imvolumedown= imvolumedown.subsample(20, 20)
    imresume = imresume.subsample(20, 20)
    immute = immute.subsample(20, 20)
    imunmute = imunmute.subsample(20, 20)
    #################################################
    TrackLabel = Label(root,text="Select Audio Track :",bg='lightskyblue',font=('arial',15,'italic bold' ))
    TrackLabel.grid(row = 0,column =0,padx=20,pady=20)

    AudioStatusLabel = Label(root, text='', bg='lightskyblue', font=('arial', 15, 'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1)


    ##################################################
    TrackLabelEntry = Entry(root,font=('arial',16,'italic bold' ),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

    ##################################################
    BrowseButton = Button(root,text='Search',bg='deeppink',font=('arial',13,'italic bold' ),width=200,bd=5,activebackground='purple4',image=imbrowse,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)


    PlayButton = Button(root,text='Play',bg='yellow',font=('arial',13,'italic bold' ),width=200,bd=5,activebackground='purple4',image=implay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)


    root.PauseButton = Button(root,text='Pause',bg='blue',font=('arial',13,'italic bold' ),width=200,bd=5,activebackground='purple4' ,image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume',bg='yellow',font=('arial',13,'italic bold' ),width=200,bd=5,activebackground='purple4',image=imresume,compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    VolumeupButoon = Button(root,text='volumeUp',bg='green2',font=('arial',13,'italic bold' ),width=200,bd=5,activebackground='purple4',image=imvolumeup,compound=RIGHT ,command=volumeup)
    VolumeupButoon.grid(row=1,column=2,padx=20,pady=20)

    StopButoon = Button(root,text='Stop',bg='red',font=('arial',13,'italic bold' ),width=200,bd=5,activebackground='purple4',image=imend,compound=RIGHT,command=stopmusic)
    StopButoon.grid(row=2,column=0,padx=20,pady=20)


    VolumeDownButoon = Button(root,text='volumedown',bg='blue',font=('arial',13,'italic bold' ),width=200,bd=5,activebackground='purple4',image=imvolumedown,compound=RIGHT ,command=volumedown)
    VolumeDownButoon.grid(row=2,column=2,padx=20,pady=20)

    root.MuteButton = Button(root,text='Mute',bg='green2',font=('Comic Sans MS',13, ),width=100,bd=5,activebackground='purple4',image=immute,compound=RIGHT ,command=mutemusic)
    root.MuteButton.grid(row=3,column=3,padx=1,pady=1)
    root.MuteButton.grid_remove()

    root.unMuteButton = Button(root,text='UnMute',bg='green2',font=('Comic Sans MS',13, ),width=100,bd=5,activebackground='purple4',image=imunmute,compound=RIGHT,command=unmutemusic)
    root.unMuteButton.grid(row=3,column=3,padx=1,pady=1)
    root.unMuteButton.grid_remove()

#######################################Progress Bar Field#########################################################################################################################################################
    ProgressbarLabel = Label(root,text='',bg='blue')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()

    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=pvalue,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)
############################################# progress bar Music ############################################
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=3,column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient = HORIZONTAL, mode = 'determinate',value=0)
    ProgressbarMusic.grid(row=3,column=1,ipadx=370,ipady=2)


    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=3,column=2)



#############################Music Player created By Manish Kumar#############################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
from PIL import ImageTk,Image


root = Tk()
root.geometry('1100x500+200+50')
root.title('Simple Music Player')
root.iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')


##############################Global Variables ################
audiotrack= StringVar()
currentvol = 0
pvalue = 40
totalsonglength = 0
count = 0
text = ''
###################Silder Window ##############################
ss="Developed By Manish Kumar"

SliderLabel = Label(root,text=ss,bg='lightskyblue',font=('chiller',40,'italic bold' ))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text=text)
    count+=1
    SliderLabel.after(200,IntroLabelTrick)
IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()



