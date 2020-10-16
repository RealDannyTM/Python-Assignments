
"""Python is Easy - Assignment #03 - If Statements
Health Checking System
By: Abdul Wasey""" 

# Global Vairables

Health = 0
CheckHealth = True
Death = False
Message = "Your health is in stable condition."

# Stataments

if Health < 50 and CheckHealth == True:
    Message = "Your health is below 50, please heal up."

elif Health > 50 and CheckHealth == True:  
    Message = "Your health is in stable condition."

else:
    Message = "You need to check your health."    

if Health == 0:
    Death = True
    Message = "You died."    


# Outputs

print (Message)    


