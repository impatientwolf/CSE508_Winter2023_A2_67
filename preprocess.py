import fileinput
import re
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk import word_tokenize,sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')


def preprocess(content):
    content= content.lower()
    content = content.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(content)

    for i in range(len(tokens)):

        #remove punctuation
        tokens[i] = re.sub(r'[^\w\s]', '', tokens[i])

        #remove white space
        tokens[i] = " ".join(tokens[i].split())

  #removing empty tokens
    tokens = [w for w in tokens if w != ""]


    stop_words = set(stopwords.words('english'))
    without_stop_word=[]
    for w in tokens:
        if w not in stop_words:
            without_stop_word.append(w)
    
    final_tokens=without_stop_word
    final_text=final_tokens[0]+" "

    for item in range(1,final_tokens):
        final_text=final_text+item[item]+" "
    
    return final_tokens, final_text


def edit_file(file_path):

    for file_no in range(1,1400+1):
        path = r'C:\Users\Priyanshu\Downloads\IR Ass2\CSE508_Winter2023_Dataset'
        if(file_no<10):
            file_no="000"+str(file_no)
            path = path + "\\"+"cranfield"+str(file_no)
        elif(file_no<100):
            file_no="00"+str(file_no)
            path = path + "\\"+"cranfield"+str(file_no)
        elif(file_no<1000):
            file_no="0"+str(file_no)
            path = path + "\\"+"cranfield"+str(file_no)
        else:
            path = path + "\\"+"cranfield"+str(file_no)

        f=open(path,"r")
        content= str(f.read())
        f.close()

        # print("intital content",content)

        # print("final_content",final_tokens)
        
        final_tokens, final_text=preprocess(content)
        f=open(path,"w")
        for item in final_tokens:
            f.write(item + " ")
        f.close()
        


path= r"C:\Users\Priyanshu\Downloads\IR Ass2\CSE508_Winter2023_Dataset"
edit_file(path)





