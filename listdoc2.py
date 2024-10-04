#type of list: homegeneus=
intergers = [1 , 2 , 3 , 4 , 5]
animal = ["dog", "cat", "goat"]
name = ["azahel", "Santiago", "Donovan"]
floats = [2.2, 3.3, 6.7, 10.3]
#type of lis: heterogeneous=
number_animels_name = [2, "cat", 34.33, "Travis"]
#list inside of a list
list_lists = [(1,2,3), ("cat", "dog", "spider")]
list = [2, 3, 3.4, 56, 100, 200, 210, 542, 1000]
#print(list[0])

words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yellow", 
    "zucchini", "apricot", "blackberry", "cantaloupe", "dragonfruit", "edamame",
    "flaxseed", "guava", "horseradish", "iceberg", "jackfruit", "kumquat", 
    "lime", "melon", "nutmeg", "olive", "peach", "pear", "pepper", "plum", 
    "quinoa", "radish", "spinach", "tomato", "turnip", "walnut", "yam", "zest",
    "artichoke", "broccoli", "carrot", "daikon", "endive", "fennel", "garlic", 
    "herb", "jalapeno", "kale", "leek", "mushroom", "nori", "okra", "parsnip",
    "quail", "rhubarb", "squash", "tarragon", "upland", "veggie", "wasabi", 
    "xanadu", "yucca", "zinnia", "avocado", "beet", "cabbage", "dill", "escarole", 
    "figs", "grapefruit", "hops", "jalapenos", "kiwifruit", "lima", "mangosteen", 
    "nectar", "olive", "pluot", "quesadilla", "romaine", "sorrel", "taro", 
    "watercress", "ximenia", "yarrow", "zucchini", "aloe", "barley", "clove", 
    "dulse", "eucalyptus", "fava", "ginseng", "honey", "indigo", "jicama", 
    "kohlrabi", "lavender", "matcha", "nutrient", "oregano", "parsley", 
    "quinoa", "rye", "sage", "thyme", "urad", "vanilla", "wheat", "xylitol", 
    "yogurt", "zest"]
#print(words[-3])

#list slicing
list = [3, 4, 7, 80, 34, 67,]
#print(list[1:4])
#print(list[1:-1])

#update a list

science = ["art", "chemistry", "guialogy"]

science[0] = "Bialogy"
#print(science)

intergers = [2, 3, 4, 5,]
intergers [-1] = 30.5
#print(intergers)
#intergers.remove(4)
#print(intergers)
#intergers.pop()
#print(intergers)
list_fruits=["lemon", "orange", "melon"]
#pop , remove, del
del list_fruits[1]
#print(list_fruits)
#list_fruits.append("MEGALOVANIA")
#print(list_fruits)
list_of_squares=[]
for int in range(1,10):
    square=int**2
    list_of_squares.append(square)

#print(list_of_squares)

#[expresion for list in list if condition]
square2=[int**2 for int in range(1,10)]

#print(square2)

#num=(1,2,3,4,5,6,7,8,9,10)
#for num in num:
    #print(num**3)
    
#pow(num,exp)

#cubic = [num**3 for num in num ]
list_of_number = (1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20)

even_number = [num*2 for num in list_of_number if num%2 == 0]
print(even_number)