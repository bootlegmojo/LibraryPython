


 
# Classes defining all of the data i look to be working with
class Library():
    def __init__ (self, booklist, newslist, maglist):
        self.booklist = booklist
        self.newslist = newslist
        self.maglist = maglist
    

    
class Book():
    def __init__ (self, id, name, author, genre, pubdate):
        self.id = id
        self.name = name
        self.author = author
        self.genre = genre
        self.pubdate = pubdate
    def printbook(self):
        
        print ("%s, %s, %s, %s, %s" % (self.id, self.name, self.author, self.genre, self.pubdate))

    #shows exel data
    def checkexel(self):
        with open('Library/booklist.csv', 'r', newline = "\n") as filehandle:
            reader=csv.reader(filehandle, delimiter='\t', quotechar='|',)
            for row in reader:
                print (", ".join(row))
class News():
    def __init__ (self, id, name, editor, publisher, pubdate):
        self.id = id
        self.name = name
        self.editor = editor
        self.publisher = publisher
        self.pubdate = pubdate

    def printnews(self):
        
        print ("%s, %s, %s, %s, %s" % (self.id, self.name, self.editor, self.publisher, self.pubdate))

class Mag():
    def __init__ (self, id, name, editor, genre, pubdate):
        self.id = id
        self.name = name
        self.editor = editor
        self.genre = genre
        self.pubdate = pubdate

    def printmag(self):
        
        print ("%s, %s, %s, %s, %s" % (self.id, self.name, self.editor, self.genre, self.pubdate))


# check if this is the right approach
class CheckedOut():
    def __init__ (self, name, person, outdate, returndate):
        self.name
        self.person
        self.outdate
        self.returndate

class Person():
    def __init__ (self, name, userid, adress, email, phonenum, dob):
        self.name = name
        self.userid = userid
        self.adress = adress
        self.email = email
        self.phonenum = phonenum
        self.dob = dob

#start adding books
Library.booklist = []
Library.newslist = []
Library.maglist = []

Library.booklist.append(Book("B1", "Bible", "God", "Religeous", 0000))
Library.booklist.append(Book("B2", "Girl in the Ice","Robert Bryndza", "Thriller", 2016))
Library.booklist.append(Book("B3", "Tatooist of Auschwitz", "Heather Morris", "Novel", 2018))
Library.booklist.append(Book("B4", "Honeymoon", "Rona Halsall", "Thriller", 2019))
Library.booklist.append(Book("B5", "Shadows of What Was Lost", "James Islington", "Fantasy", 2017))
Library.booklist.append(Book("B6", "Spellslinger 3", "Sebastian de Castell", "Fantasy", 2018))
Library.booklist.append(Book("B7", "Beneath a Scarlet Sky", "Mark Sullivan", "Novel", 2017))
Library.booklist.append(Book("B8", "Friend Request", "Laura Marshall", "Thriller", 2017))
Library.booklist.append(Book("B9", "Good Omens", "Terry Pratchett", "Parody", 2019))
Library.booklist.append(Book("B10", "Spellslinger", "Sebastian de Castell", "Fantasy", 2017))
Library.booklist.append(Book("B11", "Mary Berry's Quick Cooking", "Mary Berry", "Cooking", 2019))


Library.newslist.append(News("N1", "The Sun", "Tony Gallagher", "News Group Newspapers", "July"))
Library.newslist.append(News("N2", "Daily Mail", "Geordie Greig", "DMG Media", "June"))
Library.newslist.append(News("N3", "The Times", "John Witherow", "HarperCollins", "January"))
Library.newslist.append(News("N4", "The Guardian", "Guard Armstrong", "Guildian", "February"))
Library.newslist.append(News("N5", "Daily Express", "Expessor Smith", "Expression Session", "March"))
Library.newslist.append(News("N6", "Daily Mirror", "Michael Jackson", "Man in the Mirror", "April"))
Library.newslist.append(News("N7", "Daily Bugle", "Peter Parker", "Jonah Jameson", "June"))

Library.maglist.append(Mag("M1", "Time", "Edward Felsenthal", "News", 1923))
Library.maglist.append(Mag("M2", "Vogue", "Anna Wintour", "Fashion", 1892))
Library.maglist.append(Mag("M3", "GQ", "Condé Nast", "Mens interests", 1957))
Library.maglist.append(Mag("M4", "WIRED", "Nicholas Thompson", "Technology", 1993))
Library.maglist.append(Mag("M5", "PC Gamer", "Phil Savage", "PC gaming", 1993))
Library.maglist.append(Mag("M6", "Good Housekeeping", "Gaby Huddart ", "Womens interests", 1885))
Library.maglist.append(Mag("M7", "O, The Oprah Magazine", "Lucy Kaylin", "Womens interests", 2000))


for book in Library.booklist:
    book.printbook()

for News in Library.newslist:
    News.printnews()

for mag in Library.maglist:
    mag.printmag()
        
    

import csv

# Writes all lists to a .csv file
def writecsv():
    with open('Library/booklist.csv', 'w', newline = "\n") as filehandle: 
        writer=csv.writer(filehandle, delimiter='\t',lineterminator='\n',) 
        for book in Library.booklist:
            row = [("%s, %s, %s, %s, %s" % (book.id, book.name, book.author, book.genre, book.pubdate))]
            writer.writerow(row)

    with open('Library/newslist.csv', 'w', newline = "\n") as filehandle: 
        writer=csv.writer(filehandle, delimiter='\t',lineterminator='\n',) 
        for news in Library.newslist:
            row = [("%s, %s, %s, %s, %s" % (news.id, news.name, news.editor, news.publisher, news.pubdate))]
            writer.writerow(row)

    with open('Library/maglist.csv', 'w', newline = "\n") as filehandle: 
        writer=csv.writer(filehandle, delimiter='\t',lineterminator='\n',) 
        for mag in Library.maglist:
            row = [("%s, %s, %s, %s, %s" % (mag.id, mag.name, mag.editor, mag.genre, mag.pubdate))]
            writer.writerow(row)
       # filehandle.writelines("%s,  %s, %s, %s, %s\n" % (book.id, book.name, book.author, book.genre, book.pubdate))




# book.checkexel()

#Request each individualy 


    

