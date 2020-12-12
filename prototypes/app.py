import requests
 
address = input("please enter request according to instruction: ") 

r = requests.get(address)

print(r.json())

#writing json to the file

with open('response.txt', 'w') as f:
   f.write(r.text)
