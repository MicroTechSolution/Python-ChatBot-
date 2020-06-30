# This is sampleSort script use to seperate the word and identify the keywords
import responce

testWord = ""
testString =""
currentKey =""
keyWord =""
keyList = ["default"]
getNextWord = True

def sampleSort():
	global testString
	global testWord,getNextWord
	sample= input("user: ")
	for i in range(0,len(sample)):
		if sample[i] == ",":
			continue
		elif sample[i].isspace()== False: 			# if there is no white space then add character to the word
			testWord += sample[i]
			if getNextWord == True:
				testString += sample[i]
			if i == len(sample)-1: 			# if this is the last character of the string
				FindKey(testWord,testString,True)
		else:		

			 # if there is white space then take the word and clear the word
			FindKey(testWord,testString,False) #Sends the word to the function
			testWord = ""
			
	# Resseting All Variables
	testWord = ""
	testString = ""
	getNextWord = True
	sampleSort()
	
		

def FindKey(testWordFK, testStringFK , lastWord):
	global getNextWord
	global keyWord
	global keyList
	global testString

	# Text uppercase and file opening
	testWord = testWordFK.upper()
	testString = testStringFK.upper()
	phasesTxt = open("Phases.txt","r")
	phases = phasesTxt.read()


	theIndex = 0;
	#for i in range(0,len(phases)):
	theIndex = phases.find(testString) # Finding String
	if theIndex == -1: 	# if string is not found
		if keyWord != "":	# if keyWord is not empty
			keyList.append(keyWord)
			keyWord = ""# Storing KeyWord to list

		getNextWord = False			# Telling That Dont add next word in string
		theIndex = phases.find(testWord)	#finding the only Word

		if theIndex == -1:		# if word not found then add word in keyList
			# MAKE THE FUNCTION HERE
			#print(testWord, " Not found")
			testWord += "/UK"
			keyList.append(testWord)
			keyWord = ""



		else :					#if word Found then
			testString = testWord # starting String form the word
			getNextWord = True # 	And telling that add next Word
			# If word found
			# This is to find KeyWord
			while True:
				theIndex -= 1
				if phases[theIndex] == "/":  # moving theWord index number to start of the line
					break

			while True:
				theIndex += 1
				if phases[theIndex] == ";":  # Finding the start of the key
					theIndex += 1
					break

			while phases[theIndex] != ";":
				keyWord += phases[theIndex]
				theIndex += 1
		# Finding KeyWord End
		if lastWord:

			keyList.append(keyWord)
			keyWord = ""
			passingTheWord(keyList)


	else:	# IF string is found

		if getNextWord == True: # if next Word Will add
			 # This is to find KeyWord
			keyWord = ""
			while True:
				theIndex -= 1
				if phases[theIndex] == "/": # moving theWord index number to start of the line
					break
				
			while True:
				theIndex += 1
				if phases[theIndex] == ";": # Finding the start of the key
					theIndex +=1
					break
				
			while phases[theIndex] != ";":
				keyWord += phases[theIndex]
				theIndex +=1
		

			# Finding KeyWord End
		else:

			keyList.append(keyWord)
			keyWord = ""		#Clearing keyWord


		if lastWord:

			keyList.append(keyWord)
			keyWord = ""
			passingTheWord(keyList)

				

def passingTheWord(finalList):
	global keyList, currentKey,keyWord
	responce.analise(finalList)
	currentKey =""
	keyWord =""

	finalList = ["default"]
	keyList = ["default"]
	#for i in range(1, len(keyList)-1):
		#del keyList[i]
		
		

sampleSort() #Calling the main sampleSort Function
		
