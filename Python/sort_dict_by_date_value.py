from collections import OrderedDict
from datetime import datetime

#Input
dict1 = {'P1':'03/09/2020','P4':'06/01/2020','P2':'01/09/2019','P5':'02/09/2020','P3':'28/08/2020'}

#Expected Output is to sort the dates in descending order and return the keys in a list
#['P1', 'P5', 'P3', 'P4', 'P2']

#By default the sorted method of python uses the format of %Y-%m-%d , so first we will convert any given format to our
#required format and use the sorted method

for key , value in dict1.items():
    value = datetime.strptime(dict1.get(key), "%d/%m/%Y").strftime('%Y-%m-%d')
    dict1[key] = value
# lastconnection = datetime.strptime("21/12/2008", "%d/
#
li = []
ordered1 = OrderedDict(sorted(dict1.items(), key=lambda t: t[1],reverse=True))
print(ordered1.keys())