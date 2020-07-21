#!/usr/bin/env python
# coding: utf-8

# In[36]:


#reading a text file
file_raw = open("1342.txt","r", encoding="utf8") 
# print(file_raw.read())


# In[ ]:


#edited text file without author's notes in the start and end
import string
file_edited = open("1342_edited.txt","r", encoding="utf8") 
#remove \n from the whole text
file_edited_read = file_edited.read().replace('\n', ' ')
# print(file_edited_read)

#remove punctuation 
# # initializing punctuations string   
punctuations = '''!()-[]{};:'"”“\,<>./?@#$%^&*_~''' 
for x in file_edited_read: 
    if x in punctuations: 
        file_edited_read = file_edited_read.lower().replace(x, "")  
print(file_edited_read)


# In[17]:


#splitting text (novel) to chapters for further use
list_chapters = file_edited_read.split('chapter ')[1:]
# print(list_chapters[59], list_chapters[58])
for i in range(0, len(list_chapters)):
    a =  list_chapters[i].lstrip('0123456789.- ')
    #remove \n or new line
    list_chapters[i] = a.replace('\n','')
    punctuations = '''!()-[]{};:'"”“\,<>./?@#$%^&*_~''' 
    punctuations_dotted = '''!()-[]{};:'"”“\,<>/?@#$%^&*_~'''
for i in range(0, len(list_chapters)):
    for x in list_chapters[i]: 
        if x in punctuations: 
            list_chapters[i] = list_chapters[i].lower().replace(x, "")   
    
print(list_chapters)


# In[45]:


#creating text file for 1000 words and reading into list
def common_words_breakpoint(count):
    with open("common_words_1000.txt") as file_in:
        common_words = []
        for line in file_in:
            count = count - 1
            if count == -1:
                break
            common_words.append(line.replace('\n',''))
    return common_words
# common_words_breakpoint(200)


# In[38]:


#Method1: number of words in the whole text using COUNTER
import collections 
def getTotalNumberOfWords(string):
    count = 0
    dictionary = collections.Counter(string.split())
    for key, value in dictionary.items():
        if value>=1:
            count += value
    print(count)
getTotalNumberOfWords(file_edited_read)


# In[40]:


#Method2: number of unique words in the whole text using COUNTER:
import collections
def getTotalUniqueWords(string):
    word_list = []
    dictionary = collections.Counter(string.split())
    for key, value in dictionary.items():
        if value>=1:
            word_list.append(key)
    print(len(word_list))
getTotalUniqueWords(file_edited_read)   


# In[42]:


#Method3: 20 most frequent words in the whole text using COUNTER:
import collections
def getMostFrequentWords(string):
    word_list = []
    dictionary = collections.Counter(string.split())
    sorted_counter = dictionary.most_common(20)
    print(sorted_counter)
getMostFrequentWords(file_edited_read)


# In[52]:


#Methode4:
import collections
def get20MostInterestingFrequentWords(string, tune_point):

    word_list = []
    dictionary = collections.Counter(string.split())
    sorted_counter = dictionary.most_common()
    #breaing point as 100
    common_list = common_words_breakpoint(tune_point)
    for (key, val) in sorted_counter:
#         print(common_list)
        if key not in common_list:
            word_list.append((key, val))
            if len(word_list) == 20:
                break
    print(word_list)
            
get20MostInterestingFrequentWords(file_edited_read, 100)
get20MostInterestingFrequentWords(file_edited_read, 200)
get20MostInterestingFrequentWords(file_edited_read, 300)


# In[54]:


#Method3: 20 most frequent words in the whole text using COUNTER:
import collections
def get20LeastFrequentWords(string):
    word_list = []
    dictionary = collections.Counter(string.split())
    sorted_counter = dictionary.most_common()[:-20-1:-1]
    print(sorted_counter)
get20LeastFrequentWords(file_edited_read)


# In[56]:


#STEP3: get frequncy of words for each chapter in a list
import collections
def getFrequencyOfWord(word):
    result = []
    for i in list_chapters:
        temp = 0
        dictionary = collections.Counter(i.split())
        for key, value in dictionary.items():
            if key == word:
                temp = value
        result.append(temp)       
    return result       
print(getFrequencyOfWord('this'))
        
    


# In[57]:


import difflib
def getChapterQuoteAppears(string):
    for x in string: 
        if x in punctuations: 
            string = string.lower().replace(x, "")
#     print(string)
    for i in range(0, len(list_chapters)):
        if string in list_chapters[i]:
            return i+1
    return -1 

string = "Mr. Darcy bowed"
print(getChapterQuoteAppears(string))
    


# In[58]:


#edited text file without author's notes in the start and end
# import string
# file_edited_sent = open("1342_edited.txt","r", encoding="utf8") 
# #remove \n from the whole text
# file_edited_read_sent = file_edited_sent.read().replace('\n', ' ')
# # print(file_edited_read)

# #remove punctuation 
# # # initializing punctuations string without deleting full stop (tokenize sentences . is required)   
# punctuations_dotted = '''!()-[]{};:'"”“\,<>./?@#$%^&*_~''' 
# for x in file_edited_read_sent: 
#     if x in punctuations_dotted: 
#         file_edited_read_sent = file_edited_read_sent.lower().replace(x, "")  
# print(file_edited_read_sent)
    


# In[ ]:


# #NLTK TO TOKENISE THE TEXT TO SENTENCES
# from nltk import tokenize
# print(tokenize.sent_tokenize(file_edited_read_sent))


# In[60]:


import random
def generateSentence(word):
    sent_list = []
    n = 19
    for i in range(0, 21):
        sent_list.append(word)
        list = adjacentwordlist(word)
        word = random.choice(list)
    return " ".join(sent_list)

def adjacentwordlist(word):
    adj_list = []
    words = file_edited_read.split()
    for i, w in enumerate(words):
        if w == word:
            adj_list.append(words[i+1])
    return adj_list

print(generateSentence('the'))


# In[22]:


import regex
import difflib
def closestMatch(word):
    for i in range(0, len(list_chapters)):
        return regex.match('(list_chapters[i]){e<=1}', word)
        
print(closestMatch("Mr. Darcy bowed"))


# In[33]:


from fuzzywuzzy import fuzz
max = 0
for i in range(0, len(list_chapters)):
    a = fuzz.partial_ratio("Mr. Darcy bowed", list_chapters[i])
    if a > max:
        max = a
        index = i+1
print(index)
    


# In[ ]:




