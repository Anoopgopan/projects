import requests
import json

def clean_data():
  r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
  return r.json()

data = clean_data()
print("input ::: ==> ",data)
delete_list = [None,'','-','N/A']

final={}
for k,v in data.items():
  if type(v) == list:
    for i in v:
      if i in delete_list:
        v.remove(i)
    final.update({k:v})
  elif type(v) == dict:
    a = {}
    for i,j in v.items():
      if j not in delete_list:
        a.update({i:j})
  # print(a)
    final.update({k:a})

  elif type(v) == int:
    if v in delete_list:
       continue
    final.update({k:v})  

  elif type(v) == str:
    if v in delete_list:
      continue
    final.update({k:v})
  else:
    continue

print("Output ::: ==> ",final)
# print(json.dumps(final,indent=2))

