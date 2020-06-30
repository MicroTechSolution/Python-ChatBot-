import random

namePrefix = "liza: "
responscesSamples = open("responcesSamples.txt","r")
resp = responscesSamples.read()

phasesTxt = open("Phases.txt","r")
phases = phasesTxt.read()

finalListString = ";"
ukWord =""
finalResponce = ""
opWord = ""

def analise(theList):
    global finalListString
    global finalResponce
    StartCounts = [0]

    for i in range(1,len(theList)):     # Gathering All Keys in one string to find
        finalListString += theList[i]
        finalListString += ";"


    clearUnknown()
    theIndex = 0
    theIndex = resp.find(finalListString)   #SOLVE this
    if(theIndex == -1): # if keys are not found
        finalResponce ="Sorry I dont know what you are saying"

    else:   # if keys are found
        while resp[theIndex] != "<":
            if resp[theIndex] == "%":
                StartCounts.append(theIndex)
            theIndex += 1

        temp = random.randint(1,len(StartCounts)-1)
        theIndex = StartCounts[temp] +1
        #theIndex += 1
        while resp[theIndex] != "*":
            finalResponce += resp[theIndex]
            theIndex += 1


    checkNchange(theIndex)
    print(namePrefix, finalResponce)
    finalResponce =""
    finalListString =";"

def clearUnknown():
    global finalListString,ukWord
    tempWord = ""
    while finalListString.find("/UK") != -1:
        ukIndex = finalListString.find("/UK")
        while finalListString[ukIndex] != ";":
            ukIndex -=1

        ukIndex +=1
        while finalListString[ukIndex] != "/":
            ukWord += finalListString[ukIndex]
            tempWord += finalListString[ukIndex]
            ukIndex +=1

        temp = tempWord+"/UK"
        finalListString =finalListString.replace(temp,"UNKNOWN")
        tempWord = ""
        ukWord += ""
        #print(finalListString)

def checkNchange(theIndexCN):
    global resp,opWord,finalResponce,ukWord

    while resp[theIndexCN] != "<":
        if resp[theIndexCN] == "^":
            break
        theIndexCN += 1
    else:
        return

    theIndexCN += 1
    while resp[theIndexCN] != "*":
        opWord += resp[theIndexCN]
        theIndexCN += 1

    #print("Here ",opWord)

    if opWord == "CHANGEUSER":
        finalResponce = finalResponce.replace("USER",ukWord)

    elif opWord == "ASKAPPOINTMENT":
        print(finalResponce)
        finalResponce =""
        setAppointment()
        print("Entered here")
    elif opWord == "GETPERSONINFO":
        theInfo =""
        print(finalResponce)
        personTxt = open("persons.txt","r")
        persons = personTxt.read()
        tempIndex = persons.find(ukWord)
        if tempIndex == -1:
            tempi = askPerson()
            if tempi ==5:    
                finalResponce = "Thanks for sharing information with me"
            elif tempi == 8:
            	finalResponce = "feels bad because i hear bad word from you"
            
        else:
            while persons[tempIndex] != ";":
                tempIndex +=1

            tempIndex +=1
            theInfo = ""
            while persons[tempIndex] != ";":
                theInfo += persons[tempIndex]
                tempIndex +=1

            theInfo = badFilter(theInfo)
            finalResponce = theInfo



    ukWord = ""
    opWord = ""

def badFilter(theInfo):
    badWords = ["fuck", "fucker", "bhosdicha", "madarchod","yz","chutiya","gandu","mc","bc","ag","ass", "bhosda", "dlp","DLP"]
    gotWord = False
    for i in range(0,len(badWords)):
        temp = theInfo.find(badWords[i])
        if temp == -1:
            continue
        else:
            gotWord = True

    if gotWord == True:
        return "feels bad because you are expecting bad word from me"
    else:
        return theInfo

def getResp(theIndex):
    global resp
    StartCount = [0]
    theResponce = ""
    while resp[theIndex] != "<":
        if resp[theIndex] == "%":
            StartCount.append(theIndex)
        theIndex +=1
        
    temp = StartCount[random.randint(1,len(StartCount)-1)]
    temp += 1

    while resp[temp] != "*":
        theResponce += resp[temp]
        temp +=1
    return theResponce



def getTempKey(theWord):
    global phases
    gotWord = ""
    theIndex = phases.find(theWord)
    if theIndex != -1:
        while phases[theIndex] != "/":
            theIndex -= 1

        while phases[theIndex] != ";":
            theIndex += 1

        theIndex +=1
        while phases[theIndex] != ";":
            gotWord += phases[theIndex]

        return theWord
    else:
        return "NULL"



def askPerson():
	global resp
	persReadTxt = open("persons.txt","r")
	persRead = persReadTxt.read()
	persTxt = open("persons.txt","w")
	tempIndex = resp.find("GETPERSON")
	ans =getResp(tempIndex)
	
	print(ans)
	x = input("user: ")

	y = badFilter(x)
	if x ==y:
		x = persRead +"  /> *"+ukWord+"* ;"+x+"; "
		persTxt.write(x)
		return 5
	else:
		persTxt.write(persRead)
		return 8
			
	#WRITE HERE FOR SAVING CODE IN FILE
	
	

def setAppointment():
    theAns = input("user: ")
    print("Let me check ...")



