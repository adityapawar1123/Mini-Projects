#For a more dynamic code 
a = input("Enter a sentence: ")
if a.find(" ") != -1 : print("Single space at index", a.find(" "))
else : print("No single spaces found.")

#You can change this space detector to any word, sentence too. Just change the value in a.find("")