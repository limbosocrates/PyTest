import datetime
import logging
import uuid
import math

class Attack:
    dmg=0
    dmgTypeIndex=0
    range=0

    def __init__(self, dmg, dmgTypeIndex, range):
        self.dmg=dmg
        self.dmgTypeIndex=dmgTypeIndex

class Enemy:
    _id=uuid.uuid4()
    _lastMove=datetime.datetime.now()
    _nextWaypointIndex=1
    _health=0
    _gridX=0
    _gridY=0
    
    speed=0
    maxHealth=0
    dmgMods=[1,1,1,1]
    spawnWave=0
    spawnDelay=0
    isSpawned=False
    isDead=False
    isExited=False

    def __init__(self, maxHealth, speed, dmgMods, spawnWave, spawnDelay):
        self.maxHealth=maxHealth
        self._health=maxHealth
        self.speed=speed
        self.dmgMods=dmgMods
        self.spawnWave=spawnWave
        self.spawnDelay=spawnDelay

    def Move(self, now, wave, pathWaypoints):
        if self.isDead or self.isExited:
            return
        if not self.isSpawned:
            x=0 #calculate whether spawn time has passed and 

        elapsed=now-self._lastMove
        #calculate new gridX gridY from current position to next waypoint based on elapsed time; set coordinates to that position
        #check whether last waypoint has been passed, in which case set isExited to true, and whatever else

    def ApplyAttack(self, attack):
        if self.isDead or self.isExited:
            return
        mult=1
        if attack.dmgTypeIndex >=0 and attack.dmgTypeIndex < len(self.dmgMods):
            mult=self.dmgMods[attack.dmgTypeIndex]

        health = health - attack.dmg * mult
        logging.debug(id + " takes " + attack.dmg + "*" + mult + " of type " + attack.dmgTypeIndex + " damage.")
        if health<=0:
            self.isDead=True
            logging.debug(id + " is dead.")

class Tower:
    _gridX=0
    _gridY=0
    _health=0
    maxHealth=0
    dmgMods=[1,1,1,1]
    attack=Attack(0,0,0)
    lastExecute=datetime.datetime.now()

    def __init__(self, maxHealth, dmgMods, attack):
        self.maxHealth=maxHealth
        self._health=maxHealth
        self.dmgMods=dmgMods
        self.attack=attack
       
    def Execute(self, nmes):
        for nme in nmes:
            nme.AcceptAttack(self.attack)
    
    def IsInRange(self, nme):
        return CalculateDistance(nme._gridX, nme._gridY, self._gridX, self._gridY) <= self.attack.range

def CalculateDistance(x1,y1,x2,y2):
    return math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

    
    
