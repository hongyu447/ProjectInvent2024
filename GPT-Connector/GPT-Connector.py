from Modes.gameMode import gameMode
from Modes.storyMode import storyMode
from Modes.distress import distressMode

from TTS import ttsPlay
from speech_to_text import speech_to_text
from gptMessagePrepare import prepare_message

import sensitiveData

iprompt = []
assert1={"role": "system", "content": "You are a frined of a nine year old boy"}
assert2={"role": "assistant", "content": "You are to act and talk the way a younger child would to his friends"}
iprompt.append(assert1)
iprompt.append(assert2)

#1 for typing 0 for speaking
inputType = 0

#-----CONFIG FOR DISTRESS MODE------
email = sensitiveData.emailAddress
password = sensitiveData.emailPassword
gaurdianEmail = sensitiveData.userContactAddress #put this in sensitiveData as to not expose anyones private number
#---------------------------------------------

while(True):

    iprompt,text,functionCalled=prepare_message(iprompt,inputType) #preparing the messages for ChatGPT
    print("Function called:", functionCalled)
    print("ChatGPT response:",text)

    if functionCalled == "distress":
        distressMode(email,password,gaurdianEmail)

    if functionCalled == "game":
        gameMode(inputType)

    if functionCalled == "story":
        storyMode(inputType)
