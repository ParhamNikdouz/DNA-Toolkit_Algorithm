from classes.fileClass import File #Import File Class
from classes.sequenceClass import Sequence #Import Sequence Class
from classes.motifClass import Motif #Import Motif Class
from classes.excelClass import Excel #Import Excel Class

#Create object from file class
fileObj = File()
fastaPath = "/home/parham/Documents/Python/DNA-Toolkit/importFiles/ebola.fasta"
fileObj.openFile(fastaPath)
#fileObj.printFile()

seqObj = Sequence()
#seqObj.sequence(fastaPath)
#seqObj.printSequences()
#seqObj.getNumberOfSequences()

excel = Excel();
excelPath = "/home/parham/Documents/Python/DNA-Toolkit/importFiles/motif_count.xlsx"
excel.openExcel(excelPath)
#excel.printValues()
#excel.getNumberOfValues()

motifObj = Motif(fastaPath)
motifObj.motifList()
#motifObj.printMotif()
#motifObj.getLenMotif()
#motifObj.terminal_CountMotif()
#motifObj.gui_CountMotif()
#motifObj.numNmersMotifs()
#print(motifObj.numNmersMotifsDic)
#motifObj.terminal_FrequencyMotifs()
#motifObj.gui_FrequencyMotifs()
