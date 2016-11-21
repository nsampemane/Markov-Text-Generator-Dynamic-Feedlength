import random
import storage
class Chain:
        def __init__(self, filepath,fl=2):
                if fl< 2:
                        fl =2
                self.feedlength=fl
                self.database ={} #will store the markov chain
                self.file = open(filepath)
                self.words = self.file.read().split()
                self.createDatabase()
        def tokenizer(self):
                if len(self.words)<self.feedlength: #length of file insufficient
                        print("insufficent data")
                        return None;
                for i in range(len(self.words) - (self.feedlength)):
                        output = []
                        for k in range(self.feedlength+1):
                                output.append(self.words[i+k])
                        yield tuple(output)
        def createDatabase (self):
                for a in self.tokenizer():
                        outword = a[-1]
                        key =a[:-1]
                        try:#checks if word is already in database
                                self.database[key].addWord(outword)
                                
                        except KeyError:
                                wcount = storage.WordCount()
                                wcount.addWord(outword)
                                self.database[key] =wcount
        def gen (self,length=25):
                seed = random.choice(tuple(self.database.keys())) #choose a random two words to start from             
                head = seed[0]
                tail = seed[1:]
                output = []
                for i in range(length):
                        output.append(head)
                        nextword = self.database[(head,) + tail].getWord()
                        head = tail[0]
                        tail = tail[1:] + (nextword,)
                      
                for v in tail:
                        output.append(v)                
                return ' '.join(output)
        def getWord(self,key):
                return self.database[key].getWord()
        def diversity(self,key):
                try:
                        return self.database[key].uniqueCount()
                except KeyError:
                        return 0
        

class MultiChain:
        def __init__(self, filepath):
                self.chains = {}
                for i in (5,4,3,2): #5,4,3,2  as the input chain lengths
                        self.chains[i] = Chain(filepath,i)
        def gen(self,length=25):
                
                seed = random.choice(tuple(self.chains[5].database.keys())) #choose a random two words to start from                  
                output = list(seed)                
                for i in range(length):
                        if len(output) < 3:
                                feedlength = len(output)
                        else:
                                feedlength =5                        
                        
                        while length > 2:
                                try:
                                        totest = tuple(output[-feedlength:])
                                        if self.chains[length].diversity(totest)> 1:
                                                break
                                        length-=1
                                except KeyError:
                                        length-=1
                        previous = tuple(output[-feedlength:])
                        toadd = self.chains[feedlength].getWord(previous)
                        output.append(toadd)
                        
                return ' '.join(output)                        
                        
                        
                                
