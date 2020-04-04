s = [{"sn": "123", "station": "pcbdl", "status": "P"}, {"sn": "123", "station": "pcbdl", "status": "S"},
     {"sn": "123", "station": "PCBPM", "status": "P"}, {"sn": "123", "station": "PCBPM", "status": "S"},
     {"sn": "123", "station": "pcbdl", "status": "P"}, {"sn": "123", "station": "pcbdl", "status": "S"}]
are = {}
for i in s:
    if i["status"] == "P":
        are = i
        break
print(s[0].get("status"))
print(len(s))
print("lastitem is {}".format(are["station"]))
if are["station"]=="PCBST" or are["station"]=="PCBPM3":
    print("")
