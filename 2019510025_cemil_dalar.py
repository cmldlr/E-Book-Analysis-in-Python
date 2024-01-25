import requests  # Adding requests library
from bs4 import BeautifulSoup  # Adding beautifulsoup library
import string #Adding string library
import operator  #Adding operator library
book_name =""

number_of_books=int(input("please enter number of books(1 or 2)"))
frequiences=int(input("how many word frequencies you wish to see?"))
stop_words= {'i', 'me', '•','my','·','like','he', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
             'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
             'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
             'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
             'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
             'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
             'between', 'into', 'through', 'during', 'before', 'after','I', 'above', 'below', 'to', 'from', 'up', 'down',
             'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
             'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
             'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'The','very', 's', 't', 'can', 'will', 'just', 'don',
             "don't", 'should', "should've",'de' 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't",
             'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
             "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan',
             "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn',
             "wouldn't","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x"}
def book_scraping(book_name):
    try:#find the book name
        url = "https://en.wikibooks.org/wiki/"+book_name+"/Print_version"
    except AttributeError as error:
        url = "https://en.wikibooks.org/wiki/"+book_name+"/Print_Version"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    a = soup.find("div", class_="mw-parser-output")
    b=a.find_all(["p","li","h2"])
    c=[]
    for i in b:
       c.append(i.text)
    with open(book_name+".txt","w",encoding="utf-8") as file:#save the book
        file.writelines(c)
def word_frequencies_one_book():
   with open(book_name+".txt","r",encoding="utf-8") as file:#opening the first book
       line=file.read()
       line1=line.lower()
       line2=""
       for i in line1:
           if i not in string.punctuation:
              line2 += i
       splitwords = line2.split(" ")
       all_words = {}
   print("NO  WORD  FREQ_1")
   for word in splitwords:# for word in splitwords:find words and  numbers of words in the book
       if word not in all_words:
           if word not in stop_words:#separating words from stop_words
               all_words[word] = 1
       else:
           if word not in stop_words:
               all_words[word] += 1
   all_words_sorted = sorted(all_words.items(), key=lambda x: x[1], reverse=True)#sorting by the number of words we find
   i=0
   while  i<frequiences:#count the words we find
     print(i+1,str( all_words_sorted[i][0]),str( all_words_sorted[i][1]))
     i=i+1

def word_frequencies_two_book():
    with open(book_name + ".txt", "r", encoding="utf-8") as file:#opening the first book
        line = file.read()
        line1 = line.lower()
        line2 = ""
        for i in line1:
            if i not in string.punctuation:
                line2 += i
        splitwords = line2.split(" ")
        all_words = {}
    print("NO  WORD  FREQ_1")
    for word in splitwords:# for word in splitwords:find words and  numbers of words in the book
        if word not in all_words:
            if word not in stop_words:#separating words from stop_words
                all_words[word] = 1
        else:
            if word not in stop_words:
                all_words[word] += 1
    all_words_sorted = sorted(all_words.items(), key=lambda x: x[1], reverse=True)#sorting by the number of words we find
    i = 0
    while i < frequiences:#count the words we find
        print(i + 1, str(all_words_sorted[i][0]), str(all_words_sorted[i][1]))
        i = i + 1
    with open(book_name2 + ".txt", "r", encoding="utf-8") as file:#opening the second book
        line = file.read()
        line1 = line.lower()
        line2 = ""
        for i in line1:
            if i not in string.punctuation:
                line2 += i
        splitwords = line2.split(" ")
        all_words = {}
    print("NO  WORD  FREQ_2")
    for word in splitwords:# for word in splitwords:find words and  numbers of words in the book
        if word not in all_words:
            if word not in stop_words:#separating words from stop_words
                all_words[word] = 1
        else:
            if word not in stop_words:
                all_words[word] += 1
    all_words_sorted = sorted(all_words.items(), key=lambda x: x[1], reverse=True)#sorting by the number of words we find
    i = 0
    while i < frequiences:#count the words we find
        print(i + 1, str(all_words_sorted[i][0]), str(all_words_sorted[i][1]))
        i = i + 1
def distinct():
    print("DISTINCT WORDS")
    print("NO WORD FREQ_1")
    with open(book_name + ".txt", "r", encoding="utf-8") as file:#opening the first book
        line = file.read()
        line1 = line.lower()
        line2 = ""
        for i in line1:
            if i not in string.punctuation:
                line2 += i
        splitwords = line2.split(" ")
    with open(book_name2 + ".txt", "r", encoding="utf-8") as file:#opening the second book
        line = file.read()
        line1 = line.lower()
        line2 = ""
        for i in line1:
            if i not in string.punctuation:
                line2 += i
        splitwords2 = line2.split(" ")

    distinct_words={}
    for i in splitwords:#find words in the first book that are different from the second book
      if i not in splitwords2:
        if i not in stop_words:
            if i not in distinct_words:
                distinct_words[i]=1
            else:
                distinct_words[i]+=1
    sorting=sorted(distinct_words.items(),key=operator.itemgetter(1),reverse=True)
    j=0
    while j<frequiences:#write words in the first book that are different from the second book
        print(j + 1, str(sorting[j][0]), str(sorting[j][1]))
        j=j+1
    print("DISTINCT WORDS")
    print("NO WORD FREQ_2")
    distinct2_words = {}
    for i in splitwords2:#find words in the second book that are different from the first book
      if i not in splitwords:
        if i not in stop_words:
            if i not in distinct2_words:
                distinct2_words[i] = 1
            else:
                distinct2_words[i] += 1
    sorting2= sorted(distinct2_words.items(), key=operator.itemgetter(1), reverse=True)
    j = 0
    while j < frequiences:#write words in the second book that are different from the first book
        print(j + 1, str(sorting2[j][0]), str(sorting2[j][1]))
        j = j + 1
    common1={}
    common2={}
    for i in splitwords:#find common words found in two books
      if i in splitwords2:
       if i not in stop_words:
            if i not in common1:
                common1[i]=1
            else:
                common1[i]+=1
    sorting3 = sorted(common1.items(), key=operator.itemgetter(1), reverse=True)
    for j in splitwords2:#find common words found in two books
        if j in splitwords:
          if j not in stop_words:
            if j not in common2:
                common2[j] = 1
            else:
                common2[j] += 1
    sorting4 = sorted(common2.items(), key=operator.itemgetter(1), reverse=True)
    p=0
    print("COMMON WORDS")
    print("NO WORD FREQ_1 FREQ_2 FREQ_SUM")
    while  p<frequiences:#write common words found in two books
        print(str(p+1),str(sorting3[p][0]),str(sorting3[p][1]),str(sorting4[p][1]),str(sorting3[p][1]+sorting4[p][1]))
        p=p+1
if number_of_books==1:
    book_name = input("please enter the book name")
    book_name = book_name.replace(" ","_")
    book_name = book_name.replace("'","%27")
    print(book_name)
    book_scraping(book_name)
    word_frequencies_one_book()
elif number_of_books==2:
    book_name = input("please enter the first book name")
    book_name = book_name.replace(" ", "_")
    book_name = book_name.replace("'", "%27")
    book_name2 = input("please enter the second book name")
    book_name2 = book_name2.replace(" ", "_")
    book_name2= book_name2.replace("'", "%27")
    book_scraping(book_name)
    book_scraping(book_name2)
    word_frequencies_two_book()
    distinct()
elif number_of_books>2:
  print("Error!!.Only You can enter maximum two books.Please enter the number of books correctly.")




