'''
Created on 02/03/2018

@author: Peter
'''

from TReport import TReport
from TProject import TProject
from Task import TTask
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.Qt import QFileDialog, QTextCursor
import time
import threading
import queue
import string

app = QtWidgets.QApplication([])
form = uic.loadUi("form.ui")



global q
q = queue.Queue()
global projecto
projecto = TProject()
global terraTask
terraTask = TTask()

def print_slow(strToPrint):
    for letter in strToPrint:
        #QtWidgets.QTextBrowser.text
        form.logWindow.moveCursor(QTextCursor.End)
        form.logWindow.insertPlainText(letter)
        time.sleep(.01)

def worker_1():
    while True:
        item = q.get()
        if item is None:
            break
        print_slow(item)
        q.task_done()


def import_prj():
    #QtWidgets.QLineEdit.setEnabled(True)
    try:
        threadTmp = threading.Thread(target=worker_1)
        threadTmp.start()
        form.prjLineEdit.setText(QFileDialog.getOpenFileName(None, 'Open TScan Prj file',
                                                             'U:\\Trabalho\\Ambisig\\REN\\02 - Las\\13 (10T_16-11M_17-11M&T)\\', "Prj files (*.prj)")[0])

        projecto.readFile(form.prjLineEdit.text())
        q.put("\nStorage: " + projecto.getStorageType() + "\n")
        q.put("Description: " + projecto.getDescription() + "\n")
        q.put("Tiles" + ": " + str(projecto.getTilesCount()) + "\n\n")

        form.taskButton.setEnabled(True)
        form.taskLineEdit.setEnabled(True)
        q.put(None)

    except:
        q.put("\n********************\nUnexpected error:" + str(sys.exc_info()[0]))
        print("Unexpected error:", sys.exc_info()[0])
        q.put(None)
        pass

def import_task():
    try:
        threadTmp = threading.Thread(target=worker_1)
        threadTmp.start()
        #form.taskLineEdit.setText(QFileDialog.getExistingDirectory(None, 'Select Folder', 'U:\\GitHub\Work\\Slave_Success V2\\Testes\\Reports\\'))
        form.taskLineEdit.setText(QFileDialog.getOpenFileName(None, 'Open TSlave Task file',
                                                             'U:\\GitHub\\Work\\Slave_Success V2\\Testes\\Reports',
                                                             "Tsk files (*.tsk)")[0])

        terraTask.readFile(form.taskLineEdit.text())
        q.put("[TerraSlave task]\n")
        q.put("Macro: " + terraTask.getMacroName() + "\n")
        q.put("Macro Location: " + terraTask.getMacroLocation() + "\n")
        q.put("Neighbours: " + str(terraTask.getneighBours()) + "\n")
        q.put("Prj: " + terraTask.getProjectName() + "\n")
        q.put("SaveResults: " + str(terraTask.getSaveResults()) + "\n")

        form.reportsButton.setEnabled(True)
        form.reportsLineEdit.setEnabled(True)
        q.put(None)
    except:
        q.put("\n********************\nUnexpected error:" + str(sys.exc_info()[0]))
        q.put(None)
        print("Unexpected error:", sys.exc_info()[0])
        pass

def importReports():
    try:
        threadTmp = threading.Thread(target=worker_1)
        threadTmp.start()

        reportFiles = QFileDialog.getOpenFileNames(None, "Import TSlave Report files",
                                                   'U:\\GitHub\\Work\\Slave_Success V2\\Testes\\Reports',
                                                   "Report files (*.txt)")
        form.reportsLineEdit.setText(str(len(reportFiles[0])) + " TSlave report files")
        tmpReport = TReport()
        for reportFile in reportFiles[0]:
            tmpReport.readFile(reportFile)
            terraTask.addReportFile(tmpReport)

        return
    except:
        q.put("\n********************\nUnexpected error:" + str(sys.exc_info()[0]))
        q.put(None)
        print("Unexpected error:", sys.exc_info()[0])
        pass

form.prjButton.clicked.connect(import_prj)
form.taskButton.clicked.connect(import_task)
form.reportsButton.clicked.connect(importReports)


form.show()
app.exec()



#newTask = TTask("C:\\terra64\\tslave\\reports\\20180220_154617.tsk")
#task = TTask("C:\\terra64\\tslave\\reports\\20180220_154617_000001.tx")
