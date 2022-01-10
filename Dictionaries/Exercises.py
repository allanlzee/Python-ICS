def exercise_1():
    dictionary = {"Allan": "Zhou",
                  "Eric": "Mak",
                  "Liam": "Ung",
                  "Colby": "Chansamone-Lam",
                  "Griffin": "Gray"}

    print("Keys: ")
    for key in dictionary:
        print(key)

    print("\nValues: ")
    for values in dictionary.values():
        print(values)


def exercise_2():
    dictionary = {}

    while True:
        key = input("Enter a key: ")

        if key == "":
            break

        value = input("Enter a value: ")

        dictionary[key] = value

    print(dictionary)


def exercise_3():
    translation = {'cat': 'chat', 'cheese': 'fromage', 'parrot': 'perroquet'}

    while True: 
        word = input("What word would you like to translate: ")

        if word == "": 
            print(translation)
            break

        if word in translation: 
            print("The translated word is: {}.".format(translation[word]))
        else: 
            translate = input("Please enter the translation of the word {}: ".format(word))
            translation[word] = translate
        

def exercise_4(): 
    
    string = "massasauga rattlesnake" 

    occur = {} 

    for char in string: 
        if char not in occur: 
            occur.setdefault(char, 0) 
        
        occur[char] += 1
    
    print(occur)


def exercise_5(): 
    print("I want to revert this commit.")


def main():
    exercise_4()


if __name__ == "__main__":
    main()
