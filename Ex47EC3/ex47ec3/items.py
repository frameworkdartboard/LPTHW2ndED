# items.py

class item(object):

    def __init__(self, shortname, longname, desc):
        self.shortname = shortname
        self.longname = longname
        self.desc = desc

item_list = { 
 "singing_sword" : item("singing_sword", "Singing Sword", "this sword is singing with violent energies!" +
  "I sure would hate to be hit by this thing!") ,
 "wolf_head" : item("wolf_head", "Wolf's-Head", "this is a crappy looking helm. it does seem to raise" + 
  " your AC though, or is that lower i never remember how that works :/") , 
 "bag_full_o_gold" : item("bag_full_o_gold", "Bag Full O' Gold", "It's a bag full o' gold.  YOU'LL LIVE LIKE" +
 " A KING. A KING, I SAY!") 
}
