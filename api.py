# API Functies
import xmltodict
import requests

api_url = 'http://webservices.ns.nl/ns-api-avt?station=%s'
api_user = 'niek.visser@student.hu.nl'
api_pass = 'nagqEQlEI_xbnOtbilwoAyT_lCSNd5O0XnBywc4Gv2x0Y_O9QHuH8g'

headers = {'Authorization': 'Basic bmllay52aXNzZXJAc3R1ZGVudC5odS5ubDpuYWdxRVFsRUlfeGJuT3RiaWx3b0F5VF9sQ1NOZDVPMFhuQnl3YzRHdjJ4MFlfTzlRSHVIOGc='}
data = requests.get(api_url % 'Utrecht', headers=headers)


data_text = data.text
ez_access = xmltodict.parse(data_text)
# print(ez_access['ActueleVertrekTijden'])

for train in ez_access['ActueleVertrekTijden']:
    print("Trein van Utrecht Naar {} om {}".format(train['EindBestemming'], train['VertrekTijd']))