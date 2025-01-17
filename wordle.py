# Import
import pandas as bpd
import numpy as np
import os

# Read all the words

english_data_path = os.path.join('Data', 'relevantWords.csv')

relevant_words = bpd.read_csv(english_data_path)


# Declaring Red, Yellow, and Green boxes
l0 = np.array([])
l1 = np.array([])
l2 = np.array([])
m2 = np.array([])


#The first word
unique_words = np.array(['FRAUD','FAIRY','GREAT','HEAPS',
                         'EARTH', 'VOWEL', 'DREAM', 'DOING', 'POINT'])
global player_word
player_word = np.random.choice(unique_words,1)[0]
print('#1 word: '+ player_word)
win = 6
counter = 0
while counter<win:
    not_more = True
    #Taking player input
    player_input = input('Colors: ')
    player_input = player_input.upper()

    #Segregating player_word in Red, Yellow, Green boxes
    for i in range(0,5):
        subject = player_input[i]
        if (subject=='R'):
            l0 = np.append(l0,player_word[i])
        elif (subject=='G'): #l1 contains the index number of the Green letters
            l1 = np.append(l1,i)
        elif (subject=='Y'):
            l2 = np.append(l2,player_word[i])
            m2 = np.append(m2,i)
        elif (subject=='W'):
            print('I am Smart!')
            exit()
        else:
            relevant_words = relevant_words[relevant_words.get('words').str.contains(player_word) == False]
            player_word = np.random.choice(relevant_words.get('words'))
            print(player_word)
            not_more = False
            win = win+1
            break

    if (not_more):
        l2 = np.unique(l2)
        set1 = set(l0)
        set2 = set(l2)
        set3 = set([player_word[int(i)] for i in l1])

        common_elements = set1.intersection(set2)
        ce2 = set1.intersection(set3)
        l0 = [element for element in l0 if element not in common_elements]
        l0 = [element for element in l0 if element not in ce2]
        # Weeding Red letters words from relevant_words
        for i in l0:
            relevant_words = relevant_words[relevant_words.get('words').str.contains(i)==False]
        # Screening Yellow words letters from relevant_words
        for i in l2:
            relevant_words = relevant_words[relevant_words.get('words').str.contains(i)]

        # Green letter word process
        def screener(word):
            damner = word
            for i in l1:
                i = int(i)
                if word[i]!=player_word[i]:
                    damner = 'x'
            for i in m2:
                i = int(i)
                if word[i]==player_word[i]:
                    damner = 'x'
            return damner
        relevant_words = relevant_words.assign(words = relevant_words.get('words').apply(screener))
        relevant_words = relevant_words[relevant_words.get('words')!='x']

        # Output random word from resultant relevant_words
        player_word = np.random.choice(relevant_words.get('words'))
        print(player_word)
        print(f'{int(1/len(relevant_words)*100)}% of winning')
    # Emptying l1
        l1 = np.array([])
        m2 = np.array([])
    counter = counter + 1
