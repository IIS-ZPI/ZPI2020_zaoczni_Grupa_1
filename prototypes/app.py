import requests
 
def getRequest():
   return input("please enter request according to instruction: ") 

def parseResponse(address):
   return requests.get(address)

def showResponse(response):
   print(response.json())

def saveResponse(response):
   with open('response.txt', 'w') as f:
      f.write(response)

if __name__ == "__main__":
   response = parseResponse(getRequest())
   showResponse(response)
   saveResponse(response)