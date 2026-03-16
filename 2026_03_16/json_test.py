# JSON(Java Script Object Notation)
import json

with open("sample.json", mode="r") as f:
    data = json.loads(f.read())
    data['type'] = "drink"
    with open("sample.json", mode="w") as w:
        w.write(json.dumps(data))