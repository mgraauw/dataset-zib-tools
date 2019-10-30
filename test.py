from urllib.request import urlopen
from urllib.parse import quote
import json

baseUrl = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/v2'
edition = 'MAIN'
version = '2019-07-31'

#Prints fsn of a concept
def getConceptById(id):
    url = baseUrl + '/browser/' + edition + '/' + version + '/concepts/' + id
    response = urlopen(url).read()
    data = json.loads(response.decode('utf-8'))

    print (data['fsn']['term'])

getConceptById('109152007')