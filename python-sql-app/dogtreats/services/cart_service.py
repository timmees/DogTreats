def cart_get(session_obj):
    return session_obj.get("cart", [])

def cart_add_item(session_obj, item):
    items = session_obj.get("cart", [])
    items.append(item)
    session_obj["cart"] = items

def cart_remove_item(session_obj, item_index):
    items = session_obj.get("cart", [])
    if 0 <= item_index < len(items):
        items.pop(item_index)
        session_obj["cart"] = items

def cart_clear(session_obj):
    session_obj.pop("cart", None)

def cart_get_item(session_obj, item_index):
    items = session_obj.get("cart", [])
    if 0 <= item_index < len(items):
        return items[item_index]
    return None

def cart_set_item(session_obj, item_index, item):
    items = session_obj.get("cart", [])
    if 0 <= item_index < len(items):
        items[item_index] = item
        session_obj["cart"] = items
