 
# Unit 8 Discussion Forum
 
# Part 1

# You can set up alerts that let you know exceptions have happened and you can go fix the code. For instance,
# if you made the code print an f string: You could tell yourself exactly what went through and you can figure out
# how to better limit those things from going upstream and creating a file error. This can take a lot of the guess-
# work out of figuring out what creates a file error. If the request is a boolean value and you are returning an
# integer, that may go through, but it will never give you the result you want and may create an error. The simple
# ability to identify the bug by looking at the console would be nice.

chart = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Ten",  11, 12, 13] # this is the list we are working from
 
def exceptions_handler(num_list): # this is our function that takes a parameter
  for  num in num_list: # this is the for loop that iterates through the passed in parameter
      type(num) == int # this says when the value of "num" is an integer
      try: # try this code block
          multi_num = num ** 2 # this takes the "num" variable and squares it, then stores that value to a variable
          result = num * multi_num # this takes our original variable of "num" and multiplies it with our local
          # variable to give us a new value that is stored to a variable named "result"
          print(f"{num} X {multi_num} = {result}") # this is our display feature that shows what is happening
      except: # this says when the try condition not satisfied, run this code block
          print(f"number: ({num}) is not an integer") # this is our display statement that says there has been an
          # exception, what the exception is and what we were expecting, thus making debugging a snap   
        
exceptions_handler(chart) # this is our function call that passes in our argument list

# outputs for part 1

# 1 X 1 = 1 # the "try" worked and it runs that code block
# 2 X 4 = 8 # the "try" worked and it runs that code block
# 3 X 9 = 27 # the "try" worked and it runs that code block
# 4 X 16 = 64 # the "try" worked and it runs that code block
# 5 X 25 = 125 # the "try" worked and it runs that code block
# 6 X 36 = 216 # the "try" worked and it runs that code block
# 7 X 49 = 343 # the "try" worked and it runs that code block
# 8 X 64 = 512 # the "try" worked and it runs that code block
# 9 X 81 = 729 # the "try" worked and it runs that code block
# number: (Ten) is not an integer # an exception was made, the exception is in (parenthesis)
# 11 X 121 = 1331 # the "try" worked and it runs that code block
# 12 X 144 = 1728 # the "try" worked and it runs that code block
# 13 X 169 = 2197 # the "try" worked and it runs that code block

# Part 2

# To begin debugging on a large scale production I would start with opening my console. Once I see what error I am
# getting back, I can figure it out more quickly. If the console isn't giving me anything useful, I like to go through
# and comment out things until I can get the project to run, then one by one, remove the comment hashtag and see if
# it breaks. Once I have the problem isolated, I can then start to figure out why it isn't working. If none of that
# works, I walk away for a minute to regroup and see if I come up with a new idea. If I had a supervisor, this
# would be a great time to show them the isolated problem and get their thoughts, or throw it out on Stackoverflow.
 
# Reference:
# Downey. (2015). Think Python: How to Think Like a Computer Scientist. Greenteapress.com. https://greenteapress.com/thinkpython2/thinkpython2.pdf
# Python Try Except. (1999). W3 Schools. https://www.w3schools.com/python/python_try_except.asp
# Built-in Exceptions — Python 3.10.8 documentation. (n.d.). Retrieved October 21, 2022, from https://docs.python.org/3/library/exceptions.html
