
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