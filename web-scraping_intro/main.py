from bs4 import BeautifulSoup

""" Open file and read contents of file """
with open('100-index.html', 'r') as html_file:
    content = html_file.read()
    
    """ Creating an instance of BeautifulSoup """
    soup = BeautifulSoup(content, 'lxml')

    """ Locating all h3 elements """
    tags = soup.find_all('h3')
    for tag in tags:
        print(tag.text)
