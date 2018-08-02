# Import Dependencies
import os
from pathlib import Path
import re
# Make a reference to the paragraph_1.txt file path
filepath = Path("../../"Desktop")
filename = "paragraph_1.txt"
path_to_file = os.path.join(filepath, filename)
# Opening the paragraph_1.txt file to print
f = open(path_to_file , 'r')
message = f.read()
#print(message)

# Method 1 to calculate Approximate word count
wordcount= 0
for word in message.split():
        wordcount += 1
#print (wordcount)

# Method 2 to calculate Approximate word count
words = message.split()
words_count = len(words)

# Calculation for Approximate letter count (per word)
average = sum(len(word) for word in words) / len(words)
#print(average)
letter_count = average

# Method 1 to calculate Approximate sentence count which is giving incorrect result
sentencecount= 0
for sentence in message.split('.'):
        sentencecount += 1
#print (sentencecount)
#message.split('.')

# Method 2 to calculate Approximate sentence count
# Counting the number of sentences
sentences = re.split("(?<=[.!?]) +", message)
sentence_count = len(sentences)

# counting Average sentence length in words
#re.split("(?<=[.!?]) +", message)
wordcounts = []
sentences = re.split("(?<=[.!?]) +", message)
for sentence in sentences:
        words = sentence.split(' ')
        wordcounts.append(len(words))       
average_sentence_length = sum(wordcounts)/len(wordcounts)
#print (average_sentence_length )
#print(wordcounts)

print("Paragraph Analysis" + "\n --------------------")
print(" Approximate word count : " + str(words_count))
print("Approximate Sentence Count : " + str(sentence_count))
print("Approximate Letter Count : " + str(letter_count))
print("Approximate Sentence Length : " + str(average_sentence_length ))

text_file = open("Output_PyParagraph.txt", "w")

text_file.write("Paragraph Analysis" + "\n --------------------")
text_file.write(" Approximate word count : " + str(words_count))
text_file.write("Approximate Sentence Count : " + str(sentence_count))
text_file.write("Approximate Letter Count : " + str(letter_count))
text_file.write("Approximate Sentence Length : " + str(average_sentence_length ))
text_file.close()
