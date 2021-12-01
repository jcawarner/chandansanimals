import random

from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#scrap website for data
# from bs4 import BeautifulSoup
# import requests
#
# main_page = requests.get("https://a-z-animals.com/animals/animals-that-start-with-z/")
# main_response = main_page.content
#
# main_soup = BeautifulSoup(main_response, 'html.parser')
#
# animals = main_soup.select('h3 a')
# animal_links = [animal['href'] for animal in animals]

# 1265 animals in my database

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    fact = db.Column(db.String(1000), unique=False, nullable=False)
    location = db.Column(db.String(500), unique=False, nullable=False)
    prey = db.Column(db.String(500), unique=False, nullable=True)
    habitat = db.Column(db.String(500), unique=False, nullable=True)
    population = db.Column(db.String(500), unique=False, nullable=True)
    weight = db.Column(db.String(500), unique=False, nullable=True)
    lifespan = db.Column(db.String(500), unique=False, nullable=True)
    speed = db.Column(db.String(500), unique=False, nullable=True)
    color = db.Column(db.String(500), unique=False, nullable=True)
    image = db.Column(db.String(100), unique=False, nullable=True)
    location_map_link = db.Column(db.String(100), unique=False, nullable=True)




db.create_all()


# for link in animal_links:
#     r = requests.get(link)
#     response = r.content
#     soup = BeautifulSoup(response, 'html.parser')
#     try:
#         location = soup.select('div.col-lg-6 ul.list-unstyled')[1].text
#     except IndexError:
#         location = "unknown"
#     classification = soup.select('dt')
#     facts = soup.select('div dd')
#     class_list = [class_item.text for class_item in classification]
#     fact_list = [fact_item.text for fact_item in facts]
#     prey = ""
#     habitat = ""
#     population = ""
#     weight = ""
#     lifespan = ""
#     speed = ""
#     color = ""
#     for iter in range(len(class_list)):
#         if class_list[iter] == 'Prey':
#             prey = fact_list[iter]
#         if class_list[iter] == 'Habitat':
#             habitat = fact_list[iter]
#         if class_list[iter] == 'Estimated Population Size':
#             population = fact_list[iter]
#         if class_list[iter] == 'Weight':
#             weight = fact_list[iter]
#         if class_list[iter] == 'Lifespan':
#             lifespan = fact_list[iter]
#         if class_list[iter] == 'Top Speed':
#             speed = fact_list[iter]
#         if class_list[iter] == 'Color':
#             color = fact_list[iter]
#
#     animal_images = soup.select('img.center-block')
#     img_link = [pic['data-lazy'] for pic in animal_images]
#
#     location_link = ""
#     location_links = soup.select('img.animal-location-map')
#     for img in location_links:
#         location_link = img['src']
#
#     try:
#         animal_image = random.choice(img_link)
#     except IndexError:
#         animal_image = "NULL"
#
#     try:
#         name = soup.find('h1').text
#     except AttributeError:
#         name = "Unknown"
#
#     try:
#         fact = soup.find(class_="mb-0").text
#     except AttributeError:
#         fact = "Unknown"
#
#
#     new_animal = Animal(name=name, fact=fact, location=location, prey=prey, habitat=habitat, population=population, weight=weight, lifespan=lifespan, speed=speed, color=color, image=animal_image, location_map_link=location_link)
#
#     db.session.add(new_animal)
#     db.session.commit()


#update animal
# animal_update = db.session.query(Animal).filter_by(name="Panther").first()
# animal_update.name= "Black Panther"
# db.session.commit()

# get all the animals and info


# read a animal
# animal = Animal.query.filter_by(id= random.randint(1, 1265)).first()
# print(animal.name)
# print(animal.image)
animal_1 = Animal.query.filter_by(id=random.randint(1, 1265)).first()

@app.route("/")
def home():
    main_animal = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    animal_1 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    animal_2 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    animal_3 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_1 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_2 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_3 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_4 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_5 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_6 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_7 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_8 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_9 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_10 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_11 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    gallery_12 = Animal.query.filter_by(id=random.randint(1, 1265)).first()
    return render_template("index.html", animal=main_animal, animal_1=animal_1, animal_2=animal_2, animal_3=animal_3,
                           gallery_1=gallery_1, gallery_2=gallery_2, gallery_3=gallery_3, gallery_4=gallery_4, gallery_5=gallery_5,
                           gallery_6=gallery_6, gallery_7=gallery_7, gallery_8=gallery_8, gallery_9=gallery_9, gallery_10=gallery_10,
                           gallery_11=gallery_11, gallery_12=gallery_12)



if __name__ == '__main__':
    app.run(debug=True)
