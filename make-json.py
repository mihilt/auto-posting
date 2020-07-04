import json
from collections import OrderedDict

file_data = OrderedDict()

file_data["id"] = "asd"
file_data["pw"] = "sdf"
print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open('account.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")