"""Python is Easy - Assignment #04 - Lists
Addition and Rejection of Items""" 

#Global Variables

myUniqueList = []
myLeftovers = []

def Addition(Item):
    if Item in myUniqueList:
        RejectedItems(Item)
        return False
    else:
        myUniqueList.append(Item)
        return True

def RejectedItems(Item):
  myLeftovers.append(Item)


#Output

print(myUniqueList) 

print(Addition("Watch")) 

print(myUniqueList) 

print(myLeftovers) 

# Checking the uniqueness of the element added before. 

print(Addition("Watch"))

print(myUniqueList) 

print(myLeftovers) 

