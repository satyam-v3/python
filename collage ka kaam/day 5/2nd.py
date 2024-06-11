# WAP to count the number of characters in a string.

string="lolo popo 🫠"
print(" The OG is : "+ str(string))
lol = len([ele for ele in string if ele.isalpha()])
print(" Count of alphabets :"+ str(lol))