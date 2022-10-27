 
f_txt = open('test.txt', 'r') # this brings our input file in, opens it and stores it to a variable
 
dicky = {} # this declares the empty dictionary
 
for txt in f_txt: # this is our for loop that iterates through our file and txt becomes the counter variable
   txt_items = txt.strip().split(',') # this splits the txt into elements by a comma and assigns it to a variable
 
   if txt_items[0] in dicky:  # this is writing to dictionary if key is already present
       dicky[txt_items[0]].append(txt_items[1]) # if the key in the dictionary, add this item
       dicky[txt_items[0]].append(txt_items[2]) # if the key in the dictionary, add this item
       dicky[txt_items[0]].append(txt_items[3]) # if the key in the dictionary, add this item
       dicky[txt_items[0]].append(txt_items[4]) # if the key in the dictionary, add this item
       dicky[txt_items[0]].append(txt_items[5]) # if the key in the dictionary, add this item
       dicky[txt_items[0]].append(txt_items[6]) # if the key in the dictionary, add this item
 
   else: # this writes to dictionary if key the is not already present
       dicky[txt_items[0]] = [txt_items[1], txt_items[2], txt_items[3], txt_items[4], txt_items[5], txt_items[6]]
       # this gives the items a place to go and an order to be in
 
f_txt.close() # this closes the input file
 
print("Original") # this displays Original in the console
for k, v in dicky.items(): # this is our for loop that iterates through the dictionary items and grabs the key and
# value
  print("{}: {}".format(k, v)) # this is a display that has our key and value passed in
print("")# this creates a space in the display between the original and the inverse
 
def invert_dict(d): # our function for inverting the dictionary with a parameter passed in
   inverse = dict() # this establishes the variable inverse as an empty dictionary
   for key in d: # this is our for loop for reading each value in values of that specific key
       val = d[key] # this takes our value in the key and assigns it to a variable
       for element in val: # this is our for loop that iterates through the value variable and element becomes the
       # counter
           if element not in inverse: # our if condition that says if the counter element isn't in inverse, do this
               inverse[element] = [key] # this writes to inverted dictionary if the key(element) is not present
           else: # if the above isn't satisfied, do this
               inverse[element].append(key)  # this appends the element to inverted dictionary if key is present
   return inverse # this returns our product for inverse
 
inverted_dicky = invert_dict(dicky) # in a variable, this calls the function and passes in an argument
 
print("Inverted") # this displays the word inverted to show the inverted dictionary in the console
 
for k, v in inverted_dicky.items(): # our for loop that iterates through the items in inverted_dicky variable
   print("{}: {}".format(k, v)) # this displays out key and value in our console
 
f2 = open('my_inverted_dicky.txt', 'w') # this opens the my_inverted_dict.txt file in write mode
 
for i in inverted_dicky: # this writes one txt at a time in the inverted dicky and i becomes the counter
   txt = i + ',' + ','.join(inverted_dicky[i]) # this takes our index and adds in space and the value/key
   f2.write(txt) # this tells it to write the variable tx and whatever is in it
   f2.write('\n') # this tells it to write to a new line each time
 
f2.close() # when the for loop is done, close the file
 
# outputs
 
# this it our original output from the file test.txt
# Original
# Number: [' One', ' Two', ' three', ' four', ' Five', ' SIX']
# Name: [' Blake', ' Jen', ' Hank', ' Hazel', ' Carl', ' Jessica']
 
# this is our inverted dictionary, the key is now the value and the value is the key
# Inverted
#  One: ['Number']
#  Two: ['Number']
#  three: ['Number']
#  four: ['Number']
#  Five: ['Number']
#  SIX: ['Number']
#  Blake: ['Name']
#  Jen: ['Name']
#  Hank: ['Name']
#  Hazel: ['Name']
#  Carl: ['Name']
#  Jessica: ['Name']
 
 
# ...Program finished with exit code 0 # this says program ran smooth
 
 
# references:
 
# Python File I/O: Read and Write Files in Python. (n.d.). Retrieved October 26, 2022, from https://www.programiz.com/python-programming/file-operation
# GDB online Debugger | Compiler - Code, Compile, Run, Debug online C, C++. (n.d.). GDB Online Debugger. Retrieved October 26, 2022, from https://www.onlinegdb.com/
