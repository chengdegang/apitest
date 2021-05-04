import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url)
print(f"Status code: {r.status_code}")
#该方法将返回结果存储到字典中
response_dic = r.json()
print(f"Total repositories: {response_dic['total_count']}")
#打印该url返回有多少key
print(response_dic.keys())

rep_dics = response_dic['items']
print(f"Repositories retrurned: {len(rep_dics)}")

# rep_dic = rep_dics[0]
#查看第一个仓库里有多少key并打印
# print(f"\nKeys: {len(rep_dic)}")
# for key in sorted(rep_dic.keys()):
#     print(key)
# print("\nSlect information about first repository: ")
# print(f"name :{rep_dic['name']}")
# print(f"owner :{rep_dic['owner']['login']}")
# print(f"stars :{rep_dic['stargazers_count']}")
# print(f"repository :{rep_dic['html_url']}")
# print(f"creat :{rep_dic['created_at']}")
# print(f"update :{rep_dic['updated_at']}")
# print(f"description :{rep_dic['description']}")

print("\nSlect information about each repository: ")
for rep_dic in rep_dics:
    print(f"name :{rep_dic['name']}")
    print(f"owner :{rep_dic['owner']['login']}")
    print(f"stars :{rep_dic['stargazers_count']}")
    print(f"repository :{rep_dic['html_url']}")
    print(f"creat :{rep_dic['created_at']}")
    print(f"update :{rep_dic['updated_at']}")
    print(f"description :{rep_dic['description']}\n")


