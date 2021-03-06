# API Functies
import xmltodict
import requests
from datetime import datetime

api_url = 'http://webservices.ns.nl/ns-api-avt?station=%s'

headers = {
    'Authorization': 'Basic bmllay52aXNzZXJAc3R1ZGVudC5odS5ubDpuYWdxRVFsRUlfeGJuT3RiaWx3b0F5VF9sQ1NOZDVPMFhuQnl3YzRHdjJ4MFlfTzlRSHVIOGc='
}


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
    limit = 15
    i = 0
    for train in ez_access['ActueleVertrekTijden']['VertrekkendeTrein']:
        dateobject = datetime.strptime(train['VertrekTijd'], '%Y-%m-%dT%H:%M:%S%z')
        minute = dateobject.minute if dateobject.minute > 9 else '0{}'.format(dateobject.minute)
        spoor = 'van spoor {}'.format(str(train['VertrekSpoor']['#text'])) if '#text' in train['VertrekSpoor'] else ''
        vertraging = " ({}) ".format(train['VertrekVertragingTekst']) if 'VertrekVertragingTekst' in train else ' '
        tekst += "%s:%s%s- %s naar %s %s\n" % (
            dateobject.hour,
            minute,
            vertraging,
            train['TreinSoort'],
            train['EindBestemming'],
            spoor
        )
        i += 1
        if i == limit:
            break
    return tekst
