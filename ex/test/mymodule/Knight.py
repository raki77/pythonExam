
class Knight:
    def __init__(self, name):
        self.name = name
        self.strength = 0
        self.dex = 0
        self.vitality = 0
        self.wisdom = 0
        self.knowledge = 0
        self.Charisma = 0
        self.damage = 0
        self.depense = 0
        self.emo = Emotion(name)
    def setDamage(self, strength, weapon):
        self.damage = self.strength + weapon        
    def getDamage(self):
        return self.damage
    def setDepense(self, strength, amor):
        self.depense = self.dex + amor        
    def getDepense(self):
        return self.depense
    def getStatus(self):
        print(f'---------------------------')
        print(f'strength: {self.strength}')
        print(f'dex: {self.dex}')
        print(f'vitality: {self.vitality}')
        print(f'wisdom: {self.wisdom}')
        print(f'knowledge: {self.knowledge}')
        print(f'Charisma: {self.Charisma}')
        print(f'---------------------------')
        print(f'damage: {self.damage}')
        print(f'depense: {self.depense}')
        print(f'---------------------------')
    def attack(self, damage):
        print(f'{self.name}님이 공격[{damage}] 하였습니다.')
    def setEmotion(self, emotion):
        self.emo = emotion
    def getEmotion(self) :
        self.emo
    def setInitValue(self):
        self.strength = 18
        self.dex = 12
        self.vitality = 16
        self.Charisma = 8
        self.wisdom = 11
        self.knowledge = 6

class Weapon :
    def __init__(self, id, sword):
        self.id = id
        self.sword = sword
        self.damage = 0
        self.limit = []
    def setInitValue(self):
        self.id = '000001'
        self.sword = 'short-sword'
        self.damage = 20
        self.limit = ['기사', '요정']

class Emotion :
    def __init__(self, name):
        self.name = name
    def move(self):
        print(f'{self.name}님이 [이동] 하였습니다.')
    def stop(self):
        print(f'{self.name}님이 [정지] 하였습니다.')
    def sayHello(self):
        print(f'{self.name}님이 [인사] 하였습니다.')
    def battleSt(self):
        print(f'{self.name}님이 [전투]를 시작 하였습니다.')
    def battleEnd(self):
        print(f'{self.name}님이 [전투]를 종료 하였습니다.')