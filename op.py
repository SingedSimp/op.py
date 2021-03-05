import requests, bs4, re
defname = "Sínged Gamíng"
username = input("What is your LoL username?\n")
username = username.replace(' ', '+')
res = requests.get('https://na.op.gg/summoner/userName=' + username)
res.raise_for_status()
summoner = bs4.BeautifulSoup(res.text, 'html.parser')
name = summoner.find('span', {'class': 'Name'})
level = summoner.find('span', {'class': 'Level tip'})
rank = summoner.find('div', {'class': 'TierRank'})
winrate = summoner.find('span', {'class': 'winratio'})
lp = summoner.find('span', {'class': 'LeaguePoints'})
mains = summoner.find_all('div', {'class': 'Face'})
mains.pop(0)
while True:
    try:
        mains.pop(7)
    except:
        break
# Prints summoner name and level
print(name.text + ', level ' + level.text)
# Uses a try and except so if someone is unranked it will not throw and error
try:
    print(rank.text + ', ' + lp.text.strip(), '\n', winrate.text)
except:
    print('Unranked')
# Gets the champion name for all of their most played champions
print("Main champions:")
for main in mains:
    print(' ' + main.get('title'))
winnum = int(re.search(r'\d+',winrate.text).group())
if winnum < 40:
    print("Dodge: Yes")
elif winnum < 49:
    print("Dodge: Maybe")
elif winnum > 49:
    print("Dodge: No")
