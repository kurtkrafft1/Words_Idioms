my_family = {
    "sister": {
        "name": "Meg",
        "age": 29
    },
    "mother": {
        "name": "Ann",
        "age": 65
    },
    "aunt": {
        "name": "Kim",
        "age": 68
    },
    "aunt": {
        "name": "Delinda",
        "age": 65
    },
    "uncle": {
        "name": "Don",
        "age": 70
    }
}

members = my_family.items()
for member in members: 
    print(f'{member[1]["name"]} is my {member[0]} and is {member[1]["age"]} years old.')
