# API Functies
# TODO: Error catching
import xmltodict
import requests

api_url = 'http://webservices.ns.nl/ns-api-avt?station=%s'

headers = {
    'Authorization': 'Basic bmllay52aXNzZXJAc3R1ZGVudC5odS5ubDpuYWdxRVFsRUlfeGJuT3RiaWx3b0F5VF9sQ1NOZDVPMFhuQnl3YzRHdjJ4MFlfTzlRSHVIOGc='
}


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
    try:
        data = requests.get(api_url % waar, headers=headers)
    except:
        return 'Geen resultaten'

    if data.status_code != 200:
        return 'Geen resultaten'

    data_text = data.text
    print(data)
    ez_access = xmltodict.parse(data_text)
    if 'error' in ez_access:
        return ez_access['error']['message']
    tekst = ''
    for train in ez_access['ActueleVertrekTijden']['VertrekkendeTrein']:
        tekst = tekst + "Trein {} van {} naar {} vertrekt om {}\n".format(
            train['RitNummer'],
            waar,
            train['EindBestemming'],
            train['VertrekTijd']
        )
    return tekst
