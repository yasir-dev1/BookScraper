from bs4 import BeautifulSoup 
import requests,os


author = input("Author:").replace(" ","-")

print(author)
basepath =os.mkdir(author.replace("-","_"))

def download_book (urls,filename):
    bookpage = requests.get(urls)
    soup = BeautifulSoup(bookpage.content)
    bookurl = soup.find("a",attrs={"class","btn v-btn v-btn-default btn-group btn-group-justified special-icon"}).get("href")
    book = requests.get(bookurl)
    with open(author.replace("-","_")+"/"+filename+".pdf","wb") as file:
        file.write(book.content)

page = 1

while page > 0:


    url = f"https://foulabook.com/ar/author/{author}?page={page}"

    print(url)

    req = requests.get(url)
    

    soup = BeautifulSoup(req.content,features="lxml")

    books = soup.find_all("figure",attrs={"class":"animated-overlay overlay-alt"})
    
    if books != []:
        print(books)
        for book in books:
            book_url = book.find("a").get("href")
            print(book_url)
            title = book.find("img").get("alt")
            download_book(book_url,title)
        
        page+=1
    else:
        print(books)
        page=-1