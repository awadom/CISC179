# LISTS
# --------------------
# Lists are tools to store a stream of strings
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Eric"]
# print(friends)
# print(friends[0])
# print(friends[1:5])

# DICTIONARIES
# --------------------
# Dictionaries are tools to store a stream of key-value pairs
# months = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }
# print(months["Feb"])
# print(months.get("Feb"))
# # error handling
# print(months.get("Sep", "Not found"))
# print(months.get("LOL", "Not found"))

# TUPLES
# --------------------
# Tuples are tools to store a stream of strings
# Tuples are like dictionaries in that they are indexed but unlike dictionaries they are ordered and unchanging
# dictionaries are unordered and changable
coodinates = (4, 5)
print(coodinates[1])

atuple = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Eric"]
# access Jim
print(atuple[2])
# access Jim to Toby
print(atuple[2:5])

# tuples cant be changed, lists can.
# tuples are immutable, lists are mutable.
# tuples are ordered, lists are ordered, dictionaries are unordered.
