import requests
import time
#########config#######
YOUR_SSPanel_address = "Please replace it"
YOUR_SSPanel_muKey = "Please replace it"
node_id_start = 3
node_id_end = 5
# default refreash every 90 sec
waiting_time = 90 
########END config####
url = "https://{0}/mod_mu/users?key={1}&node_id=".format(YOUR_SSPanel_address, YOUR_SSPanel_muKey)

while True:
        for node_id in range(node_id_start, node_id_end):
                try:
                        requests.get(url + str(node_id))
                except:
                        pass
        time.sleep(waiting_time)
