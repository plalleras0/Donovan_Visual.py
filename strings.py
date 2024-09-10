firstName= input("first name:")
lastName= input("last name:")
count= len(firstName + lastName)
initials= lastName[0] + firstName[0]

double_fname = ""
for letter in firstName:
    double_fname += letter + letter
    
revered_name = lastName[::-1]

print (f"Hello {firstName} , {lastName} ! Your name has {count} letters, and your initials are {initials}. {double_fname} , your name spelled backwards is {revered_name}.")