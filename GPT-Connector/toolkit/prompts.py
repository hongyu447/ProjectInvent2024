promptList =[0]

latestVersion =2
print("Enter which version you'd like to use (1,2,3,4..)")
version = int(input(""))
while version not in list(range(latestVersion+1)):
    print("Enter an integer value between 1 and ",latestVersion)



distressPrompt="notify caregivers that user is distressed only if the user explicity mentions distress"
copingPrompt="the user would like to practice coping skills such as meditation or breathing excerises"
V1={"distressPrompt":distressPrompt,"copingPrompt":copingPrompt}
promptList.append(V1)


distressPrompt="the user explicity, clearly, and directly states that they are in a severe state of distress and needs urgent consoling."
copingPrompt="the user would like to practice coping skills such as meditation or breathing excerises"
V2={"distressPrompt":distressPrompt,"copingPrompt":copingPrompt}
promptList.append(V2)


distressPrompt=""
copingPrompt=""
V3={"distressPrompt":distressPrompt,"copingPrompt":copingPrompt}
promptList.append(V3)


distressPrompt=""
copingPrompt=""
V4={"distressPrompt":distressPrompt,"copingPrompt":copingPrompt}
promptList.append(V4)


distressPrompt=""
copingPrompt=""
V5={"distressPrompt":distressPrompt,"copingPrompt":copingPrompt}
promptList.append(V5)
