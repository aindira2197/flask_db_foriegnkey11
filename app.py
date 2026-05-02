from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)

class Hotel(db.Model):
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    rooms = db.relationship('Room', backref='hotel', cascade="all, delete")


class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)

    number = db.Column(db.String(20))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id', ondelete='CASCADE'))

    bookings = db.relationship('Booking', backref='room', cascade="all, delete")


class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id', ondelete='CASCADE'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id', ondelete='CASCADE'))

    check_in = db.Column(db.String(20))
    check_out = db.Column(db.String(20))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


menga shunaqa 100 foiz toliq qilib 5 ta masala yozib ber
