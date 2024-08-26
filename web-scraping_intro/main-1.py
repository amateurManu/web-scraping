from bs4 import BeautifulSoup

""" Open file and read contents of file """
with open('100-index.html', 'r') as html_file:
    content = html_file.read()
    
    """ Creating an instance of BeautifulSoup """
    soup = BeautifulSoup(content, 'lxml')

    availabilities = soup.find_all('article')
    for available in availabilities:
        places = available.h2.text
        amount = available.div.text.replace(' ','')
        print(f"{places} costs {amount.strip()}")
