import requests
from bs4 import BeautifulSoup



param = 'shrutigupta5555'

def getavatar(param):
    
    url = "https://devpost.com/" + param
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")

    avatarurl = soup.find('img', attrs = {"class": "user-photo"})
    # print(avatarurl)
    return avatarurl['src']

def getdisplayname(param):

    url = "https://devpost.com/" + param
    # print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")

    name = soup.find('h1', attrs = {"id": "portfolio-user-name"}).getText().split("\n")[1].lstrip()
    return name

def getTotalProjects(param):

    url = "https://devpost.com/" + param
    n = getdisplayname(param)
    # print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    pagecountul = soup.find('ul', attrs = {'class': 'pagination'})
    if pagecountul:
        pages = len(pagecountul.find_all('li')) - 2

    else:
        pages = 1
        
    memberCount = {}
    memberLink = {}
    projectlist = []

    for i in range(pages):
        x = i + 1
        url = "https://devpost.com/" + param + "?page=" + str(x)
        # print(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text)
        try:
            projectsDiv =  soup.find_all('div', attrs = {"class": "gallery-item"})
        except:
            projectsDiv=[]
        for projects in projectsDiv:
            p = {}
            projecturl = projects.find('img', attrs = {"class": "software_thumbnail_image"})['src']
            projecttitleDiv =  projects.find('div', attrs = {"class": "software-entry-name"})  

            projecttitle = projecttitleDiv.find('h5').getText().strip()
            like = projects.find('span', attrs = {'class': 'like-count'}).getText().strip()
            teamDiv = projects.find('div', attrs = {'class': 'members'})
            tt = teamDiv.find_all('span')
            p['projecturl'] = projecturl
            p['like'] = like
            p['projecttitle'] = projecttitle
            teamlist = []
            for team in tt:
                
                name = team.find('img')['alt']
                turl = team['data-url']
                id = turl.split("/")[-1]
                if name != n:
                    teamlist.append(name)
                    if id in memberCount:
                        memberCount[id] += 1
                    else:
                        memberCount[id] = 1

                    if id not in memberLink:
                        memberLink[id] = name
            p['team'] = teamlist
            projectlist.append(p)
    # print(projectlist)     
    return projectlist, memberCount, memberLink      
                
    
def getfriendslocation(param):
    projectlist, memberCount, memberLink  = getTotalProjects(param)
    loc = {}
    avatar={}
    count = 0
    for key in memberLink.keys():
        count+=1
        if count>24:
            break
        new_url = "https://devpost.com/" + key
        
        res = requests.get(new_url)
        soup = BeautifulSoup(res.text, features="html.parser")

        cl = soup.find('ul', attrs = {'id': 'portfolio-user-links'})
        try:
            location = cl.find('li')
        except:
            location = False
        flag = soup.find('span', attrs = {'class':'ss-location'})
        if location and flag:
            
            
            curr = location.getText().strip()
            soup = BeautifulSoup(res.text, features="html.parser")
            avatarurl = soup.find('img', attrs = {"class": "user-photo"})
            lmao = avatarurl['src']
            # print(f"")
            print(f"avatar dictionalry: {lmao}")
        else:
            curr = ""
        loc[key] = curr
        avatar[key] = lmao
        
    return loc, avatar


def getfollowers(param):
    url = "https://devpost.com/" + param
    res = requests.get(url)
    soup = BeautifulSoup(res.text)

    try:
        followers = soup.find('li', attrs = {"data-followers-tab": "true"}).getText().strip().split(" ")[0]
    except:
        followers = 0
    # print(followers)
    return followers


# getfollowers("aakzsh")

def winnerandparticipated(param):
    url = "https://devpost.com/"+param+"/achievements"
    # print(url)

    res = requests.get(url)
    soup = BeautifulSoup(res.text)

    try:
        participatedDiv =  soup.find('div', attrs = {'id': 'achievement_3'})
        participated = participatedDiv.find('h5').getText().strip().split(" ")[-1]
    except:
        participated = 0

    try:
        winnerDiv = soup.find('div', attrs = {'id': 'achievement_5'})
        winner = winnerDiv.find('h5').getText().strip().split(" ")[-1]
    except:
        winner = 0
    
    return winner, participated
# getavatar(param)
# print(getfriendslocation(param))