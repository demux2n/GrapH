#!/usr/bin/python3 

import sys
import argparse
import requests
import networkx as nx
import matplotlib.pyplot as plt

from helper import *

g = nx.DiGraph()

def main() : 
 
   global g 

   parser = argparse.ArgumentParser()
   parser.add_argument("-s", "--start", help="Account to start graph at.", dest='user')
   parser.add_argument("-d", "--depth", help="Depth to recurse.", type=int, dest='depth')
   parser.add_argument("--following", help="Include following.", action='store_true')
   parser.add_argument("--followers", help="Include followers.", action='store_true')
   parser.add_argument("--repos", help="Include repositories.", action='store_true')
   args = parser.parse_args()

   args.depth -= 1
   recurse(args.user, args.depth, args.following, args.followers, args.repos)

   nx.draw_circular(g, with_labels=True)

   plt.axis('off')
   plt.show() # display
   #print(g.degree)

def recurse (cuser, cdepth, bfollowing, bfollowers, brepos) : 

   global g
   following = []
   followers = []
   repos     = []

   if bfollowers : 
      followers = userFollowers(cuser)
      for i in followers : 
         g.add_edge(i, cuser)

   if bfollowing : 
      following = userFollowing(cuser)
      for i in following : 
         g.add_edge(cuser, i)

   if brepos : 
      repos = userRepos(cuser) 

   all = following + followers

   if cdepth > 0 : 
      for i in all : 
         recurse(i, cdepth-1, bfollowing, bfollowers, brepos)

if __name__ == "__main__" : 
   main()
