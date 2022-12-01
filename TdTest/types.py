import datetime

class Attack:
    dmg=0
    dmgTypeIndex=0

    def __init__(self, dmg, dmgTypeIndex):
        self.dmg=dmg
        self.dmgTypeIndex=dmgTypeIndex

class Nme:
    gridX=0
    gridY=0
    speed=0
    maxHealth=0
    health=0
    dmgMods=[1,1,1,1]
    lastMove=datetime.datetime.now()
    nextWaypointIndex=1
    isDead=False

    def __init__(self, maxHealth, speed, dmgMods):
        self.maxHealth=maxHealth
        self.health=maxHealth
        self.speed=speed
        self.dmgMods=dmgMods
        self.gridX=0
        self.gridY=0

    def Move(self, now, pathWaypoints):
        elapsed=now-self.lastMove
        #calculate new gridX gridY from current position to next waypoint based on elapsed time; set coordinates to that position

    def AcceptAttack(self, attack):
        mult=1
        if attack.dmgTypeIndex >=0 and attack.dmgTypeIndex < len(self.dmgMods):
            mult=self.dmgMods[attack.dmgTypeIndex]

        health = health - attack.dmg * mult
        if health<=0:
            self.isDead=True

class Tower:
    gridX=0
    gridY=0
    maxHealth=0
    health=0
    dmgMods=[1,1,1,1]
    attack=Attack(0,0)
    lastExecute=datetime.datetime.now()

    def __init__(self, maxHealth, dmgMods, attack):
        self.maxHealth=maxHealth
        self.health=maxHealth
        self.dmgMods=dmgMods
        self.attack=attack
       
    def Execute(self, nmes):
        for nme in nmes:
            nme.AcceptAttack(self.attack)


    
    
