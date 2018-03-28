'''
Created on 02/03/2018

@author: Peter
'''


class TTile(object):
    '''
    classdocs
    '''
    __tileName = ""
    __groupFirst = 0
    __groupCount = 0
    __listaCoord2D = []

    def __init__(self, tileName="", groupFirst=0, groupCount=0, listaCoord2D=[]):
        '''
        Constructor
        '''
        __tileName = self.setTileName(tileName)
        __groupFirst = self.setGroupFirst(groupFirst)
        __groupCount = self.setGroupCount(groupCount)
        __listaCoord2D = self.setListaCoord2D(listaCoord2D)

    def getTileName(self):
        return self.__tileName

    def setTileName(self, name):
        if isinstance(name, str):
            self.__tileName = name
        else:
            raise Exception('Not quite my type of data: need a str')

    def getGroupFirst(self):
        return self.__groupFirst

    def setGroupFirst(self, first):
        if isinstance(first, int):
            self.__groupFirst = first
        else:
            raise Exception('Not quite my type of data: need a int')

    def getGroupCount(self):
        return self.__groupFirst

    def setGroupCount(self, count):
        if isinstance(count, int):
            self.__groupCount = count
        else:
            raise Exception('Not quite my type of data: need a int')

    def getListaCoord2D(self):
        return self.__groupFirst

    def setListaCoord2D(self, list2D):
        if isinstance(list2D, list):
            self.__listaCoord2D = list2D
        else:
            raise Exception(
                'Not quite my type of data: need a 2D array list of floats')
