from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)