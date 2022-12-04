import datetime
import logging
import gameTypes

logging.basicConfig(level=logging.DEBUG)

pathWaypoints=[(0,100), (100,100), (100,200), (200,200)]
nmes=[gameTypes.Enemy(100, [], pathWaypoints, 1, 0)]
towers=[]
maxWaves=5
wave=0

def MoveEnemies(now):
    for nme in nmes:     
        nme.Move(now, wave, pathWaypoints)

def ExecuteTowers(now):
    for tower in towers:
        tower.Execute(now)

def CheckWaveEnd():
    activeCount=len(nmes)
    for nme in nmes:
        if nme.isDead or nme.isExited:
            activeCount=activeCount-1
    return activeCount==0

def DrawScreen():
    pass #TODO

#game loop
isRunning=True
logging.info("Starting game loop.")
while (isRunning):
    now = datetime.datetime.now()
    MoveEnemies(now)
    ExecuteTowers(now)
    if CheckWaveEnd():
        wave=wave+1
        if wave >= maxWaves:
            logging.info("Max wave limit reached. Ending loop.")
            isRunning=False
            continue
        else:    
            logging.debug("wave" + wave + " starting.")

logging.info("Game loop ended.")



