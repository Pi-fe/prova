programming_language = {'python' : "Guido van Rossum", 'perl' : "Larry Wall", 'c' : "Kerninghan and Ritchie",}

print(programming_language)


for key, value in programming_language.items():
    print("name: " + key)
    print("author: " + value)

#looping all the keys

for key in programming_language.keys():
    print("name: " + key)

#default iteration schema: by key

for key in programming_language:
    print("name: "+key)


#looping all the values

for value in programming_language.values():
    print("author: " + value)

#adding an element

programming_language['ruby'] = "Yukihiro 'Matz' Matsumoto"

for key, value in programming_language.items():
    print("name: " + key)
    print("author: "+ value)


#removing an element

del programming_language['perl']

for key, value in programming_language.items():
    print("name: " + key)
    print("author: "+ value)


#popping an element

programming_language.pop('ruby')
'Matz'
for key, value in programming_language.items():
    print("name: " + key)
    print("author: "+ value)