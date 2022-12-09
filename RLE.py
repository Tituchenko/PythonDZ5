import os.path

def RLEcoding (str):
    prevS=''
    numPrevS=0
    result=''
    for s in str:
        if not s.isdigit():
            if prevS=='':
                prevS=s
                numPrevS+=1
            else:
                if s==prevS:
                    numPrevS+=1
                else:
                    result+=f'{numPrevS}{prevS}'
                    prevS=s
                    numPrevS=1
        else:
            if numPrevS>0:
                result += f'{numPrevS}{prevS}'
            prevS=''
            numPrevS=0
            result+=f'\{s}\\'
    if not prevS=='':
            result += f'{numPrevS}{prevS}'
    return result

def RLEencoding (str):
    arrS=[]
    numInS=[]
    result=''
    for s in str:
        if s.isdigit():
            if len(numInS)<(len(arrS)+1):
                numInS.append(int(s))
            else:
                numInS[len(arrS)]=numInS[len(arrS)]*10+int(s)
        else:
            arrS.append(s)
    for i,s in enumerate(arrS):
        for j in range (0,numInS[i]):
            result+=s
    return result

fileNameBase=''
while (not (os.path.exists (fileNameBase))):
    fileNameBase=input(f'Введите название файла для кодированя:')
fileNameCode=input(f'Введите название файла для сохранения результата кодирования:')
fileNameEncode=''
while (not (os.path.exists (fileNameEncode)) or fileNameEncode==fileNameCode):
    fileNameEncode=input(f'Введите название файла для раскодирования:')

fileNameEncodeResult=input(f'Введите название файла для сохранения результата раскодирования:')
BaseFile=[]
CodeFileFromBase=[]
with open(fileNameBase,'r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        else:
            BaseFile.append(line.rstrip())
            CodeFileFromBase.append(RLEcoding (line.rstrip()))
with open(fileNameCode,'w') as f:
    for str in CodeFileFromBase:
        f.writelines(str+'\n')
CodeFile=[]
EncodeFile=[]
with open(fileNameEncode,'r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        else:
            CodeFile.append(line.rstrip())
            EncodeFile.append(RLEencoding (line.rstrip()))
with open(fileNameEncodeResult,'w') as f:
    for str in EncodeFile:
        f.writelines(str+'\n')
