# API Functies
import xmltodict
import requests

api_url = 'http://webservices.ns.nl/ns-api-avt?station=%s'
api_user = 'niek.visser@student.hu.nl'
api_pass = 'nagqEQlEI_xbnOtbilwoAyT_lCSNd5O0XnBywc4Gv2x0Y_O9QHuH8g'

headers = {
    'Authorization': 'Basic bmllay52aXNzZXJAc3R1ZGVudC5odS5ubDpuYWdxRVFsRUlfeGJuT3RiaWx3b0F5VF9sQ1NOZDVPMFhuQnl3YzRHdjJ4MFlfTzlRSHVIOGc='}


def verkrijg_utrecht():
    """
    Verkrijg de vertrektijden van Utrecht
    :return:
    """
    return zoek('Utrecht')


def zoek(waar):
    """
    Zoek naar actuele vertrektijden
    :param waar:
    :return:
    """
    data = requests.get(api_url % waar, headers=headers)

    data_text = data.text
    ez_access = xmltodict.parse(data_text)
    if 'error' in ez_access:
        print(ez_access['error']['message'])
        exit(1)
    for train in ez_access['ActueleVertrekTijden']['VertrekkendeTrein']:
        print("Trein {} van {} naar {} vertrekt om {}".format(
            train['RitNummer'],
            waar,
            train['EindBestemming'],
            train['VertrekTijd']
        ))
