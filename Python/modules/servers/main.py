from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
# db.Column : Table 의 column 을 만든다,
class Cafe(db.Model):
    # __init__ method 는 SQLAlchemy 가 자동 생성

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # serialising our database row Object to JSON
    # converting it to a JSON structure.
    def to_dict(self):
        cafe_dict = {}
        for column in self.__table__.columns:
            cafe_dict[column.name] = getattr(self, column.name)
        return cafe_dict

    def to_dict_2(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")  # decorator 패턴, URL 연결에 사용
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_get_request():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)

    # dict type 의 자료를 반환하는 Cafe class 의 method 를 정의한다.
    """
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })
    """
    return jsonify(cafe=random_cafe.to_dict())


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)