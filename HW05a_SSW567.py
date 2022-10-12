from unicodedata import name
import requests
import json


def github_api_commit():
    username = input("your Github user ID: ")

    url = "https://api.github.com/users/{}/repos".format(username)

    response = requests.get(url)  # this is for get data from API
    data = json.loads(response.text)  # convert data in JSON file

    l = []
    m = []
    o = []
    temp = []
    for i in data:  # this is to convert JSON file into dictionary
        for k in i.values():  # this is for getting values from dictionary
            m.append(k)

        for j in i.keys():  # this is for getting keys from dictionary
            l.append(j)

    for t in range(len(l)):  # if key is 'name' than it will store value in list
        if l[t] == 'name':
            temp.append(m[t])

    for temp2 in range(0, len(l)):  # this is to print every repository

        repos = temp[temp2]
        url2 = "https://api.github.com/repos/{}/{}/commits".format(username, repos)
        count = 0
        response2 = requests.get(url2)
        data2 = json.loads(response2.text)

        for n in data2:  # this is for getting keys from dictionary
            for a in n.keys():
                o.append(a)

        for b in range(len(o)):  # if key is 'committer' than it will increase count
            if o[b] == 'committer':
                count += 1
        print("Repos:", repos, " And Your Commiter is: ", count)
    return True

print(github_api_commit())

