# dicts.py


# craeating some basic dictionary, acees to values via keys

my_dict = {
    "oem":"audi",
    "model":"avant",
    "power":'123_bhp'
}

print(my_dict["oem"])

# change some value

my_dict['power'] = "145bhp"
print(my_dict)

my_dict['condition'] = 'new'
print(my_dict)

# remove some value
my_dict.pop('model')
print(my_dict)