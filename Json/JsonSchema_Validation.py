# Schema purpose and usage 

# Valid JSON syntax does not guarantee required fields or correct values.
#  JSON Schema describes types and constraints
# Install `python -m pip install jsonschema`; use type, properties, required, minLength, minimum, maximum, enum.
# `jsonschema.validate(instance=payload, schema=schema)` raises ValidationError for invalid data and SchemaError for a malformed schema.

# python -m pip install jsonschema
from jsonschema import validate 

schema={
    "type":"object",
    "properties":{"name":{"type":"string","minLength":1},
                  "age":{"type":"integer","minimum":0}},
    "required":["name","age"]
}

validate(instance={"name":"Asha","age":20},schema=schema)

# This will fail because age is less than 0
# bad_data = {"name": "Asha", "age": -5}
# validate(instance=bad_data, schema=schema)
