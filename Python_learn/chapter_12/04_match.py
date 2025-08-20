# Similar to the switch case in the python
def switch(status): 
       match status: 
             case 200: 
                  return "OK" 
             case 404: 
                 return "Not Found" 
             case 500:                  return "Internal Server Error" 
             case _: 
                 return "Unknown status" 
# Usage 
print(switch(200))  # Output: OK 
print(switch(404))  # Output: Not Found 
print(switch(500))  # Output: Internal Server Error 
print(switch(403))  # Output: Unknown status 