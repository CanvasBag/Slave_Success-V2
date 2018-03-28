'''
Created on 02/03/2018

@author: Peter
'''

import re
import ntpath


class TTask(object):
    '''
    classdocs
    '''
    __fileName = ""
    __fileLocation = ""
    __macroName = ""
    __macroLocation = ""
    __neighbours = 0.0
    __projectName = ""
    __targetBlocks = []
    __task = []
    __saveResults = 0
    __reportFiles = []

    def __init__(self):
        '''
        Constructor
        '''


    def readFile(self, stringDirectory):
        listaTaskTmp = []
        self.setFileName(re.split('\.', ntpath.split(stringDirectory)[1])[0])
        self.setFileLocation(ntpath.split(stringDirectory)[0])
        with open(stringDirectory) as fin:
            for linha in fin:
                listaTaskTmp.append(re.split('\n', linha)[0])
                if 'Macro=' in linha:
                    self.setMacroName(re.split('\.', ntpath.split(
                        re.split('=|\n', linha)[1])[1])[0])
                    self.setMacroLocation(ntpath.split(
                        re.split('=|\n', linha)[1])[0])
                elif 'Neighbours' in linha:
                    self.setneighBours(float(re.split('=|\n', linha)[1]))
                elif 'SaveResults' in linha:
                    self.setSaveResults(int(re.split('=|\n', linha)[1]))
                elif 'Blocks=' in linha:
                    linhaSplit = re.split('=|-|\n', linha)
                    if len(linhaSplit) == 3:  # para o caso de ser só um bloco
                        self.addTargetBlocks([linhaSplit[1]])
                    elif len(linhaSplit) == 4:  # para o caso de ser mais de um bloco
                        self.addTargetBlocks([linhaSplit[1], linhaSplit[2]])
                elif 'Project=' in linha:
                    self.setProjectName(re.split('\.', ntpath.split(
                        re.split('=|\n', linha)[1])[1])[0])
        self.setTask(listaTaskTmp)

    def getFileName(self):
        return self.__fileName

    def setFileName(self, name):
        if isinstance(name, str):
            self.__fileName = name
        else:
            print('Not quite my type of data: need a str')
            raise Exception('Not quite my type of data: need a str')

    def getFileLocation(self):
        return self.__fileLocation

    def setFileLocation(self, location):
        if isinstance(location, str):
            self.__fileLocation = location
        else:
            print('Not quite my type of data: need a str')
            raise Exception('Not quite my type of data: need a str')

    def getMacroName(self):
        return self.__macroName

    def setMacroName(self, name):
        if isinstance(name, str):
            self.__macroName = name
        else:
            print('Not quite my type of data: need a str')
            raise Exception('Not quite my type of data: need a str')

    def getMacroLocation(self):
        return self.__macroLocation

    def setMacroLocation(self, location):
        if isinstance(location, str):
            self.__macroLocation = location
        else:
            print('Not quite my type of data: need a str')
            raise Exception('Not quite my type of data: need a str')

    def getneighBours(self):
        return self.__neighbours

    def setneighBours(self, nghbs):
        if isinstance(nghbs, float):
            self.__neighbours = nghbs
        else:
            print('Not quite my type of data: need a float')
            raise Exception('Not quite my type of data: need a float')

    def getProjectName(self):
        return self.__projectName

    def setProjectName(self, pName):
        if isinstance(pName, str):
            self.__projectName = pName
        else:
            print('Not quite my type of data: need a str')
            raise Exception('Not quite my type of data: need a str')

    def getTargetBlocks(self):
        return self.__targetBlocks

    def setTargetBlocks(self, tBlocks):
        if isinstance(tBlocks, list):
            self.__targetBlocks = tBlocks
        else:
            print('Not quite my type of data: need a str')
            raise Exception('Not quite my type of data: need a list')

    def addTargetBlocks(self, tBlocks):
        if isinstance(tBlocks, list):
            self.__targetBlocks.append(tBlocks)
        else:
            print('Not quite my type of data: need a list')
            raise Exception('Not quite my type of data: need a list')

    def getTask(self):
        return self.__task

    def setTask(self, task):
        if isinstance(task, list):
            self.__task = task
        else:
            print('Not quite my type of data: need a list')
            raise Exception('Not quite my type of data: need a list')

    def setSaveResults(self, toSave):
        if isinstance(toSave, int):
            self.__saveResults = toSave
        else:
            print('Not quite my type of data: need a int')
            raise Exception('Not quite my type of data: need an int')

    def getSaveResults(self):
        return self.__saveResults

    def setReportFiles(self, reports):
        if isinstance(reports, list):
            self.__reportFiles = reports
        else:
            print('Not quite my type of data: need a list')
            raise Exception('Not quite my type of data: need a list')

    def addReportFile(self, report):
        try:
            self.__reportFiles.append(report)
        except TypeError:
            print('Not quite my type of data: need a TReport')