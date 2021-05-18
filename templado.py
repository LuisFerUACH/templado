import numpy as np

def getVecindad(actual, proble):
    return proble[actual]

def siguiente(vecindad, fs):
    fmejor =0
    mejor = None
    for edo in vecindad:
        if fs[edo] > fmejor :
            mejor = edo
            fmejor = fs[edo]
    return mejor

def temSim(ini, proble, fs):
    mejor = ini
    actual = ini
    T =25
    while T >0.25:
        vecindad = getVecindad(actual, proble)
        nuevo = siguiente(vecindad, fs)
        if fs[nuevo] <= fs[mejor]:
            mejor = nuevo
        else:
            r = np.random.uniform()
            ppeor = np.exp((fs[mejor] - fs[nuevo])/T)
            if r < ppeor:
                mejor = nuevo
        actual = nuevo
        T = T *0.5
    return mejor

def main(ini):
    proble ={ 'A':[ 'B','C','D'] ,'B':[ 'A','C','E','F'] ,
              'C':[ 'A','B','D','F','G'] ,'D':[ 'A','C','G','K'] ,
              'E':[ 'B','F','I','H'] ,'F':[ 'B','C','E','I','G'],
              'G':[ 'D','C','F','I','J','K'] ,'H':[ 'E','I','L'] ,
              'I':[ 'E','F','H','L','J'] ,'J':[ 'I','G','M','N','K'] ,
              'K':[ 'D','G','J','N'] ,'L':[ 'I','H','M'] ,
              'M':[ 'L','J','N'] ,'N':[ 'M','J','K']}
    ## La altura de cada estado
    fs ={ 'A':25 , 'B':20, 'C':23 , 'D':18 , 'E':12 , 'F':23, 'G':15, 'H':15, 'I':16, 'J':5, 'K':25, 'L':25, 'M':3, 'N':12}
    mejor = temSim (ini, proble , fs )
    print ('La mejor solucion encontrada partiendo del nodo ' + ini + ' fue '+ mejor )
    
if __name__ == '__main__':
    indi = np.random.randint(1, 15)
    nodoInicial = ''
    if indi==1:
        nodoInicial = 'A'
    elif indi==2:
        nodoInicial = 'B'
    elif indi==3:
        nodoInicial = 'C'
    elif indi==4:
        nodoInicial = 'D'
    elif indi==5:
        nodoInicial = 'E'
    elif indi==6:
        nodoInicial = 'F'
    elif indi==7:
        nodoInicial = 'G'
    elif indi==8:
        nodoInicial = 'H'
    elif indi==9:
        nodoInicial = 'I'
    elif indi==10:
        nodoInicial = 'J'
    elif indi==11:
        nodoInicial = 'K'
    elif indi==12:
        nodoInicial = 'L'
    elif indi==13:
        nodoInicial = 'M'
    elif indi==14:
        nodoInicial = 'N'
    main(nodoInicial)