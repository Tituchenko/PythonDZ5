# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""
from random import choice,randint
candyOnTable=150
maxCanTake=28
round=1


def checkWin(who):
    if candyOnTable==0:
        print (f'Игра заершена на {round} ходу. Победил - {who}!!!')

def getHumanTurn ():
    global candyOnTable,maxCanTake
    anotherTurn=True
    while (anotherTurn):
        numTurn=int(input(f'Ход {round}. Ход человека. На столе {candyOnTable} конфет. Сколько заберете? (max={maxCanTake}):'))
        if numTurn > 0 and numTurn <= maxCanTake and numTurn<=candyOnTable:
            anotherTurn=False
    candyOnTable-=numTurn
    checkWin ('Человек')

def getCompTurn ():
    global candyOnTable, maxCanTake
    if candyOnTable<=maxCanTake:
        turn=candyOnTable
    else:
        turn=candyOnTable%(maxCanTake+1)
        if turn==0:
            turn=randint(1,maxCanTake)
    print (f'Ход {round}. Ход компьютера. На столе {candyOnTable} конфет. Сколько заберете? (max={maxCanTake}):{turn}')
    candyOnTable -= turn
    checkWin('Комьютер')

if choice([0,1])==0:
    firstTurn=getHumanTurn
    secondTurn=getCompTurn

else:
    firstTurn = getCompTurn
    secondTurn = getHumanTurn


while candyOnTable>0:
    firstTurn()
    if  candyOnTable>0:
        secondTurn()
    round+=1
