from __future__ import division #Import for calculate divide
from classes.fileClass import File #Import File Class
from classes.sequenceClass import Sequence #Import Sequence Class
from classes.excelClass import Excel #Import Excel Class
from Bio.Seq import Seq #Import Sequence BioPython
from Bio.Alphabet import generic_dna

############################################################################################
#Motif class                                                                               #
#In this class we add motif file to motif list                                             #
#You can print motifs, and get number of motifs in list                                    #
#We can get count repeated motifs with Overlap in each sequence by bioPython library       #
#Also we calculate sum of n-mers motifs in each sequnce for calculation frequency of motifs#
############################################################################################

class Motif:

    motifs = []
    numNmersMotifsDic = {}

    #Initial method
    def __init__(self, addr):
        seq = Sequence() #Create object from sequence
        self.sequences = seq.sequence(addr)

    #Print motifs
    def printMotif(self):
         print (self.motifs)

    #Save motifs in list
    def motifList(self):
        valueObj = Excel() #Create object from excel class
        self.motifs = valueObj.values

    def getLenMotif(self):
        print (len(self.motifs))

    #Calculate count of motifs in sequence with overlap in command mode
    def terminal_CountMotif(self):

        pattern = ''
        countMotifs = {}
        

        #Print length of motifs
        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)

            for j in range(1,len(self.motifs)):
                pattern = self.motifs[j]
                #Number of repeat pattern
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))
            print (countMotifs)
            
    #Calculate count of motifs in sequence with overlap in GUI mode
    def gui_CountMotif(self):

        #Import html.py library for create table
        import lib.HTML as html 

        pattern = ''
        countMotifsList = []
        
        HTMLFILE = 'htmlOutput/motifCount.html'
        f = open(HTMLFILE, 'w')
        
        t = html.Table(header_row = self.motifs)
        
        #Length of motifs
        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)
            countMotifs = []
            countMotifs.append('<b>'+str(i+1)+'</b>') #number of sequence in table

            for j in range(1,len(self.motifs)):
                pattern = self.motifs[j]
                #Number of repeat pattern
                countMotifs.append(my_dna.count_overlap(pattern))
            t.rows.append(countMotifs)
        
        htmlcode = str(t)
        f.write(htmlcode)
        f.write('<p>')
        print ('Done'+'-'*79)

    #Calculate number of n-mers motifs in sequence
    def numNmersMotifs(self):

        pattern = ''
        countMotifs = {}
        
        
        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)

            summ=[0]*5; #Define summ variable

            for j in range(1,len(self.motifs)):
                pattern = self.motifs[j]
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))

            for value in countMotifs.keys():
                if (len(value) == 1):
                    temp = countMotifs[value] #This is a list
                    summ[0] += temp[0]
                elif (len(value) == 2):
                    temp = countMotifs[value]
                    summ[1] += temp[0]                   
                elif (len(value) == 3):
                    temp = countMotifs[value]
                    summ[2] += temp[0]
                elif (len(value) == 4):
                    temp = countMotifs[value]
                    summ[3] += temp[0]
                elif (len(value) == 5):
                    temp = countMotifs[value]
                    summ[4] += temp[0]
            self.numNmersMotifsDic[i] = []
            self.numNmersMotifsDic[i].append(summ[0])
            self.numNmersMotifsDic[i].append(summ[1])
            self.numNmersMotifsDic[i].append(summ[2])
            self.numNmersMotifsDic[i].append(summ[3])
            self.numNmersMotifsDic[i].append(summ[4])

    #Calculate Frequency of motifs in sequence
    def terminal_FrequencyMotifs(self):
        pattern = ''
        countMotifs = {}

        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)
            print ('Sequence', i+1)
            
            for j in range(1,len(self.motifs)):
                pattern = self.motifs[j]
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))

            for key, value in countMotifs.items():
                if (len(key) == 1):
                    temp = value[0] #This is a list
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][0])*100) #Caculate Percentage and show 2 decimal
                    print ('Frequency of', key, '==>', percentage, '%')
                elif (len(key) == 2):
                    temp = value[0]
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][1])*100)
                    print ('Frequency of', key, '==>', percentage, '%')
                elif (len(key) == 3):
                    temp = value[0]
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][2])*100)
                    print ('Frequency of', key, '==>', percentage, '%')
                elif (len(key) == 4):
                    temp = value[0]
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][3])*100)
                    print ('Frequency of', key, '==>', percentage, '%')
                elif (len(key) == 5):
                    temp = value[0]
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][4])*100)
                    print ('Frequency of', key, '==>', percentage,'%')
                
    #Calculate Frequency of motifs in sequence in GUI mode
    def gui_FrequencyMotifs(self):

        #Import html.py library for create table
        import lib.HTML as html

        pattern = ''
        countMotifs={}
        percentage = ''
        
        HTMLFILE = 'htmlOutput/motifFrequency.html'
        f = open(HTMLFILE, 'w')
        
        t = html.Table(header_row = self.motifs)
 
        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)
            frequencyMotifsList = []
            frequencyMotifsList.append('<b>'+str(i+1)+'</b>') #number of sequence in table
            
            for j in range(1,len(self.motifs)):
                pattern = self.motifs[j]
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))

            for key, value in countMotifs.items():
                if (len(key) == 1):
                    temp = value[0] #This is a list
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][0])*100)
                    percentage = str(percentage)+'%'
                    frequencyMotifsList.append(percentage)

                elif (len(key) == 2):
                    temp = value[0]
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][1])*100)
                    percentage = str(percentage)+'%'
                    frequencyMotifsList.append(percentage)

                elif (len(key) == 3):
                    temp = value[0]
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][2])*100)
                    percentage = str(percentage)+'%'
                    frequencyMotifsList.append(percentage)

                elif (len(key) == 4):
                    temp = value[0]
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][3])*100)
                    percentage = str(percentage)+'%'
                    frequencyMotifsList.append(percentage)

                elif (len(key) == 5):
                    temp = value[0]
                    percentage = '%.2f' % ((temp/self.numNmersMotifsDic[i][4])*100)
                    percentage = str(percentage)+'%'
                    frequencyMotifsList.append(percentage)


            t.rows.append(frequencyMotifsList)
        
        htmlcode = str(t)
        f.write(htmlcode)
        f.write('<p>')
        print ('Done'+'-'*79)
