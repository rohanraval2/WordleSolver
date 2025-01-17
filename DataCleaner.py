import pandas as pd
import os

dictionary_path = os.path.join('Data', 'english Dictionary.csv')

words = pd.read_csv(dictionary_path)

# Only keeping 5 letter words with alphabets and UpperCasing all the words
relevant_words = words.groupby('word').sum().reset_index()
relevant_words = relevant_words[relevant_words.get('word').str.len()==5].get(['word'])
relevant_words = relevant_words.assign(words = relevant_words.get('word').str.upper())

relevant_words = relevant_words.assign(words = relevant_words.get('word').str.upper())
relevant_words = relevant_words[~relevant_words['word'].str.contains('-')]

new_data_path = os.path.join('Data', 'relevantWords.csv')
relevant_words.to_csv(new_data_path)