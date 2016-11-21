
import collections
import random

class WordCount:
    def __init__(self,):
  
        self.words = collections.OrderedDict() #need order to choose weighted random
        self.count=0 #combined count of all words
        
    def addWord(self,toAdd):
        try:
            self.words[toAdd]+=1
        except KeyError: #triggers if word has not been recorded yet
            self.words[toAdd]=1
        self.count+=1
        
    def getCount(self,toGet): #this function is unused
        try:
            return self.words[toGet]
        except KeyError:
            return 0
        
    def getWord(self):
        r = random.uniform(0, self.count) #random int over cumalative count
        upto = 0
        for c in self.words.keys(): #loop subtracts weight to find which word cumulative random lies on
            if upto + self.words[c] >=r:
                return c
            upto+=self.words[c]
        assert false #loop should not get here

    def uniqueCount(self):
        return len(self.words)


    



           
