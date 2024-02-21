import json

with open('sample-data.json', 'r') as f:
    data = json.load(f)

print("DN", "Status", "Description", "Speed", "MTU")
print("--", "------", "-----------", "-----", "---")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    dn = attributes["dn"]
    status = attributes["adminSt"]
    description = attributes["descr"] if attributes["descr"] else 'inherit'
    speed = attributes["speed"] if attributes['speed'] != 'inherit' else '9150'
    mtu = attributes["mtu"]
    
    print(dn, status, description, speed, mtu)
