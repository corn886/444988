import random
class Pet():
    def __init__(self,name,age,times,emotion,saturation,health,active):
        self.name = name
        self.age = age
        self.times = times
        self.emotion = emotion
        self.saturation = saturation
        self.health = health
        self.active = active
    def eat(self):
        d.saturation += 30
        d.emotion += 10
    def touch(self):
        d.emotion += 20
    def clean(self):
        d.saturation -= 20
        d.health += 10
    def fight(self):
        d.emotion -= 50
        d.saturation -= 20
        d.health -= 10
    def kill(self):
        d.health -= 99999999
    def toPrint(self):
        print('%+12s'%f)
        print('%s'%self.name)
        print('%s%-13s%s%s'%("年齡",self.age,"行動次數",self.times))
        print('%s'%(self.active))
n = input("給寵物取個名字吧！")
d = Pet(n,0,0,50,50,50,0)
f = ("(O w O)")
print('%+12s'%f)
print('%s'%d.name)
while True:
    try:
        a = int(input("要做些甚麼呢？1.餵食 2.摸頭 3.打掃 4.打他 5.殺了他(其他輸入為隨機）"))
    except ValueError:
        a = random.randint(1,5)
    d.times += 1
    if a == 1:
        d.eat()
        a = "進食中"
        f = ("( O ~ O )")
    elif a == 2:
        d.touch()
        a = "好感度上升"
        f = ("(O ∀ O)~♥")
    elif a == 3:
        d.clean()
        a = "房間乾淨了一點"
        f = ("d(O ∀ O)b")
    elif a == 4:
        d.fight()
        a = "受傷了..."
        f = ("(T A T)")
    elif a == 5:
        d.kill()
    elif a:
        a = random.randint(1,5)
        if a == 1:
            d.eat()
            a = "進食中"
            f = ("( O ~ O )")
        elif a == 2:
            d.touch()
            a = "好感度上升"
            f = ("(O ∀ O)~♥")
        elif a == 3:
            d.clean()
            a = "房間乾淨了一點"
            f = ("d(O ∀ O)b")
        elif a == 4:
            d.fight()
            a = "受傷了..."
            f = ("(T A T)")
        elif a == 5:
            d.kill()
    d.saturation -= 10
    if d.saturation < 0:
        d.health -= 10
    elif d.saturation > 100:
        d.health -= 5
    elif d.emotion < 0:
        d.health -= 20
    if d.health <= 0:
        print('%+12s'%"(X ﹃ X)")
        print('%s'%d.name)
        print("享年",d.age,"歲")
        print("他死的真慘 ŏ _ ŏ")
        break
    if d.times == 5:
        d.age += 1
        d.times = 0
    d = Pet(n,d.age,d.times,d.emotion,d.saturation,d.health,a)
    d.toPrint()