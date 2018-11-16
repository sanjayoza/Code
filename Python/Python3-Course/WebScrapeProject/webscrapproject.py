import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import reader, writer, DictReader, DictWriter
import os


BASE_URL = "http://quotes.toscrape.com"
FILE_NAME = "quotes.csv"
### Check if file exists with quotes, 
### if exists then read the file and return quotes 
### otherwise return empty list
def get_quotes_from_file():
    if not os.path.isfile(FILE_NAME):
        print("file does not exist")
        return None
    print("reading the file " + FILE_NAME)
    with open(FILE_NAME) as file:
        csv_reader = DictReader(file)
        quotes = list(csv_reader)
        return quotes   

### write the quotes to a csv file
def write_quotes_file(quotes):
    with open(FILE_NAME, "w") as file:
        headers = ("quote", "author", "href")
        csv_writer = DictWriter(file, fieldnames=headers)  # get iterator
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)
        
### get the quotes from web site if they do not exist in file
def get_quotes():
    url = "/page/1"
    
    # check if file does not exist then get data from web
    all_quotes = get_quotes_from_file()
    if all_quotes:
        return all_quotes
    all_quotes = []
    while url:
        # get and process data from one page
        get_url = BASE_URL + url
        print("Scraping ... " + get_url)
        res = requests.get(get_url)
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:   
            all_quotes.append(
                {
                    "quote": quote.find(class_="text").get_text(), 
                    "author": quote.find(class_="author").get_text(),
                    "href" : quote.find("a")['href']
                })
        # look for the next button the page (it is a class). If there is no next then
        # the page has no next button
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")['href'] if next_btn else None
        sleep(2)    # sleep for 2 seconds
    write_quotes_file(all_quotes)
    return all_quotes

def play_game():
    quotes = get_quotes()
    quote = choice(quotes)
    print("Here' a quote: ")
    print(quote["quote"])
    author = quote["author"]
    remaining_guesses = 4
    print(author)
    guess = ''
    names = author.split(" ")
    while guess.lower() != author.lower() and remaining_guesses > 0:
        str1 = "Who said this quote? Guesses remaining {}" .format(remaining_guesses)
        guess = input(str1 + "\n> ")
        if guess.lower() == author.lower():
            print("You WIN !! Guessed correctly")
            break
        
        remaining_guesses -= 1
        if remaining_guesses == 3:
            url = BASE_URL + quote["href"]
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            bdate = soup.find(class_="author-born-date").get_text()
            bloc = soup.find(class_="author-born-location").get_text()
            print("Hint ! Author was born on {} {}" .format(bdate, bloc))
        elif remaining_guesses == 2:
            print("Hint ! Author's first name starts with: {}"
                  .format(names[0][0]))
        elif remaining_guesses == 1:
            print("Hint ! Author's last name starts with: {}"
                  .format(names[1][0]))
        else:
            print("Sorry you ran out of guesses, author is {}" .format(author))
    
    again = ""
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n) > ")
        if again.lower() in ('y', 'yes'):
            play_game()
        else:
            print("Goodbye !")
            break
    

if __name__ == "__main__":    
    play_game()
