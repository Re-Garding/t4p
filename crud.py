from model import *



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
        blurb,
        wash,
        width,
        holiday,  
        pic,         
        pic2=None, 
        reflect=False, 
        no_var_qty=None, 
        var1=None, 
        var2=None, 
        var3=None,
        var4=None, 
        var_without_quantity=None
    ):
    """create a new db item"""
    item = Item(title=title, 
                category=category, 
                keywords=keywords,
                blurb=blurb, 
                washable=wash, 
                width=width,
                holiday=holiday, 
                pic_path=pic, 
                reflective=reflect, 
                pic2_path = pic2,
                no_var_qty=no_var_qty, 
                var1 = var1, 
                var2=var2,
                var3=var3, 
                var4=var4, 
                var_without_quantity=var_without_quantity
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
        _4ft = None,
        _4ft_cost=None, 
        _6ft = None,
        _6ft_cost=None, 
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
        _4ft = _4ft,
        _4ft_cost=_4ft_cost, 
        _6ft = _6ft,
        _6ft_cost=_6ft_cost, 
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
        _4ft = None,
        _4ft_cost=None, 
        _6ft = None,
        _6ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None
        ):
    """quantities for no variation items"""

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
        _4ft = _4ft,
        _4ft_cost=_4ft_cost, 
        _6ft = _6ft,
        _6ft_cost=_6ft_cost, 
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
        _4ft = None,
        _4ft_cost=None, 
        _6ft = None,
        _6ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None):
    """quantities for no variation items"""

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
        _4ft = _4ft,
        _4ft_cost=_4ft_cost, 
        _6ft = _6ft,
        _6ft_cost=_6ft_cost, 
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
        _4ft = None,
        _4ft_cost=None, 
        _6ft = None,
        _6ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None
        ):
    """quantities for no variation items"""

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
        _4ft = _4ft,
        _4ft_cost=_4ft_cost, 
        _6ft = _6ft,
        _6ft_cost=_6ft_cost, 
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
        _4ft = None,
        _4ft_cost=None, 
        _6ft = None,
        _6ft_cost=None, 
        xxs=None,
        xxs_cost=None, 
        xs=None,
        xs_cost=None):
    """quantities for no variation items"""

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
        _4ft = _4ft,
        _4ft_cost=_4ft_cost, 
        _6ft = _6ft,
        _6ft_cost=_6ft_cost, 
        xxs=xxs,
        xxs_cost=xxs_cost, 
        xs=xs,
        xs_cost=xs_cost 
    )
    db.session.add(item)
    db.session.commit()
    return item





def create_invoice(doc, user, date):
    invoice = Invoice(doc=doc, user=user, date=date)
    db.session.add(invoice)
    db.session.commit()
    return invoice




def create_sale(user, date, invoice, collar=None, leash=None):
    sale = Sale(user=user, date=date, invoice=invoice, collar=collar, leash=leash)
    db.session.add(sale)
    db.session.commit()
    return sale