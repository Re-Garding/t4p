from model import *


def get_item(id):
    return Item.query.get(id)

def new_pic(url, item_id=None):
    pic = Picture(url=url, item_id=item_id)
    db.session.add(pic)
    db.session.commit()
    return pic

def add_item_to_pic(pic_id, item_id):
    pic = Picture.query.get(pic_id)
    pic.item_id = item_id
    db.session.commit()



def create_user(email, fname, lname, password, street=None,
                city=None, state=None, zipcode=None, unit=None, ):
     
     """create a user"""

     user = User(
                email=email, 
                fname=fname, 
                lname=lname, 
                password=password, 
                street_address=street, 
                city=city, 
                state=state, 
                zipcode=zipcode,
                unit_num=unit
                )
     
     db.session.add(user)
     db.session.commit()    
     return user



def create_item(
        title, 
        category,
        keywords, 
        wash,
        width,
        width_unit,
        length,
        length_unit,
        holiday,  
        reflect=False, 
        quantity=None,
        price = None,
        sized_qty = None,
        var1=None, 
        var2=None, 
        var3=None,
        var4=None, 
        var_without_quantity=None,
        materials_used=None,
        handmade=None,
        primary_color=None,
        secondary_color=None,
        collar_type=None,
        closure_type=None,
        item_type=None,
        pic=None
    ):
    """create a new db item"""
    item = Item(title=title, 
                category=category, 
                keywords=keywords,
                washable = wash,
                width=width,
                width_unit=width_unit,
                length=length,
                length_unit=length_unit,
                holiday=holiday,  
                reflective=reflect, 
                quantity=quantity,
                price = price,
                sized_qty=sized_qty,
                var1=var1, 
                var2=var2, 
                var3=var3,
                var4=var4, 
                var_without_quantity=var_without_quantity,
                materials_used=materials_used,
                handmade=handmade,
                primary_color=primary_color,
                secondary_color=secondary_color,
                collar_type=collar_type,
                closure_type=closure_type,
                item_type=item_type,
                pic=pic
                )
    db.session.add(item)
    db.session.commit()
    return item



def create_qty(
        s = None,
        s_cost = None, 
        m = None,
        m_cost=None, 
        l = None,
        l_cost=None, 
        xl = None,
        xl_cost=None, 
        four_ft = None,
        four_ft_cost=None, 
        six_ft = None,
        six_ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None
        ):
    """quantities for no variation items"""

    item = Quantity(
        s = s,
        s_cost = s_cost, 
        m = m,
        m_cost=m_cost, 
        l = l,
        l_cost=l_cost, 
        xl = xl,
        xl_cost=xl_cost, 
        four_ft = four_ft,
        four_ft_cost=four_ft_cost, 
        six_ft = six_ft,
        six_ft_cost=six_ft_cost, 
        xxs=xxs,
        xxs_cost=xxs_cost, 
        xs=xs,
        xs_cost=xs_cost 
    )
    db.session.add(item)
    db.session.commit()
    return item


def create_var1(
        variation, 
        s = None,
        s_cost = None, 
        m = None,
        m_cost=None, 
        l = None,
        l_cost=None, 
        xl = None,
        xl_cost=None, 
        four_ft = None,
        four_ft_cost=None, 
        six_ft = None,
        six_ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None
        ):
    """quantities for variation 1 items"""

    item = Variation1(
        variation=variation,
        s = s,
        s_cost = s_cost, 
        m = m,
        m_cost=m_cost, 
        l = l,
        l_cost=l_cost, 
        xl = xl,
        xl_cost=xl_cost, 
        four_ft = four_ft,
        four_ft_cost=four_ft_cost, 
        six_ft = six_ft,
        six_ft_cost=six_ft_cost, 
        xxs=xxs,
        xxs_cost=xxs_cost, 
        xs=xs,
        xs_cost=xs_cost
    )
    db.session.add(item)
    db.session.commit()
    return item



def create_var2(variation,
        s = None,
        s_cost = None, 
        m = None,
        m_cost=None, 
        l = None,
        l_cost=None, 
        xl = None,
        xl_cost=None, 
        four_ft = None,
        four_ft_cost=None, 
        six_ft = None,
        six_ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None):
    """quantities for variation 2 items"""

    item = Variation2(
        variation=variation,
        s = s,
        s_cost = s_cost, 
        m = m,
        m_cost=m_cost, 
        l = l,
        l_cost=l_cost, 
        xl = xl,
        xl_cost=xl_cost, 
        four_ft = four_ft,
        four_ft_cost=four_ft_cost, 
        six_ft = six_ft,
        six_ft_cost=six_ft_cost, 
        xxs=xxs,
        xxs_cost=xxs_cost, 
        xs=xs,
        xs_cost=xs_cost 
    )
    db.session.add(item)
    db.session.commit()
    return item




def create_var3(
        variation,
        s = None,
        s_cost = None, 
        m = None,
        m_cost=None, 
        l = None,
        l_cost=None, 
        xl = None,
        xl_cost=None, 
        four_ft = None,
        four_ft_cost=None, 
        six_ft = None,
        six_ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None
        ):
    """quantities for variation 3 items"""

    item = Variation3(
        variation=variation, 
        s = s,
        s_cost = s_cost, 
        m = m,
        m_cost=m_cost, 
        l = l,
        l_cost=l_cost, 
        xl = xl,
        xl_cost=xl_cost, 
        four_ft = four_ft,
        four_ft_cost=four_ft_cost, 
        six_ft = six_ft,
        six_ft_cost=six_ft_cost, 
        xxs=xxs,
        xxs_cost=xxs_cost, 
        xs=xs,
        xs_cost=xs_cost
    )
    db.session.add(item)
    db.session.commit()
    return item



def create_var4(
        variation, 
        s = None,
        s_cost = None, 
        m = None,
        m_cost=None, 
        l = None,
        l_cost=None, 
        xl = None,
        xl_cost=None, 
        four_ft = None,
        four_ft_cost=None, 
        six_ft = None,
        six_ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None):
    """quantities for variation 4 items"""

    item = Variation4(
        variation=variation, 
        s = s,
        s_cost = s_cost, 
        m = m,
        m_cost=m_cost, 
        l = l,
        l_cost=l_cost, 
        xl = xl,
        xl_cost=xl_cost, 
        four_ft = four_ft,
        four_ft_cost=four_ft_cost, 
        six_ft = six_ft,
        six_ft_cost=six_ft_cost, 
        xxs=xxs,
        xxs_cost=xxs_cost, 
        xs=xs,
        xs_cost=xs_cost 
    )
    db.session.add(item)
    db.session.commit()
    return item

def get_items():
    """return all items in db"""
    return Item.query.all()



def create_invoice(doc, user, date):
    """generate a new invoice"""
    invoice = Invoice(doc=doc, user=user, date=date)
    db.session.add(invoice)
    db.session.commit()
    return invoice




def create_sale(user, date, invoice, collar=None, leash=None):
    """generate a new sale"""
    sale = Sale(user=user, date=date, invoice=invoice, collar=collar, leash=leash)
    db.session.add(sale)
    db.session.commit()
    return sale