# Python3 code to demonstrate working of  
# Convert numeric words to numbers 
# Using join() + split() 

  

help_dict = { 

    'A': '$8', 

    'B': '$3', 

    'C': '$7', 

    'D': '$9', 

    'E': '$1', 

    'F': '$2', 

    'G': '$5', 

    'H': '$4', 

    'I': '$6', 

    'J' : '$A',

    'K': '$C', 

    'L': '&7', 

    'M': '&4', 

    'N': '&3', 

    'O': '&2', 

    'P': '&6', 

    'Q': '&8', 

    'R': '&5', 

    'S': '&1', 

    'T' : '&0',

    'U': '&J', 

    'V': '$L', 

    'W': '&B', 

    'X': '$D', 

    'Y': '$G', 

    'Z': '&F', 

} 

  
# initializing string 

test_str = input("Enter text to be encrypted: ")

  
# printing original string 

print("The original Text is : " + test_str) 

  
# Convert words to Code  
# Using join() + split() 

res = ''.join(help_dict[ele] for ele in test_str) 

  
# printing result  

print("The string after performing replace : " + res)  
 