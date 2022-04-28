import uuid
from asyncio.windows_events import NULL
from unicodedata import name
import json

class Cell:
  def __init__(self, name, age):
    self.type = name
    self.content = age


# def getMetadata():
#     metadata={}
#     metadata['kernelspec']={}
   # metadata['kernelspec']['display_name'] = 'Python 3 (ipykernel)'
    #metadata['kernelspec']['language'] = 'python'
    #metadata['kernelspec']['name'] = 'python3'


    

def getDefaultBody():
    body={}
    body['metadata']={}#' "kernelspec": {    "display_name": "Python 3 (ipykernel)",    "language": "python",    "name": "python3"   },   "language_info": {    "codemirror_mode": {     "name": "ipython",     "version": 3    },    "file_extension": ".py",    "mimetype": "text/x-python",    "name": "python",    "nbconvert_exporter": "python",    "pygments_lexer": "ipython3",    "version": "3.7.9"   }'
    body['cells'] = []
    body['nbformat'] = 4
    body['nbformat_minor'] = 5
    return body

def getCell(cellObject,ifAddKql):
    cell={}
    cell['cell_type']=cellObject.type
    if(cellObject.type=='code'):
        cell['execution_count']=NULL
        if ifAddKql:
            cell['source']=[str('%%kql\n'+cellObject.content)]
        else:
            cell['source']=[str(cellObject.content)]
    else :
        cell['source']=[str(cellObject.content)]
    cell['metadata']={}
    cell['outputs']=[]
    cell['id']=str(uuid.uuid4())
    return cell





def getIpynb(ls):
    body=getDefaultBody()
    body['cells'].append(getCell(Cell('code','!pip install Kqlmagic --no-cache-dir  --upgrade'),False))
    body['cells'].append(getCell(Cell('code','%reload_ext Kqlmagic'),False))
    body['cells'].append(getCell(Cell('code','%kql AzureDataExplorer://tenant="Microsoft.com";code;cluster=\'https://azdhnorthamcentral.kusto.windows.net\';database=\'SLICE\''),False))
    
    for x in ls:
        body['cells'].append(getCell(x,True))
    jsonObject=json.dumps(body)
    return (jsonObject)

