#initial dictionary
d2 = {1:10, 2:20, 3:30, 4:40, 5:50}
def insert_item(d, key, value):
    d[key] = value 

    print(f'After inserting ({key}: {value}: {d})')
def update_item(d, key, new_value):
    if key in d:
        d[key] = new_value
        print(f'Updated key {key} to new value {new_value}: {d}')
    else:
        print(f'Key {key} not found in dictionary. No update made.')
def delete_item(d, key):
    if key in d:
        del d[key]
        print(f'Deleted key {key}: {d}')
    else:
        print(f'Key {key} not found in dictionary. No deletion made.')

#insert a new item
insert_item(d2,6,60)

#update an existing item
update_item(d2, 2, 25)

#delete an existing item
delete_item(d2, 3)

#ptint the final dictionary
print(f'Final dictionary: {d2}')