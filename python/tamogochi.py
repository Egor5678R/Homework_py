from asyncio.windows_events import NULL
from distutils.command.install_egg_info import to_filename
import random, time
class Animals():
    
    def __init__(self,name,thirst,hunger,happiness,level,hp,exp):
        self.name=name
        self.hunger=0
        self.thirst=0
        self.hp=0
        self.happiness=0
        self.level=1
        self.ills=NULL
        self.exp=0
        

class Dog(Animals):
    def __init__(self,name,thirst,hunger,happiness,level,hp,exp):
        super().__init__(name,thirst,hunger,happiness,level,hp,exp)
        self.hp=100
        self.recEat=['корм','кость','мясо']
        self.recDrink=['вода фильтрованная','кефир']

        self.recGame=['апорт','палка-приманка','найди лакомство']
        self.hunger=100
        self.level=1
        self.happiness=100
        self.thirst=100
        self.ills=NULL
        

class Cat(Animals):
    def __init__(self,name,thirst,hunger,happiness,level,hp,exp):
        super().__init__(name,thirst,hunger,happiness,level,hp,exp)
        self.hp=90
        self.exp=0
        self.recEat=['корм','куриное мясо','рыба']
        self.recDrink=['вода фильтрованная','молоко']
        
        self.recGame=['найди лакомство','палка-дразнилка','качели']
        self.hunger=100
        self.level=1
        self.happiness=100
        self.thirst=100
        self.ills=NULL

class Parrot(Animals):
    def __init__(self,name,thirst,hunger,happiness,level,hp,exp):
        super().__init__(name,thirst,hunger,happiness,level,hp,exp)
        self.hp=50
        self.exp=0
        self.recEat=['морковь','овёс','семечки']
        self.recDrink=['вода фильтрованная']

        self.recGame=['']
        self.hunger=100
        self.level=1
        self.happiness=100
        self.thirst=100
        self.ills=NULL

class Hamster(Animals):
    def __init__(self,name,thirst,hunger,happiness,level,hp,exp):
        super().__init__(name,thirst,hunger,happiness,level,hp,exp)
        self.hp=15
        self.exp=0
        self.recEat=['корм','тыква','овёс']
        self.recDrink=['вода фильтрованная']
        self.recGame=['колесо']
        self.hunger=100
        self.level=1
        self.happiness=100
        self.thirst=100
        self.ills=NULL

class Kapibara(Animals):
    def __init__(self,name,thirst,hunger,happiness,level,hp,exp):
        super().__init__(name,thirst,hunger,happiness,level,hp,exp)
        self.hp=150
        self.exp=0
        self.recEat=['корм','арбуз','бананы']
        self.recDrink=['вода фильтрованная']
        self.recGame=['найди лакомство']
        self.hunger=100
        self.level=1
        self.happiness=100
        self.thirst=100
        self.ills=NULL

class Poni(Animals):
    def __init__(self,name,thirst,hunger,happiness,level,hp,exp):
        super().__init__(name,thirst,hunger,happiness,level,hp, exp)
        self.hp=200
        self.exp=0
        self.recEat=['корм','сено','трава']
        self.recDrink=['вода фильтрованная','вода из под крана']
        self.recGame=['найди лакомство']
        self.ills=NULL
        self.hunger=100
        self.level=1
        self.happiness=100
        self.thirst=100

class Karakal(Animals):
    def __init__(self,name,thirst,hunger,happiness,level,hp,exp):
        super().__init__(name,thirst,hunger,happiness,level,hp,exp)
        self.hp=95
        self.exp=0
        self.recEat=['корм','мясо индейки','варёное мясо']
        self.recDrink=['вода фильтрованная','молоко']
        self.recGame=['найди лакомство','мячики','плетёный шарик']
        self.ills=NULL
        self.hunger=100
        self.level=1
        self.happiness=100
        self.thirst=100


    
def drinking(drank):


    Drink=['вода из под крана','молоко','вода фильтрованная','яблочный сок','кефир']
    print('Выберите питьё:',Drink)
    intDrink=input().lower()
    if intDrink==drank.recEat[0] or intDrink==drank.recDrink[1]:
            print("Вы напоили своего питомца","\n+5 к счастью", "\n+2 к здоровью","\n+4 к опыту","\n+2 к жажде")
            drank.happiness+=5
            drank.hp +=2
            drank.thirst+=2
            drank.exp+=4



    else:
        print("Вы неправильно напоили своего питомца","\n-5 к счастью", "\n-2 к здоровью","-4 к опыту")
        drank.happiness-=5
        drank.hp-=2
        drank.exp-=4
    atil=random.randint(1,10)
    if atil<=4:
        print('Ваш питомец заболел','\nВам срочно нужно идти к ветиринару')
        print('1.Идти к ветеринару \n2.Не идти к ветиринару')
        di=int(input())
        if di==1:
            print("Вы сходили к ветиринару \n+4 к здоровью \n+4 к опыту")
            drank.hp +=4    
            drank.exp+=4
        elif di==2:
            print("Вы не сходили ко врачу ваш питомец умер")
            drank.hp=0
        else:
            print('Вы неправильно ввели команду')

def eating(ate):
    
    Eat=['корм','кость','мясо','куриное мясо','рыба','морковь','овёс','семечки','крецкий орех','тыква','изюм','бананы','трава','арбуз','сено','мясо индейки','варёное мясо']
    print('Выберите еду:',Eat)
    intEat=str(input()).lower()
    if intEat==ate.recEat[0] or intEat==ate.recEat[1] or intEat==ate.recEat[2]:
        print("Вы покормили своего питомца","\n+5 к счастью", "\n+10 к здоровью","\n+10 к опыту","\n+2 к голоду")
        ate.happiness+=5
        ate.hp += 10
        ate.hunger+=2
        ate.exp+=10

    else:
        print("Вы неправильно покормили своего питомца","\n-5 к счастью", "\n-10 к здоровью","-10 к опыту")
        ate.happiness-=5    
        ate.hp-=5
        ate.exp-=10
        atil=random.randint(1,10)
        if atil<=4:
            print('Ваш питомец заболел','\nВам срочно нужно идти к ветиринару')
            print('1.Идти к ветеринару \n2.Не идти к ветиринару')
            di=int(input())
            if di==1:
                print("Вы сходили к ветиринару \n+10 к здоровью \n+10 к опыту")
                ate.hp +=10

                ate.exp+=10
            elif di==2:
                print("Вы не сходили ко врачу ваш питомец умер")
                ate.hp=0
            else:
                print('Вы неправильно ввели команду')    

def games(game):
    Game=['палка-приманка','колесо','апорт','найди лакомство','мячики','удочка-дразнилка','качели','плетёный шарик']
    print('Выбирите игру:',Game)
    intGame=input().lower()     
    if intGame==game.recGame[0] or intGame==game.recGame[1] or intGame==game.recGame[2]:
        print("Вы поиграли со своим питомцем","\n+10 к счастью", "\n+10 к опыту")
        game.happiness+=10
            
        game.exp+=10

    else:
        print("Вы неправильно поиграли со своим питомцем","\n-10 к счастью","-10 к опыту")
        game.happiness-=10
            
        game.exp-=10 
    
def gamE(self):
    if self.exp==100:
        self.level+=1
    elif self.level==5:
        quit()
    elif self.hp==0:
        quit()
ani=input('Выбирите питомца  ').lower()
nam=input('Назовите своего питомца  ').lower()
if ani=='karakal':
    anim=Karakal(nam,thirst=100,hunger=100,happiness=100,level=1,hp=95,exp=0)
    print('Вы выбрали питомца собаку')
elif ani=='dog':
    anim=Dog(nam,thirst=100,hunger=100,happiness=100,level=1,hp=100,exp=0)
    print('Вы выбрали питомца собаку')

elif ani=='cat':
    anim=Cat(nam,thirst=100,hunger=100,happiness=100,level=1,hp=90,exp=0)
    print('Вы выбрали питомца кошку')
elif ani=='parrot':
    anim=Parrot(nam,thirst=100,hunger=100,happiness=100,level=1,hp=50,exp=0)
    print('Вы выбрали питомца попугая')
elif ani=='kapibara':
    anim=Kapibara(nam,thirst=100,hunger=100,happiness=100,level=1,hp=150,exp=0)
    print('Вы выбрали питомца капибару')
elif ani=='hamster':
    anim=Hamster(nam,thirst=100,hunger=100,happiness=100,level=1,hp=15,exp=0)
    print('Вы выбрали питомца хомяка')
elif ani=='poni':
    anim=Poni(nam,thirst=100,hunger=100,happiness=100,level=1,hp=200,exp=0)
    print('Вы выбрали питомца пони')
else:
    print('Питомец выбран неправильно')
    quit()   


    
while True:
    time.sleep(5)
    doing=int(input("Выбирите действие: \n1.Покормить \n2.Напоить \n3.Поиграть \n4.Статистика \n"))
    
    if doing==4:
        print(f'Здоровье питомца: {anim.hp}')
        print(f'Счастье питомца: {anim.happiness}')
        print(f'Голод питомца: {anim.hunger}')
        print(f'Жажда питомца: {anim.thirst}')
        print(f'Уровень питомца: {anim.level}')
    elif doing==1:
        eat=eating(anim)
        eat.eating()
    elif doing==2:
        drink=drinking(anim)
        drink.drinking()
    elif doing==3:
        game=games(anim)
        game.games()

    else:
        print('Неизвесная команда')    
    time.sleep(30)
    anim.hp-=5
    anim.hunger-=10
    anim.thirst-=10
    anim.happiness-=10
    
    
    

    
        
        


    

    


          
