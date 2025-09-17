def get_last(items):
    if not items:
        return None
    
    return items[-1]


items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
print(get_last(items))

items = []
print(get_last(items))