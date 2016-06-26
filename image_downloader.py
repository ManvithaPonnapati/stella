import urllib
from urllib import urlopen
import json
new_dict={}
senti_dict={}
link_relation_dict={}
link_list=[]
senti_list=[]
final_list_pics=[]

search_key = 'cars'
api_key = "2817347-3ab03d21ef61f9d5e8b3db26a"
api_url = "https://pixabay.com/api/?key="+api_key+"&q="+search_key

#print api_url

json_data = urlopen(api_url).read()

result = json.loads(json_data)

#print result

link_numb = len(result['hits'])

for i in range(1,link_numb):
    #print result['hits'][i]['likes']
    link_list.append(result['hits'][i]['pageURL'])
    link_relation_dict[result['hits'][i]['pageURL']]=result['hits'][i]['webformatURL']
    new_dict[result['hits'][i]['pageURL']]=result['hits'][i]['likes']

link_list_sorted = sorted(link_list, key=new_dict.__getitem__, reverse=True)
#print link_list_sorted

for i in range(0,4):
    hpe_url = "https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?url="+link_list_sorted[i]+"&apikey=1284d3cc-29cf-4f7e-8f8c-2b8434befeeb"
    json_data1 = urlopen(hpe_url).read()
    result1 = json.loads(json_data1)
    senti_list.append(link_list_sorted[i])
    senti_dict[link_list_sorted[i]] = result1['aggregate']['score']
    #senti_dict[i]=result1['aggregate']['score']

#print senti_dict
senti_list_sorted = sorted(senti_list, key=senti_dict.__getitem__, reverse=True)

#print senti_list_sorted
#print link_relation_dict

for i in senti_list_sorted:
    final_list_pics.append(link_relation_dict.get(i))

for i in final_list_pics:
    print i

urllib.urlretrieve(final_list_pics[0],'1.jpg')