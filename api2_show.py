import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url)
print(f"Status code: {r.status_code}")
#该方法将返回结果存储到字典中
response_dic = r.json()

rep_dics = response_dic['items']
rep_name,star = [],[]

for rep_dic in rep_dics:
    rep_name.append(rep_dic['name'])
    star.append(rep_dic['stargazers_count'])

data = [{
    'type':'bar',
    'x':rep_name,
    'y':star,
}]
my_layout = {
    'title':'github famous repositories',
    'xaxis':{'title':'Repository'},
    'yaxis':{'title':'stars'},
}

fig = {'date':data,'layout':my_layout}
offline.plot(fig, filename ='python_git_ana.html')




