#Logik für Warenkorb
#cart wird in der Flask-Session gespeichert, nicht in DB
def cart_get(session_obj):
    return session_obj.get("cart", []) #bekommt Elemente aus route /cart/add

def cart_add_item(session_obj, item):
    items = session_obj.get("cart", [])
    items.append(item) #item wird an Liste gehängt
    session_obj["cart"] = items #Liste wieder in Session

def cart_remove_item(session_obj, item_index):
    items = session_obj.get("cart", []) #Warenkorb Liste holen
    if 0 <= item_index < len(items): #Index mind. 0 und kleiner als Anzahl der Elemente der Liste
        items.pop(item_index) #Element an Position von item_index wird gelöscht
        session_obj["cart"] = items 

def cart_clear(session_obj):
    session_obj.pop("cart", None) #cart wird geleert

def cart_get_item(session_obj, item_index):
    items = session_obj.get("cart", [])
    if 0 <= item_index < len(items):
        return items[item_index] #entsprechendes Item wird zurückgegeben
    return None #wenn ungültig -> none zurückgeben

def cart_set_item(session_obj, item_index, item):
    items = session_obj.get("cart", [])
    if 0 <= item_index < len(items):
        items[item_index] = item #Item an entsprechender Stelle einsetzen
        session_obj["cart"] = items #Liste wieder speichern
