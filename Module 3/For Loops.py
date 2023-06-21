# for letter in "SDCCD":
#     print(letter)

campuses = ["City", "Mesa", "Miramar"]
# print (len(campuses))

# for campus in campuses:
#     print(campus)

# for index in range(7,20):
#     print (index)

# my attempt
# i = 0
# for campus in campuses:
#     i += 1
#     print (str(i)+") "+campus)

i = 0
for campus in range(len(campuses)):
    i += 1
    print(str(i))
    print(campuses[campus])
