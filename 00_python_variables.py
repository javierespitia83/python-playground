"""Project: Testig variables and methods
Description: File to test git
Author: [javierespitia83]
Version: 1.0.0
date: 2026-02-118
# Notes:
# Lists: [item1, item2, ...]
# Methods: append(), extend(), insert(), remove(), pop(), index(), count(), sort(), reverse(), clear()
# Tuples: (item1, item2, ...)
# Immutable. Methods: count(), index()
# Sets: {item1, item2, ...}
# Unordered, unique elements. Methods: add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), update()
# Dictionaries: {key1: value1, key2: value2, ...}
# Methods: keys(), values(), items(), get(), pop(), update(), clear(), setdefault()
"""
#String Exercise
welcome = "Hola Javier"
welcome =  welcome.replace("Javier", "Carlos")
email = "JAVIERESPITIA83@GMAIL.COM"
email = email.lower()
print(welcome)
print(email)
#List, Dict, Set, and Tuple Exercise
#List Exercise
tech_company = ["meta", "openai", "Amazon", "Apple", "Cisco"]
tech_company = tech_company + ["Juniper"]
print(tech_company)
print(tech_company[-1])
print(tech_company[0::2])

#Dic Exercise
routers_inventory = {'rtcore':"10.0.0.1", 'rtdistribution':"10.0.0.2"}
routers_inventory['rtcore']="10.0.0.254"
print(routers_inventory.items())
#Set Exercise
social_networks = {"facebook", "instagram", "X"}
social_networks.add("linkedin")
print(sorted(social_networks))
#tuppla exercise
DB_config = ("10.0.0.254", 1521, "Oracle_user", "myPass")

