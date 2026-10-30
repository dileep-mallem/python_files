# Four core Methods 

# json.dumps(obj) -> returns JSON text 
# json.loads(text) -> Parses text into Python Data 
# json.dump(obj,file) -> write JSON to a file - like obj 
# json.load(file) -> reads and parses one doc . 
# Trct : "s" means string 

import json 

data={"name":"Dileep","active":True}
text=json.dumps(data,indent=2)
restored=json.loads(text) # {'name': 'Dileep', 'active': True}

with open("data.json","w", encoding="utf-8") as f : 
    json.dump(data,f,ensure_ascii=False,indent=2)

with open("data.json",encoding="utf-8") as f : 
    loaded=json.load(f)

print(restored)
# indent=2 pretty-prints
# sort_keys=True sorts keys
# ensure_ascii=False writes Telugu, Hindi, and other Unicode directly;
# separators=(',', ':') makes compact JSON. 
#  Open files with encoding='utf-8' For read→modify→write, load, edit, then rewrite


#***  Appending another object to regular .json usually breaks it; for an array load/edit/rewrite, or use JSONL for append-only records.
# 1. Load: Read the entire JSON file into your computer's memory and parse it into an array.
# 2. Edit: Use your code to push/add the new object into that memory-based array.
# 3. Rewrite: Overwrite the old file entirely with the newly updated array.

d2= {"నమస్కారం": "హలో", "language": "తెలుగు"}
print(json.dumps(d2,ensure_ascii=False,indent=2))
# {
#   "నమస్కారం": "హలో",
#   "language": "తెలుగు"
# }

compact=json.dumps(d2,separators=(",",":"),ensure_ascii=False)
sorted_text=json.dumps(d2,sort_keys=True)

print(json.loads(compact),"\n",json.loads(sorted_text)) 
# {'నమస్కారం': 'హలో', 'language': 'తెలుగు'} 
# {'language': 'తెలుగు', 'నమస్కారం': 'హలో'}

# **Nested access and flattening**
# Use data['user']['profile']['name'] for guaranteed paths; use .get() for optional keys.
#  Loop over arrays of objects
#  Flatten nested paths into keys such as user.name; decide how arrays and key collisions should be handled.

