'''
Created on 02/03/2018

@author: Peter

Class TReport é uma classe que cria objectos que contêm informação dos relatórios guardados pelo
TSlave quando corrida uma task

Variáveis:
ComputerName - string - Nome do PC que processou determinado bloco
BlokName - string - Nome da tile processada
LoadedPtsAct - int - Pontos abertos do bloco
LoadedPtsNgb - int - Pontos abertos do neighbour
SavedPts - int - Pontos Salvos
ListaOrdens - ["string"] -  lista das ordens que fazem parte da macro/task 
Status - Boolean - sucesso ou insucesso da task para o determinado bloco
'''

import re


class TReport(object):
    '''
    classdocs
    '''
    __computerName = ""
    __tileName = ""
    __loadedPtsAct = 0
    __loadedPtsNgb = 0
    __savedPts = 0
    __tStatus = False
    __listaOrdens = []

    def __init__(self):
        '''
        Constructor
        '''

    def readFile(self, streamFileTReport):
        with open(streamFileTReport) as fin:
            listaOrdensTmp = []
            for linha in fin:
                if 'Computer=' in linha:
                    self.setComputerName(re.split('=|\n', linha)[1])
                elif 'Block' in linha:
                    self.setTileName(re.split('\n', linha)[0])
                elif 'active' in linha:
                    self.setLoadedPtsAct(int(re.findall('\d+', linha)[0]))
                elif 'neighbouring' in linha:
                    self.setLoadedPtsNgb(int(re.findall('\d+', linha)[0]))
                elif 'FnScan' in linha:
                    listaOrdensTmp.append(re.split('\n', linha)[0])
                elif 'Saved' in linha:
                    self.setSavedPts(int(re.findall('\d+', linha)[0]))
                elif 'Status' in linha:
                    if 'Success' in linha:
                        self.setStatus(True)
        self.setlLstaOrdens(listaOrdensTmp)

    def getComputerName(self):
        return self.__computerName

    def setComputerName(self, name):
        if isinstance(name, str):
            self.__computerName = name
        else:
            print('Not quite my type of data: need a str')
            raise Exception('Not quite my type of data: need a str')

    def getTileName(self):
        return self.__tileName

    def setTileName(self, name):
        if isinstance(name, str):
            self.__tileName = name
        else:
            print('Not quite my type of data: need a str')
            raise Exception('Not quite my type of data: need a str')

    def getLoadedPtsAct(self):
        return self.__loadedPtsAct

    def setLoadedPtsAct(self, count):
        if isinstance(count, int):
            self.__loadedPtsAct = count
        else:
            print('Not quite my type of data: need a int')
            raise Exception('Not quite my type of data: need a int')

    def getLoadedPtsNgb(self):
        return self.__loadedPtsNgb

    def setLoadedPtsNgb(self, count):
        if isinstance(count, int):
            self.__loadedPtsNgb = count
        else:
            print('Not quite my type of data: need a int')
            raise Exception('Not quite my type of data: need a int')

    def getSavedPts(self):
        return self.__savedPts

    def setSavedPts(self, count):
        if isinstance(count, int):
            self.__savedPts = count
        else:
            print('Not quite my type of data: need a int')
            raise Exception('Not quite my type of data: need a int')

    def getStatus(self):
        return self.__tStatus

    def setStatus(self, status):
        if isinstance(status, bool):
            self.__tStatus = status
        else:
            print('Not quite my type of data: need a bool')
            raise Exception('Not quite my type of data: need a bool')

    def getListaOrdens(self):
        return self.__listaOrdens

    def setlLstaOrdens(self, strList):
        if isinstance(strList, list):
            self.__listaOrdens = strList
        else:
            print('Not quite my type of data: need a list of strings')
            raise Exception(
                'Not quite my type of data: need a list of strings')
