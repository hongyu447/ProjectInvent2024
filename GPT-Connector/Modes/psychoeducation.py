import random
import sys

sys.path.append('../')

from TTS import ttsPlay
from gptMessagePrepare import prepare_message


def psychoeducation(inputType, button):
    topic = chooseTopic(inputType, button)
    if topic == "Anxiety":
        return AnxietyTopic(inputType, button, topic)
    elif topic in ["story", "stop", "distress", "coping"]:
        return topic

    


def chooseTopic(inputType, button):
    message = "What is a psychoeducation topic you would like to learn: "
    print("OWL response:", message)
    ttsPlay(message)
    iprompt = []
    assert1 = {"role": "system", "content": "You are an ai friend of a child"}
    assert2 = {"role": "assistant",
               "content": "You are attempting to find out what psychoeducation module a child wants to learn"}
    iprompt.append(assert1)
    iprompt.append(assert2)
    topic = None
    while topic == None:
        _, _, topic = prepare_message(iprompt, inputType, selectGameTools, button=button)

    return topic


def AnxietyTopic(inputType, button=None, topic):
    iprompt = []
    assert1 = {"role": "system", "content": "You are an ai friend to a child"}


    content = f"""You are now a child psychoeducation teacher. Your job is to teach a child with mental struggles about anxiety through a blend of lecturing and conversation when the child talks to you."""

    assert2 = {"role": "assistant", "content": content}

    iprompt.append(assert1)
    iprompt.append(assert2)
    iprompt.append({"role": "user", "content": "What is anxiety? I want to learn!"})
    iprompt, text, functionCalled = prepare_message(iprompt, 2, noTools)
    while True:
        

        content = f"""You are now a child psychoeducation teacher. Your job is to teach a child with mental struggles about anxiety through a blend of lecturing and conversation when the child talks to you. The information you have to teach is here: Anxiety is a feeling that everyone experiences sometimes. It happens when you feel nervous, worried, or scared about something. Anxiety is your brain’s way of keeping you safe, but sometimes it can make you feel this way even when there is no real danger.

Your brain has a special part called the amygdala that helps protect you. When it thinks something might be dangerous, it sends a signal to your body to get ready to fight, run away, or freeze—this is called the fight-flight-freeze response. Your heart might beat faster, your muscles might feel tense, and you might feel like you need to take quick breaths. This is your body’s way of preparing to deal with danger. But sometimes, your brain makes a mistake and reacts this way even when things are actually okay.

Anxiety can feel different for everyone, but some common feelings include a fast heartbeat, sweaty hands, dizziness, a knot in your stomach, having lots of worried thoughts, or wanting to avoid certain things because they make you nervous.

Some anxiety is actually a good thing. It helps you focus when you need to take a test or keeps you safe when crossing the street. But when anxiety happens too often or feels too big, it can make things harder instead of helping.

The good news is that you can learn ways to calm down when anxiety feels too strong. Deep breathing can help by slowing your heartbeat and telling your brain you are safe. Try breathing in slowly through your nose for four seconds, holding it for four seconds, and breathing out through your mouth for four seconds. Grounding techniques can also help. When you feel anxious, look around and name five things you can see, four things you can touch, three things you can hear, two things you can smell, and one thing you can taste. This helps bring your focus to the present moment.

Another helpful trick is positive self-talk. Instead of thinking, “I can’t do this,” try saying, “I can try my best.” Changing your thoughts can help you feel more confident. Talking about anxiety with a trusted adult can also make a big difference. You don’t have to handle it alone.

Remember, anxiety is a normal feeling, and everyone experiences it sometimes. With practice, you can learn ways to manage it and feel more in control."""

        assert2 = {"role": "assistant", "content": content}
        iprompt[1] = assert2

        iprompt, text, functionCalled = prepare_message(iprompt, inputType, ##triviaTools,
                                                        button=button)  # preparing the messages for ChatGPT

        if functionCalled in ["story", "stop", "distress", "coping"]:
            return functionCalled
