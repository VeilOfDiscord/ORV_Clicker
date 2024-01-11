# Handles majority of the game logic.
class game:
    def __init__(self, coin, enemy_health, dmg, npc, dmg_help):
        self.coin = coin

        self.enemy_health = enemy_health
        self.health = enemy_health        
        self.dmg = dmg

        self.npc = npc
        self.dmg_help = dmg_help 

        self. enemy_mult = 1.1

    def updateHealth(self):
        if (self.health < 1000.0):
            self.enemy_mult = 1.549   
        elif (self.health > 1000.0):
            self.enemy_mult = 2.1863

    def updateDamage(self):
        if (self.dmg < 20.0):
            dmg_incr = 1.5
        elif (self.dmg > 21.0 and self.dmg < 1000.0):
            dmg_incr = 2.5
        elif (self.dmg > 101.0 and self.dmg < 10000.0):
            dmg_incr = 3.33

    def respawnEnemy(self):
        self.updateHealth()
        self.health = self.health * self.enemy_mult
        self.enemy_health = self.health
        self.coin += 100

    def dealDamage(self):
        self.enemy_health = self.enemy_health - self.dmg
        print("Dealt", self.dmg,"dmg, enemy now at", self.enemy_health, "hp")