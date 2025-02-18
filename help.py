import numpy as np
import pymongo
from pymongo import MongoClient
from faker import Faker
from random import randint, choice
import datetime
import time

raw_matirals = [
    ("Salt", "kg",10),
    ("Papad (Sagun)", "kg",50),
    ("Sugar", "kg",40),
    ("Poha", "kg",40),
    ("Maida", "kg",40),
    ("Atta", "kg",30),
    ("Sooji", "kg",50),
    ("Shabji Biryani Masala", "kg",550),
    ("Kitchen King", "kg",750),
    ("Paw Bhaji Masala", "kg",440),
    ("Sambhar Masala", "kg",600),
    ("Chiken Masala", "kg",1000),
    ("Chana Masala Chole Masala)", "kg",800),
    ("Chat Masala (100gm) 1Pkt", "kg",100),
    ("Kasoori Methi(250gm) 1pkt", "kg",200),
    ("Jeera", "kg",400),
    ("Hing", "bo",100),
    ("Rose Water", "bo",200),
    ("Orange Red Powder", "bo",340),
    ("Apple Green Powder", "bo",440),
    ("Gole Marij Kali Mirch)", "kg",560),
    ("Orange Red Powder Apple Green Powder", "kg",1020),
    ("Gole Marij(Kali Mirch)", "kg",560),
    ("Kala Jeera", "kg",500),
    ("Bada", "kg",400),
    ("Ajwain", "kg",700),
    ("Mirchi Powder", "kg",200),
    ("Haldi Powder", "kg",200),
    ("Sendha Namak (500gm) 1pkt", "kg",30),
    ("Dhaniya Powder", "kg",300),
    ("Bourn Vita", "kg",300),
    ("Horlicks", "kg",470),
    ("Javitri", "kg",600),
    ("Dal Chini", "kg",600),
    ("Sewai", "kg",70),
    ("Arhar Dal (Toor Dal)", "kg",100),
    ("Kabuli Chana", "kg",120),
    ("Besan", "kg",80),
    ("Rajma", "kg",150),
    ("Chay Patti (Tea Leaves)", "kg",250),
    ("Chay Patti (Tea Leaves)", "kg",250),
    ("Phalli Dana (Peanut)", "kg",130),
    ("Moong Dal", "kg",120),
    ("Urad Dal", "kg",160),
    ("Chana Dal", "kg",80),
    ("Green Moong (Khada Moong)", "kg",120),
    ("White Matar", "kg",150),
    ("Dhaniya Khada", "kg",200),
    ("Black Chana", "kg",70),
    ("Sabudana", "kg",80),
    ("Rice", "kg",48),
    ("Idly Rice", "kg",40),
    ("Soyabin Bari", "kg",100),
    ("Tomato Souce", "bo",80),
    ("Pickle", "bo",400),
    ("Green Chilli (Souce)", "bo",150),
    ("Red Chilli (Souce)", "bo",150),
    ("Oil Dalda", "kg",130),
    ("Soya Souce", "kg",130),
    ("Vinegar", "kg",200),
    ("Tomato Souce (Pouch)", "kg",97),
    ("Water Tulsi", "kg",340),
    ("oil", "ltr",157),
    ("Maza", "ltr",57),
    ("Sprite", "ltr",55),
    ("Thums Up", "kg",47),
    ("Magaj", "kg",630),
    ("Methi", "kg",230),
    ("Masoor Dal", "kg",140),
    ("Mastered Seed Ajina Moto Salt", "kg",70),
    ("Kewada Water", "kg"),
    ("Corn Flower (Makka Atta Ararot)", "kg",340),
    ("Frymes (Tikona Papad)", "kg",300),
    ("Tamrind (imali)", "kg",90),
    ("Sattu Atta", "kg",60),
    ("Rosted Chana", "kg",100),
    ("Ghadi Powder", "kg",58),
    ("V-Hari Mirch-K", "kg",60),
    ("V-Karela", "kg",40),
    ("V-Kheera", "kg",30),
    ("V-Khekhasi", "kg",80),
    ("V-Lauki", "kg",20),
    ("V-Parval", "kg",30),
    ("V-Mooli", "kg",30),
    ("V-Methi bhaji", "kg",50),
    ("V-Green Matar", "kg",60),
    ("V-Palak Bhaji", "kg",30),
    ("V-Kadhi Leaves V-Spring Onion", "kg",30),
    ("V-Kela", "kg",30),
    ("V-Nibu (PIC/NOS)", "kg",50),
    ("V-Kundru", "kg",50),
    ("-Kaddu", "kg",40),
    ("V-Hari Mirchi Big-K", "kg",80),
    ("V-Shimla", "kg",30),
    ("V-Tamatar", "kg",10),
    ("V-Lal Bhaji", "kg",40),
    ("V-Semi V-Pyaj", "kg",30),
    ("V-Aloo", "kg",20),
    ("Lahspon", "kg",50),
    ("Green Elaichi", "kg",2000),
    ("Sauf", "kg"),
    ("Kaju Tukada", "kg",800),
    ("Long", "kg",1700),
    ("Kismis", "kg",200),
    ("Soda", "kg",70),
    ("Tartari", "kg",1500),
    ("Mastered Oil", "kg",155),
    ("Coffee (90gm) 1pkt ", "kg",332),
    ("Pairie-G (Rs-5/-)", "kg"),
    ("Good Day (Rs-10/-)", "kg"),
    ("Chicken", "kg",200),
    ("Amul Butter", "kg",800),
    ("Amul Cheese", "kg",600),
    ("Chocolate Syrup", "kg",200),
    ("Pizza Souce", "kg",170),
    ("Veg Mayonmise", "kg",180),
    ("Sweet Corn", "kg",52),
    ("GREEN MATAR", "kg",40),
    ("Burger Tikki", "pcs",25),
    ("French Fries", "kg",340),
    ("Yellow Color", "bo",),
    ("Maggi (280g pkt)", "kg",40),
    ("Gulab Jal (250ml) 1Bott", "bo",50),
]


CLIENT = MongoClient("mongodb://localhost:27017")
user_data = CLIENT["aviskar"]["users_data"]

faker_data = Faker(locale="en_IN")

genrate_data_of = input("Enter what kind of data to genrate:- ")

if genrate_data_of == "user":
    for i in range(int(input("Enter the number of user to input:- "))):
        while True:
            phone = faker_data.phone_number()
            if phone[0] == "+":
                break
            else:
                continue
        today = str(datetime.date.today())
        age = randint(15, 65)
        dob = str(int(today[:4]) - age) + today[4:]

        collage = "RCST"
        course = "BCA"
        collage_year = randint(1, 4)

        you_are_data_list = ["student", "non-student"]
        you_are = choice(you_are_data_list)
        if you_are != "student":
            collage = None
            course = None
            collage_year = None

        user = {
            "username": faker_data.name(),
            "email": faker_data.email(),
            "password": faker_data.password(),
            "date_of_birth": dob,
            "you_are": {
                you_are: {
                    "collage": collage,
                    "course": course,
                    "collage_year": collage_year,
                }
            },
            "gender": choice(["Male", "Female"]),
            "age": age,
            "favorite_color": faker_data.color_name(),
            "address": faker_data.address().replace("\n", " "),
            "phone": phone,
            "privilege": "user",
        }
        user_data.insert_one(user)

elif genrate_data_of == "menu":
    food_list = {
        "plain dosa": 20,
        "masala dosa": 25,
        "cutpiece dosa": 30,
        "uttapam": 25,
        "sambhar vada (2cps)": 20,
        "idly (2pcs)": 15,
        "poha": 15,
        "chana poha": 20,
        "samosa (2pcs)": 20,
        "samosa mutter": 25,
        "dahi samosa": 30,
        "aalu gunda (2pcs)": 15,
        "aalu gunda mutter": 20,
        "tea": 10,
        "coffee": 15,
        "sabudana khichdi": 20,
        "sabudana vada (3pcs)": 20,
        "hot milk per glass": 15,
        "aalo paratha": 30,
        "paneer paratha": 30,
        "chhole bhature": 30,
        "veg sandwitch": 20,
        "bread pakoda (1pcs)": 10,
        "bhajiya piyagi": 15,
        "pyaji vada": 10,
        "momos (6pcs)": 20,
    }
    user = [
        {
            "name": i,
            "price": j,
            "quantity": {"half": round(j / 2), "full": j},
            "discount": None,
        }
        for i, j in food_list.items()
    ]

    user_data = CLIENT["aviskar"]["menu_item"].insert_many(user)

elif genrate_data_of == "sales":
    data = list(user_data.find({}, limit=int(input("Number of user:- "))))
    menu_data = list(CLIENT["aviskar"]["menu_item"].find({}))

    for i in data:
        item = {}
        for _ in range(randint(1, 10)):
            x = choice(menu_data)
            item.update({x["name"]: {"price": x["price"], "quantity": randint(1, 10)}})

        bought = {
            "items": item,
            "total": sum([i["price"] * i["quantity"] for i in item.values()]),
        }
        date_time = str(faker_data.date_time_this_year()).split(" ")
        item_data = {
            "username": i["username"],
            "email": i["email"],
            "phone": i["phone"],
            "bought": bought,
            "date": date_time[0],
            "time": date_time[1],
        }
        user_data = CLIENT["aviskar"]["sales"].insert_one(item_data)

elif genrate_data_of == "in out":
    def generate_raw_matarial(x: int):
        raw_m = list(set([choice(raw_matirals) for _ in range(x)]))

        return {i[0]: {"quintity": randint(5, 100), "unit": i[1]} for i in raw_m}


    generate_raw_matarial(randint(5, 30))


    def genrate_date(from_, to):
        return [str(i) for i in np.arange(from_, to, dtype="datetime64[D]")]


    date_data = genrate_date("2022-01", "2022-12-23")

    i_data = [
        {
            i: {
                "in": generate_raw_matarial(randint(5, 30)),
                "out": generate_raw_matarial(randint(5, 30)),
            }
        }
        for i in date_data
    ]

    raw_mar_data = CLIENT["aviskar"]["in_out"]
    raw_mar_data.insert_many(i_data)

    print(raw_mar_data.find({}))

elif genrate_data_of == "raw material":
    pass
