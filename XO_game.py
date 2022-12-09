from random import choice
winPositions=({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}) # выигрышые позиции
game =[x for x in range(1,10)]
round=0
def printGame (game):
    print('┌─┬─┬─┐')
    print(f'|{game[0]}|{game[1]}|{game[2]}|')
    print ('├─┼─┼─┤')
    print(f'|{game[3]}|{game[4]}|{game[5]}|')
    print ('├─┼─┼─┤')
    print(f'|{game[6]}|{game[7]}|{game[8]}|')
    print('└─┴─┴─┘')

def getHumanTurn (game,symbol):
    numTurn=0
    anotherTurn=True
    while (anotherTurn):
        numTurn=int(input(f'Ход {round} ({symbol}):'))
        if numTurn > 0 and numTurn < 10:
            if (str(game[(numTurn)-1]).isdigit()):
                anotherTurn=False
    game [numTurn-1]=symbol
    return game

def getPosition (game,symbol): #Возвращает список занятых symbol позиций
    return  [i+1 for i,x in enumerate(game) if x==symbol]

def anotherSymbol (symbol):
    if symbol=='X':
        return 'O'
    else:
        return 'X'

def checkWin (game,symbol):
    pos=getPosition(game,symbol)
    for wp in winPositions:
        if wp.issubset(pos):
            return True
    return False

def getCurWinPosition (game,symbol):
    # возвращает список ->
    # [0]-список множеств, по которым еще можно выиграть с учетом текущих позиций противника.
    # [1]-сколько в этих множеств наших позиций
    curPos=[]
    curPosHasMy=[]
    posAnother=getPosition (game,anotherSymbol(symbol))
    posMy = getPosition(game, symbol)
    for wp in winPositions:
        for p in posAnother:
            if p in wp:
                break
        else:
            hasMy=0
            for p in posMy:
                if p in wp:
                   hasMy+=1
                   wp.remove(p)
            curPos.append(wp)
            curPosHasMy.append(hasMy)
    return curPos,curPosHasMy

def getFreePos (game):# возвращает свободные позиции
    return [x for x in range (1,10) if str(game[x-1]).isdigit()]

def checkNextTurnWin (game,symbol): # проверяет можно ли победить symbol следующим ходом
    freePos = getFreePos(game)
    for i in freePos:
        gameTemp=game.copy()
        gameTemp[i-1]=(symbol)
        if checkWin (gameTemp,(symbol)):
            return i
    else:
        return 0

def getCompTurn (game,symbol): # ход компьютера
    # Проверим можем ли победить
    checkMy=checkNextTurnWin(game,symbol)
    if checkMy>0:
        game[checkMy - 1] = symbol
        print(f'Ход {round} ({symbol}):{checkMy}')
        return game
    # Проверим может ли соперник победить следующим
    checkOpponent=checkNextTurnWin(game,anotherSymbol(symbol))
    if checkOpponent>0:
        game[checkOpponent - 1] = symbol
        print(f'Ход {round} ({symbol}):{checkOpponent}')
        return game
    # иначе вытащим возможные ходы, входящие в выигрышные на текущий момент комбинации
    curWinPosition=getCurWinPosition(game,symbol)
    realTurn=set()
    realTurnInWin=[0]*10
    for i in range(0,len(curWinPosition[1])):
        # в ходах в выигрышных комбинациях оставим только те, в которых уже есть наши ходы максимально
        if curWinPosition[1][i]==max(curWinPosition[1]):
            realTurn.update(list(curWinPosition[0][i]))
            # посчитаем также в скольких выигрышных комбинациях есть возможные ходы (увеличиваем шанс вилки!)
            for j in curWinPosition[0][i]:
                realTurnInWin[j]+=1

    if len (realTurn)>0:
        realTurnMaxInWin=set()
        for rt in realTurn:
            if realTurnInWin[rt]==max(realTurnInWin):
                realTurnMaxInWin.add(rt)
        turn=choice(list(realTurnMaxInWin))

    else:
        turn=choice(getFreePos(game))
    game[turn - 1] = symbol
    print (f'Ход {round} ({symbol}):{turn}')
    return game


if choice([0,1])==0:
    firstTurn=getHumanTurn
    secondTurn=getCompTurn
else:
    firstTurn = getCompTurn
    secondTurn = getHumanTurn
while not checkWin (game,'X') and not checkWin(game,'O') and len(getFreePos(game))>0:
    round+=1
    printGame (game)
    game=firstTurn (game,'X')
    if len(getFreePos(game))>0 and not checkWin(game,'X'):
        printGame(game)
        game=secondTurn(game,'O')
if not checkWin (game,'X') and not checkWin(game,'O'):
    print ('Ничья!')
elif checkWin (game,'X'):
    print ('Победила команда X')
else:
    print('Победила команда O')