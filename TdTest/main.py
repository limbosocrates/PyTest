import datetime
import types

global pathWaypoints
pathWaypoints=[(0,100), (100,100), (100,200), (200,200)]
nmes=[types.Nme(100, [], pathWaypoints)]
towers=[]

def MoveNmes(now):
    for nme in nmes:     
        nme.Move(now)

def ExecuteTowers(now):
    for tower in towers:
        tower.Execute(now)

isRunning=True
while (isRunning):
    now = datetime.datetime.now()
    MoveNmes(now)





