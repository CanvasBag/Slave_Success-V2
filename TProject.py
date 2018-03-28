'''
Created on 02/03/2018

@author: Peter

Classe TProject é uma classe que define um objecto onde irá ser guardada informação de um projecto TerraScan
TProject tem 2 variáveis: Cabecalho e a ListaDeTiles

** Cabecalho:
Lista de array de 2 dimensões, com a seguinte tipo de dados: [texto, texto]; em que cada posição representa a informação 
que se encontra no cabeçalho dos projectos TScan
[ [a, b]
  .
  .
  [n, n]]

** DicionarioDeTiles:
Dicionario que contém objectos do tipo TTile, esta "lista" corresponde ao conjunto de tiles que definem o projecto
'''

from itertools import islice
from multi_key_dict import multi_key_dict
from TTile import TTile
import re


class TProject(object):
    '''
    classdocs
    '''

    __storageType = ''
    __description = ''
    __cabecalho = []
    __dicTiles = multi_key_dict()

    def __init__(self):
        '''
        Constructor
        '''

    def readFile(self, streamFileTProject):
        cabecalhoTmp = []
        dicTmp = multi_key_dict()
        tileID = 1
        inCabecalho = True
        tileName = ''
        groupF = 0
        groupC = 0
        listCoord = []
        with open(streamFileTProject) as fin:
            for linha in islice(fin, 1, None):
                if inCabecalho:
                    if linha != "\n":
                        # split segundo os caracteres = e \n, ex.: 'StoreEcho=1\n'
                        # -> ['StoreEcho', '1', '']
                        par = re.split('=|\n', linha)
                        if 'Storage' in linha:
                            self.__storageType = par[1]
                        elif 'Description' in linha:
                            self.__description = par[1]
                        cabecalhoTmp.append([par[0], par[1]])
                        continue
                    else:
                        inCabecalho = False
                        continue
                elif self.__getSorageTypeFile() in linha:
                    tileName = re.split('\n', linha)[0]
                elif 'GroupFirst' in linha:
                    groupF = re.split('=|\n', linha)[1]
                elif 'GroupCount' in linha:
                    groupC = re.split('=|\n', linha)[1]
                elif '\n' == linha:
                    newTile = TTile(tileName, int(groupF),
                                    int(groupC), listCoord)
                    dicTmp[tileID, tileName] = newTile
                    tileID += 1
                    listCoord = []

                else:
                    pto = re.findall("[-+]?\d*\.\d+|\d+", linha)
                    listCoord.append([float(pto[0]), float(pto[1])])
        self.setCabecalho(cabecalhoTmp)
        self.setDicTiles(dicTmp)

    def __getSorageTypeFile(self):
        return 'fbi' if 'Fast' in self.__storageType else \
            'bin' if 'Terra' in self.__storageType else \
            'las' if 'LAS' in self.__storageType else \
            'laz'

    def getStorageType(self):
        return self.__storageType

    def getDescription(self):
        return self.__description

    def getCabecalho(self):
        return self.__cabecalho

    def setCabecalho(self, listArray):
        '''Lista de array de 2 dimensões: ["txt", "txt"] informação dos cabeçalhos dos projectos TScan 
        ex.: Scanner=Airborne ["Scanner", "Airborne"]'''
        self.__cabecalho = listArray

    def getDicTiles(self):
        return self.__dicTiles

    def setDicTiles(self, dictry):
        """Dic que contém objectos do tipo TTile"""
        self.__dicTiles = dictry

    def getTilesCount(self):
        return len(self.__dicTiles)
