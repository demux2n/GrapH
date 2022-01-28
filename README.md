## GrapH

A simple way to view relationships on GitHub. Not at all an original idea.

# Installation

pip install -r requirements.txt

You may also need to install your distribution's python3-tk:
* sudo apt install python3-tk

# Usage

Create a digraph of relationships
* -s Account to start graph at
* -d Depth to travel (ie degrees of separation)
*  --following Include following relationships
*  --followers Include follower relationships

GrapH.py -d 2 -s demux2n --following
