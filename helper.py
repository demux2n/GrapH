#!/usr/bin/python3 

import requests
from private import token as apikey
# token='YOURAPIKEY'

url  = 'https://api.github.com/users/'
head = {'Authorization': 'token {}'.format(apikey)}

#response = requests.get(url + '/users/tomsom', headers=head)

def userFollowing (uname) :
   fr = []
   r = requests.get(url + uname + "/following", headers=head)
   fd = r.json()
   for i in fd :
      fr.append(i["login"])
   return(fr)

def userFollowers (uname) :
   fr = []
   r = requests.get(url + uname + "/followers", headers=head)
   fd = r.json()
   for i in fd :
      fr.append(i["login"])
   return(fr)

def userRepos (uname) :  
   fr = []
   r = requests.get(url + uname + "/repos", headers=head)
   fd = r.json()
   for i in fd : 
      fr.append(i["name"])
   return(fr)
