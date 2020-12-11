from riotwatcher import LolWatcher, ApiError
import json

api_key = '' #input your token here
watcher = LolWatcher(api_key)

#Getting the user Server
print('Type in your server: ')
region = input()

#Getting the user Name
print('Input your name: ')
name = input()

user = watcher.summoner.by_name(region, name)
userRank = watcher.league.by_summoner(region, user['id'])
matches = watcher.match.matchlist_by_account(region, user['accountId'])
lastMatch = matches['matches'][0]
matchDetail = watcher.match.by_id(region, last_match['gameId'])

#Printing Data
print('user ->:'+user)
print(userRank)
print(matches)
print(lastMatch)
print(matchDetail)