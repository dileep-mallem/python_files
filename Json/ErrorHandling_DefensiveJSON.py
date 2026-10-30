import json 

def parse_object(text) : 
    try : 
        value=json.loads(text)
    except json.JSONDecodeError as exc : 
        return {"ok":False,"error":f"line {exc.lineno}, col{exc.colno} : {exc.msg}"}
    if not isinstance(value,dict) : 
        return {"ok":False,"error":"Expected a JSON Object"}
    return {"ok":True,"data":value}
data={"name":"Dileep","active":True}
text=json.dumps(data,indent=2) 
print(parse_object(text=text)) # {'ok': True, 'data': {'name': 'Dileep', 'active': True}}

# Simulating data that was appended raw to a text file
t2 = """{
    "username": "alice",
    "status": "online"
}
{
    "username": "bob",
    "status": "offline"
}"""
print(parse_object(text=t2)) # {'ok': False, 'error': 'line 5, col1 : Extra data'}


# 2.Trailing Comma Error 
broken_comma_data = """{
    "title": "Data Log",
    "version": 2.0,
    "tags": ["system", "alerts",],
}"""

print(parse_object(text=broken_comma_data)) # {'ok': False, 'error': 'line 4, col32 : Illegal trailing comma before end ofarray'}

# Single quotes around 'id', 'undefined', and code comments break JSON
broken_syntax_data = """{
    'id': 101,
    "message": "Connection timed out",
    "timestamp": undefined
}"""
print(parse_object(text=broken_syntax_data)) # {'ok': False, 'error': 'line 2, col5 : Expecting property name enclosed in double quotes'}