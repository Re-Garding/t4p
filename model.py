"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


categories = ['clearence', 'movie/tv', 'disney', 'floral', 'animals',
               'patterns', 'halloween', 'Christmas', 'patriotic', 'food/drink',
               'video games', 'sayings'
               ]


class User(db.Model):
    """a user"""

    __tablename__ = 'users'
    
    email = db.Column(db.String(), primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(), nullable=False)
    street_address = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String(2))
    zipcode = db.Column(db.Integer())
    unit_num = db.Column(db.String())


    def __repr__(self):
        return f'<User name: {self.fname} email:{self.email}>'
    



    
class Item(db.Model):
    """an item for sale"""
     
    __tablename__ = 'items'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(), nullable= False)
    category = db.Column(db.String(), nullable= False)
    keywords = db.Column(db.String())
    blurb = db.Column(db.String())
    washable = db.Column(db.Boolean(), nullable= False)
    width = db.Column(db.Float(), nullable=False)
    holiday = db.Column(db.String(), nullable= False)
    pic_path = db.Column(db.String(), nullable= False)
    reflective = db.Column(db.Boolean, nullable=False)
    pic2_path = db.Column(db.String())
    no_var_qty = db.Column(db.Integer, db.ForeignKey('quantity.id'))
    var1 = db.Column(db.Integer, db.ForeignKey('var1.id'))
    var2 = db.Column(db.Integer, db.ForeignKey('var2.id'))
    var3 = db.Column(db.Integer, db.ForeignKey('var3.id'))
    var4 = db.Column(db.Integer, db.ForeignKey('var4.id'))
    var_without_quantity = db.Column(db.String())

    def __repr__(self):
        return f'Title: {self.title}'

    quantity = db.relationship('Quantity', backref='item')
    var1_qty = db.relationship('Variation1', backref='item')
    var2_qty = db.relationship('Variation2', backref='item')
    var3_qty = db.relationship('Variation3', backref='item')
    var4_qty = db.relationship('Variation4', backref='item')



class Quantity(db.Model):
    """quantity of a unique item"""

    __tablename__ = 'quantity'

    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    s = db.Column(db.Integer)
    s_cost = db.Column(db.Float())
    m = db.Column(db.Integer)
    m_cost  = db.Column(db.Float())
    l = db.Column(db.Integer)
    l_cost  = db.Column(db.Float())
    xl = db.Column(db.Integer)
    xl_cost = db.Column(db.Float())
    _4ft = db.Column(db.Integer)
    _4ft_cost = db.Column(db.Float())
    _6ft = db.Column(db.Integer)
    _6ft_cost = db.Column(db.Float())
    xxs = db.Column(db.Integer)
    xxs_cost = db.Column(db.Float())
    xs = db.Column(db.Integer)
    xs_cost = db.Column(db.Float())

    def __repr__(self):
        return f'Id {self.id}'    



class Variation1(db.Model):
    """quantity of a unique item"""

    __tablename__ = 'var1'

    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    variation = db.Column(db.String(), nullable=False)
    s = db.Column(db.Integer)
    s_cost = db.Column(db.Float())
    m = db.Column(db.Integer)
    m_cost  = db.Column(db.Float())
    l = db.Column(db.Integer)
    l_cost  = db.Column(db.Float())
    xl = db.Column(db.Integer)
    xl_cost = db.Column(db.Float())
    _4ft = db.Column(db.Integer)
    _4ft_cost = db.Column(db.Float())
    _6ft = db.Column(db.Integer)
    _6ft_cost = db.Column(db.Float())
    xxs = db.Column(db.Integer)
    xxs_cost = db.Column(db.Float())
    xs = db.Column(db.Integer)
    xs_cost = db.Column(db.Float())

    def __repr__(self):
        return f'Id {self.id} Variation: {self.variation}'
    


class Variation2(db.Model):
    """quantity of a unique item"""

    __tablename__ = 'var2'

    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    variation = db.Column(db.String(), nullable=False)
    s = db.Column(db.Integer)
    s_cost = db.Column(db.Float())
    m = db.Column(db.Integer)
    m_cost  = db.Column(db.Float())
    l = db.Column(db.Integer)
    l_cost  = db.Column(db.Float())
    xl = db.Column(db.Integer)
    xl_cost = db.Column(db.Float())
    _4ft = db.Column(db.Integer)
    _4ft_cost = db.Column(db.Float())
    _6ft = db.Column(db.Integer)
    _6ft_cost = db.Column(db.Float())
    xxs = db.Column(db.Integer)
    xxs_cost = db.Column(db.Float())
    xs = db.Column(db.Integer)
    xs_cost = db.Column(db.Float())

    def __repr__(self):
        return f'Id {self.id} Variation: {self.variation}'
    


class Variation3(db.Model):
    """quantity of a unique item"""

    __tablename__ = 'var3'

    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    variation = db.Column(db.String(), nullable=False)
    s = db.Column(db.Integer)
    s_cost = db.Column(db.Float())
    m = db.Column(db.Integer)
    m_cost  = db.Column(db.Float())
    l = db.Column(db.Integer)
    l_cost  = db.Column(db.Float())
    xl = db.Column(db.Integer)
    xl_cost = db.Column(db.Float())
    _4ft = db.Column(db.Integer)
    _4ft_cost = db.Column(db.Float())
    _6ft = db.Column(db.Integer)
    _6ft_cost = db.Column(db.Float())
    xxs = db.Column(db.Integer)
    xxs_cost = db.Column(db.Float())
    xs = db.Column(db.Integer)
    xs_cost = db.Column(db.Float())

    def __repr__(self):
        return f'Id {self.id} Variation: {self.variation}'
    


class Variation4(db.Model):
    """quantity of a unique item"""

    __tablename__ = 'var4'

    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    variation = db.Column(db.String(), nullable=False)
    s = db.Column(db.Integer)
    s_cost = db.Column(db.Float())
    m = db.Column(db.Integer)
    m_cost  = db.Column(db.Float())
    l = db.Column(db.Integer)
    l_cost  = db.Column(db.Float())
    xl = db.Column(db.Integer)
    xl_cost = db.Column(db.Float())
    _4ft = db.Column(db.Integer)
    _4ft_cost = db.Column(db.Float())
    _6ft = db.Column(db.Integer)
    _6ft_cost = db.Column(db.Float())
    xxs = db.Column(db.Integer)
    xxs_cost = db.Column(db.Float())
    xs = db.Column(db.Integer)
    xs_cost = db.Column(db.Float())

    def __repr__(self):
        return f'Id {self.id} Variation: {self.variation}'




class Invoice(db.Model):
    """store pdf invoices as blobs"""

    __tablename__ = 'invoices'

    invoice_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    doc = db.Column(db.LargeBinary())
    user_email = db.Column(db.String(), db.ForeignKey('users.email'), nullable=False)

    user = db.relationship('User', backref='invoice')

    def __repr__(self):
        return f'User: {self.user} Date: {self.date}'
    


class Sale(db.Model):
    """record of a specific item sold - It's id, user, invoice # """

    __tablename__ = 'sales'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_email = db.Column(db.String(), db.ForeignKey('users.email'), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    invoice = db.Column(db.Integer, db.ForeignKey('invoices.invoice_id'), nullable=False)

    user = db.relationship('User', backref='sale')


    

def connect_to_db(flask_app, db_uri="postgresql:///threads", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
