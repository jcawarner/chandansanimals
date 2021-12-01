from bs4 import BeautifulSoup
import requests

main_page = requests.get("https://a-z-animals.com/animals/animals-that-start-with-a/")
main_response = main_page.content

main_soup = BeautifulSoup(main_response, 'html.parser')

animals = main_soup.select('h3 a')
animal_links = [animal['href'] for animal in animals]

animal_list = []
for link in animal_links:
	r = requests.get(link)
	response = r.content
	soup = BeautifulSoup(response, 'html.parser')
	animal_list.append(soup.find('h1').text)




