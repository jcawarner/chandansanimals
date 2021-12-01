from bs4 import	BeautifulSoup
import requests
import random

r = requests.get("https://a-z-animals.com/animals/aardvark/")
response = r.content

soup = BeautifulSoup(response, 'html.parser')

#name of animal
# print(soup.find('h1').text)

#fact
# print(soup.find(class_="mb-0").text)

#img link

#locations
# print(soup.select('div.col-lg-6 ul.list-unstyled')[1].text)

#fact list
# print(soup.select('dt'))
# classification = soup.select('dt')
# # for dt in soup.select('dt'):
# # 	print(dt.text)
#
# #fact list
# # print(soup.select('div dd'))
# facts = soup.select('div dd')
#
# for des in range(len(classification)):
# 	print(classification[des - 1].text, facts[des - 1].text)
#
# class_list = [class_item.text for class_item in classification]
# fact_list = [fact_item.text for fact_item in facts]
#
# print(class_list)
# print(fact_list)
#
# for iter in range(len(class_list)):
# 	if class_list[iter] == 'Prey':
# 		print(fact_list[iter])

# animal_images = soup.select('img.center-block')
# img_link = [pic['data-lazy'] for pic in animal_images]
# animal_image = img_link[random.randint(0,4)]
# print(animal_image)

location_img = soup.select('img.animal-location-map')
for img in location_img:
	print(img['src'])