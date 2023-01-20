
def getSortedNumberasc(n):
    # Function for sorting some number in Ascending order
  
    # Convert to equivalent string
    number = str(n)
  
    # Sort the string
    number = ''.join(sorted(number))
  
    # Convert to equivalent integer
    number = int(number)
  
    # Return the integer
    return number

def getSortedNumberdesc(n):
    # Function for sorting some number in Descending order
  
    # Convert to equivalent string
    number = str(n)
  
    # Sort the string
    number = ''.join(sorted(number, reverse=True))
  
    # Convert to equivalent integer
    number = int(number)
  
    # Return the integer
    return number
  
# Two challenges with this program.
''' 1. If the number goes below 999 then we need to add a 0 to the end of the number. 
Similarly if goes below 100 then include two zeros and if it goes below 10 then include 3 zeros.

    2. If you start with the number 0001 then the code breaks and actually it gets stuck in a continous loop. 
    This is due to python's interpretation of zeros'''

print("Kaprekar's constant - 6174.")
print("This program takes a number and arrange it in desending order and then assending order.\n And subtracts both from each other and will do so until you get the Kaprekar's constant.")
value = (input("Please enter a 4 digit number: "))
count = 0
sub_value = 0
new_value_asc = getSortedNumberasc(value)
new_value_desc = getSortedNumberdesc(value)
sub_value = new_value_desc - new_value_asc
if sub_value < 1000 and sub_value > 99:
    sub_value = sub_value * 10
elif sub_value < 100 and sub_value > 9:
    sub_value = sub_value * 100
elif sub_value < 10 and sub_value > 0:
    sub_value = sub_value * 1000
while sub_value != 6174:

    count += 1
    new_value_asc = getSortedNumberasc(sub_value)
    new_value_desc = getSortedNumberdesc(sub_value)
    sub_value = new_value_desc - new_value_asc

print(f"It took {count} times to get the Kaprekar's constant for your number.")


