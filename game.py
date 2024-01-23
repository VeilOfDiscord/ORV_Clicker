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

        self.monsterCount = 0
        self.stageNum = 0

    def renderText(self, screen, font, text, colour, pos):
        label = font.render(text, 1, colour)
        screen.blit(label, pos)

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

        if self.monsterCount < 6:
            self.monsterCount = self.monsterCount + 1
        else:
            self.monsterCount = 0

        

    def dealDamage(self):
        self.enemy_health = self.enemy_health - self.dmg
        print("Dealt", self.dmg,"dmg, enemy now at", self.enemy_health, "hp")

    def recruitCompanion(self):
        if self.npc < 6:
            self.npc = self.npc + 1


    def updateStage(self, font, screen):
        if self.monsterCount == 0:
            self.monsterCount += 1
            self.stageNum += 1

        self.renderText(screen, font, "Stage "+str(self.stageNum), (255,255,255), (20,20))


    def normalizedHP(self, bar):
        #max of 300
        # different health bars
        # decrease green bar as much proportionally as needed
        # hp is 300, damage taken is 10, so take off 10/300 of the green bar
        dmg_taken = self.health - self.enemy_health
        percentage_dmg = 

        
