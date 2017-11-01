class Smartphone(object):
    def __init__(self, manufacturer, model, year, chip, os, display, battery, capacity):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.chip = chip
        self.os = os
        self.display = display
        self.battery = battery
        self.capacity = capacity
    def productname(self):
        return str(self.year) + " " + self.manufacturer + " " + self.model 
    def __repr__(self):
        return self.productname()
    def speclist(self):
        return "This device features a " + self.display + " display, powered by the " + self.chip + " SoC, runs " + self.os + " out of the box, with a " + str(self.battery) + " capacity battery and " + str(self.capacity) + " GB of on-board storage."
        
current_year = 2017

addison = Smartphone('Motorola', 'Moto Z Play', 2016, 'Snapdragon 625', 'Android 6.0 Marshmallow', '5.7 inch Full HD AMOLED', 3510, 32)
bacon = Smartphone('OnePlus', 'One', 2014, 'Snapdragon 801', 'Android 4.4 KitKat', '5.5 inch Full HD IPS LCD', 3100, 64)
angler = Smartphone('Huawei', 'Nexus 6P', 2015, 'Snapdragon 810', 'Android 6.0 Marshmallow', '5.7 inch Quad HD AMOLED', 3450, 32)
bullhead = Smartphone('LG', 'Nexus 5X', 2015, 'Snapdragon 808', 'Android 6.0 Marshmallow', '5.2 inch Full HD AMOLED', 2700, 32)
anniversary = Smartphone('Apple', 'iPhone X', 2017, 'A11 Bionic', 'iOS 11', '5.8 inch Full HD+ AMOLED', 2716, 64)
toro = Smartphone('Samsung', 'Galaxy Nexus', 2011, 'OMAP 4460', 'Android 4.0 Ice Cream Sandwich', '4.7 inch HD AMOLED', 1750, 16)

phone_list = [addison, bacon, angler, bullhead, anniversary, toro]

age_list = []
def ages(phones):
    for device in phones:
        device_age = current_year - device.year
        if device_age == 0:
            age_list.append("The " + device.manufacturer + " " + device.model + " was released this year.")
        elif device_age == 1:
            age_list.append("The " + device.manufacturer + " " + device.model + " was released last year.")
        elif device_age < 0:
            age_list.append("The " + device.manufacturer + " " + device.model + " will come out at some time in the future!")
        else:
            age_list.append("The " + device.manufacturer + " " + device.model + " was released " + str(device_age) + " years ago.")
    return age_list

ages(phone_list)
print age_list
