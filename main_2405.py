# name: huynh hoang nam
# class: gcs 1002

# exercise 1:
#function to print out message
def introductionInput(name, age: int, entranceYear: int, currentYear: int) -> str:
    year = currentYear - entranceYear
    # change the message base on the studied year (1st,2nd,3rd,...th)
    if(year == 1):
        print(f"hello my name is {name} i am {age} years old, i am a {year}'st student at greenwich.")
    elif(year == 2):
        print(f"hello my name is {name} i am {age} years old, i am a {year}'nd student at greenwich.")
    elif(year == 3):
        print(f"hello my name is {name} i am {age} years old, i am a {year}'rd student at greenwich.")
    else:
        print(f"hello my name is {name} i am {age} years old, i am a {year}'th student at greenwich.")
# loop to make sure input info is correct
while True:
    try:
        # name
        nameInput = input("enter your name: ")
        # age
        ageInput = int(input("enter your age: "))
        # entrance year
        entranceYearInput = int(input("enter your entrance year: "))
        # current year
        currentYearInput = int(input("enter your current year: "))
        break
    except ValueError:
        # request reinput
        print("invalid input try again")

introductionInput(nameInput,ageInput,entranceYearInput,currentYearInput)

# exercise 2:
stringInput = input("enter your string: ")
while True:
    try:
        intInput = int(input("enter the location to the word you want to replace: "))
        break
    except ValueError:
        print("invalid input try again")
newStringInput = input("enter replacement words: ")
#counting initial char length
initialCharCount = len(stringInput)
#split string into individual words
stringWords = stringInput.split()
#count initial words numbers
initalStringWordsLength = len(stringWords)
#split added string into individual words
newStringWords = newStringInput.split()
#delete the word at the specified location and replace deleted word with new words
stringWords[intInput - 1 : intInput] = newStringWords
#count new word num
newStringWordsLength = len(stringWords)
#get result
result = ' '.join(stringWords)
#count new char lenth
newCharCount = len(result)
# print result
print("\n\n")
print("result:" + result)
print("initial word count: ", initalStringWordsLength)
print("initial character count: ", initialCharCount)
print("new word count: ", newStringWordsLength)
print("new character count: ", newCharCount)
print("replace word's location: ", intInput)