import requests
import json

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/rt157")
t = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/sgg15")

print(r.text, t.text)

dict_p =  json.loads(r.text)
recipient = dict_p["Recipient"]
donor = dict_p["Donor"]

r_blood = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(recipient))

print(r_blood.text)

t_blood = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(donor))
print(t_blood.text)

if (r_blood.text==t_blood.text):
 match = "Yes"
else:
 match = "No"

out_data = {"Name": "rt157", "Match": "{}".format(match)}

r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(r.text)


