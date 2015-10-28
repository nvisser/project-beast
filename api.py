# API Functies
# TODO: Error catching
import xmltodict
import requests
from datetime import datetime

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
    ez_access = xmltodict.parse(data_text)
    if 'error' in ez_access:
        return ez_access['error']['message']
    tekst = ''
    limit = 10
    i = 0
    for train in ez_access['ActueleVertrekTijden']['VertrekkendeTrein']:
        dateobject = datetime.strptime(train['VertrekTijd'], '%Y-%m-%dT%H:%M:%S%z')
        try:
            tekst += "%s:%s - %s naar %s van spoor %s\n" % (
                dateobject.hour,
                dateobject.minute,
                train['TreinSoort'],
                train['EindBestemming'],
                str(train['VertrekSpoor']['#text'])
            )
        except:
            tekst += "%s:%s - %s naar %s\n" % (
                dateobject.hour,
                dateobject.minute,
                train['TreinSoort'],
                train['EindBestemming']
            )
        i += 1
        if i == limit:
            break
    return tekst
