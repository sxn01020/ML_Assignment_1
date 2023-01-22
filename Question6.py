sentence="I am a teacher and I love to inspire and teach people" #input sentence

#Calculating the unique words from the sentence
words=sentence.split() #splitting the sentence into a list of words
print("List of words after splitting the sentence is: ",words)
print("Number of unique words from the given sentence is: ",len(set(words)))