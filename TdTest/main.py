import datetime
import gameTypes

pathWaypoints=[(0,100), (100,100), (100,200), (200,200)]
nmes=[gameTypes.Nme(100, [], pathWaypoints)]
towers=[]
wave=0

def MoveEnemies(now):
    for nme in nmes:     
        nme.Move(now, wave)

def ExecuteTowers(now):
    for tower in towers:
        tower.Execute(now)

isRunning=True
while (isRunning):
    now = datetime.datetime.now()
    MoveEnemies(now)
    ExecuteTowers(now)
    #TODO: determine when wave ends; maybe when all nmes with that spawnWave have spawned?  then when to start a new wave




