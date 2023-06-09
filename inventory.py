from crud import get_items, get_item
from num2words import num2words

def get_single_item(id):
    return get_item(id)


def get_inventory():
    inventory = get_items()
    invent = {}
    for i, item in enumerate(inventory):
            
        temp = { 
                "id" : num2words(item.id), 
                "title" : item.title,
                "category": item.category,
                "pic_path":item.picture.url,
                "total_inv": 0,
                "variations": {}
            }
        
        # if items are sized without variations
        if item.sized_qty:
            temp["sized_qty"] = {
                "s":item.qty.s,
                "m":item.qty.m,
                "l":item.qty.l,
                "xl":item.qty.xl,
                "xxs":item.qty.xxs,
                "xs":item.qty.xs,
                "4ft":item.qty.four_ft,
                "6ft":item.qty.six_ft
                }
            # we will count all items in inventory for a total
            for count in temp['sized_qty'].values():
                if count:
                    temp['total_inv'] = temp.get('total_inv', 0) + count

        # for variations without quantity or price difference
        if item.var_without_quantity:
            temp["variations_no_qty"] = item.var_without_quantity.split(',')

        # for variations with quantity and price differences
        if item.var1:
            temp["variations"][item.var1_qty.variation] = {
                "s" : item.var1_qty.s,
                "m" : item.var1_qty.m,
                "l": item.var1_qty.l,
                "xl" : item.var1_qty.xl,
                "xxs": item.var1_qty.xxs,
                "xs": item.var1_qty.xs,
                "4ft" : item.var1_qty.four_ft,
                "6ft" : item.var1_qty.six_ft,
                "s$" : item.var1_qty.s_cost,
                "m$" : item.var1_qty.m_cost,
                "l$": item.var1_qty.l_cost,
                "xl$" : item.var1_qty.xl_cost,
                "xxs$": item.var1_qty.xxs_cost,
                "xs$": item.var1_qty.xs_cost,
                "4ft$" : item.var1_qty.four_ft_cost,
                "6ft$" : item.var1_qty.six_ft_cost
            }
            for key in temp['variations'][item.var1_qty.variation].keys():
                dic = temp['variations'][item.var1_qty.variation]
                if dic[key] and '$' not in key:
                    temp['total_inv'] = temp.get('total_inv', 0) + dic[key]

        if item.var2:
            temp["variations"][item.var2_qty.variation] = {
                "s" : item.var2_qty.s,
                "m" : item.var2_qty.m,
                "l": item.var2_qty.l,
                "xl" : item.var2_qty.xl,
                "xxs": item.var2_qty.xxs,
                "xs": item.var2_qty.xs,
                "4ft" : item.var2_qty.four_ft,
                "6ft" : item.var2_qty.six_ft,
                "s$" : item.var2_qty.s_cost,
                "m$" : item.var2_qty.m_cost,
                "l$": item.var2_qty.l_cost,
                "xl$" : item.var2_qty.xl_cost,
                "xxs$": item.var2_qty.xxs_cost,
                "xs$": item.var2_qty.xs_cost,
                "4ft$" : item.var2_qty.four_ft_cost,
                "6ft$" : item.var2_qty.six_ft_cost
            }
            for key in temp['variations'][item.var2_qty.variation].keys():
                dic = temp['variations'][item.var2_qty.variation]
                if dic[key] and '$' not in key:
                    temp['total_inv'] = temp.get('total_inv', 0) + dic[key]

        if item.var3:
            temp["variations"][item.var3_qty.variation] = {
                "s" : item.var3_qty.s,
                "m" : item.var3_qty.m,
                "l": item.var3_qty.l,
                "xl" : item.var3_qty.xl,
                "xxs": item.var3_qty.xxs,
                "xs": item.var3_qty.xs,
                "4ft" : item.var3_qty.four_ft,
                "6ft" : item.var3_qty.six_ft,
                "s$" : item.var3_qty.s_cost,
                "m$" : item.var3_qty.m_cost,
                "l$": item.var3_qty.l_cost,
                "xl$" : item.var3_qty.xl_cost,
                "xxs$": item.var3_qty.xxs_cost,
                "xs$": item.var3_qty.xs_cost,
                "4ft$" : item.var3_qty.four_ft_cost,
                "6ft$" : item.var3_qty.six_ft_cost
            }
            for key in temp['variations'][item.var3_qty.variation].keys():
                dic = temp['variations'][item.var3_qty.variation]
                if dic[key] and '$' not in key:
                    temp['total_inv'] = temp.get('total_inv', 0) + dic[key]
        if item.var4:
            temp["variations"][item.var4_qty.variation] = {
                "s" : item.var4_qty.s,
                "m" : item.var4_qty.m,
                "l": item.var4_qty.l,
                "xl" : item.var4_qty.xl,
                "xxs": item.var4_qty.xxs,
                "xs": item.var4_qty.xs,
                "4ft" : item.var4_qty.four_ft,
                "6ft" : item.var4_qty.six_ft,
                "s$" : item.var4_qty.s_cost,
                "m$" : item.var4_qty.m_cost,
                "l$": item.var4_qty.l_cost,
                "xl$" : item.var4_qty.xl_cost,
                "xxs$": item.var4_qty.xxs_cost,
                "xs$": item.var4_qty.xs_cost,
                "4ft$" : item.var4_qty.four_ft_cost,
                "6ft$" : item.var4_qty.six_ft_cost
            }
            for key in temp['variations'][item.var4_qty.variation].keys():
                dic = temp['variations'][item.var4_qty.variation]
                if dic[key] and '$' not in key:
                    temp['total_inv'] = temp.get('total_inv', 0) + dic[key]

        invent[i] = temp
    return invent