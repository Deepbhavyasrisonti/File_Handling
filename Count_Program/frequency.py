# Program, that accepts file name as an input fromm the user , and open the file and count the number of times a character appear
filename=input("enter the file name:")
with open(filename)as file:
    text=file.read()
    letter=input("Enter a character:")
    c=0
    for char in text:
        if char ==letter:
            c+=1
print(letter,"appears",c,"times in the file")