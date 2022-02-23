import requests

out_data = {"user": "Sanika+Kayana", "message": "Amazing!!"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)

print(r.status_code)

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/ria")

print(r.text)

