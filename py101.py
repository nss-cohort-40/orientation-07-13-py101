# Py 101

# variables
sum = 2 + 2

print("the value of sum is", sum)

name = "Fred"

def say_name():

    # global name
    name = "Linda"
    print("internal", name)

say_name()
print("external", name)

# if/else
name = "Larry"
if name == "Linda":
    print("I am Linda. Larry is on vacation.")
elif name == "Fred":
    print( "Welcome to Costco. I am Fred")
else:
    print("I am Larry")

# String interpolation
print(f"My name is {name}")

# No type coercion
# print(2 + "2") # no work!

# Collections!
# arrays #nope and objects # yes! But....

# js
# let stuff = {name: "", category: ""}

# list
more_stuff = [2, "things", True] # booleans are capitalized

more_stuff.append("wow!")
print(more_stuff[2]) #prints True
print(more_stuff[-1]) #prints wow!

more_stuff.insert(0, "Sorry bout that")
print(more_stuff)

more_stuff.extend([45, False, "blah"])
print(more_stuff)

# python: dictionary
stuff = {"name": "Sally", "category": "Manager"}

# reassign values
stuff["name"] = "Regina"
print(stuff["name"])

# Assign new properties
stuff["salary"] = "60,000"

# Nested values
stuff["address"] = {"street": "Sesame St", "num": 123}
print(stuff)

# access nested values
print(stuff["address"]["street"])

# Sets
junk = {"Curlies", "lies", 34, None}

junk.add("more stuff")
print(junk)

junk.add(34)
print(junk)

names = ["Joe", "Linda", "Fred", "Linda"]
print(names)

example = set()
example.add("hello")
print(example)

names = list(set(names))
print(names)

colors = []
print(colors)

# empty dict
addresses = {}
addresses["num"] = 123
print(type(addresses))

# tuple is cool because it's immutable
my_tup = (1,2,3, "hello")
print(my_tup[2])

# How does it know it's a tuple?
my_tup = (12,)
print(type(my_tup))

# loops
# for...in
my_tup = (1, 2, 3, 3, "hello")
my_set = {1, 2, 3}
junk = ["Fred", True, [1,2,3], 234]

for foo in junk:
    print(f"Why is {foo} still in here?")

for foo in my_tup:
    print(f"This is in my tup: {foo}")

for foo in my_set:
    print(f"Is this in any order? {foo}")

my_dict = {
    123: "number",
    "name": "Broomhilda"
}

for key, value in my_dict.items():
    print(f"What is the value? {key}: {value}")


# slicing
my_list = [1, 2, 4, "hello", "monkey"]
# The JS way
# let my_subset = my_list.slice(0,3)

my_subset = my_list[1:3]
print(my_subset)
my_subset = my_list[:3]
my_subset = my_list[3:]
print(my_subset)
my_subset = my_list[1:34] #doesn't break
print(my_subset)


# What kind of file is this?
print("name", __name__)

if __name__ == "__main__":
    print("Shut up, Joe.")
