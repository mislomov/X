# Dictionary Exercises

# 1. Sort a Dictionary by Value
def sort_dict_by_value(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

# 2. Add a Key to a Dictionary
def add_key_to_dict(d, key, value):
    d[key] = value
    return d

# 3. Concatenate Multiple Dictionaries
def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# 4. Generate a Dictionary with Squares
def generate_squares_dict(n):
    return {x: x*x for x in range(1, n+1)}

# 5. Dictionary of Squares (1 to 15)
def squares_dict_1_to_15():
    return {x: x*x for x in range(1, 16)}

# Set Exercises

# 1. Create a Set
def create_set(elements):
    return set(elements)

# 2. Iterate Over a Set
def iterate_over_set(s):
    for item in s:
        print(item)

# 3. Add Member(s) to a Set
def add_members_to_set(s, *members):
    s.update(members)
    return s

# 4. Remove Item(s) from a Set
def remove_items_from_set(s, *items):
    for item in items:
        s.discard(item)
    return s

# 5. Remove an Item if Present in the Set
def remove_item_if_present(s, item):
    s.discard(item)
    return s