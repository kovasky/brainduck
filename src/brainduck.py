from tree import Tree
import sys

class BrainDuck:
    def __init__(self):
        self.errorFlag = False
        self.alphabet = ['>', '<', '+', '-', '.', ',', '[', ']']
        self.listOfPrefixes = []
        self.tree = None

    def readFile(self,fileLocation):
        with open(fileLocation) as file:
            for line in file:
                for char in line:
                    if char in self.alphabet: #ignore all other char not in alphabet
                        self.listOfPrefixes.append(char)

        self.listOfPrefixes.append(None)

    def consume(self):
        val = self.listOfPrefixes[0]
        self.listOfPrefixes = self.listOfPrefixes[1:]
        return Tree(val)

    def loop(self):
        val = self.consume()
        while self.listOfPrefixes [0] != ']'  and self.listOfPrefixes[0] != None:
            val.add_child(self.operation())
        if self.listOfPrefixes [0] == ']':
            val.add_child(self.consume())
        else:
            self.errorFlag = True
        return val

    def operation(self):
        if self.listOfPrefixes[0] == ']':
            self.errorFlag = True
            return None
        elif self.listOfPrefixes[0] == '[':
            return self.loop()
        elif self.listOfPrefixes[0] == None:
            return None
        else:
            return self.consume()

    def parse(self,fileLocation):
        self.tree = Tree()
        self.readFile(fileLocation)
        while self.listOfPrefixes[0] is not None:
            val = self.operation()
            if val != None:
                self.tree.add_child(val)
            elif self.errorFlag == True:
                break
        if self.errorFlag == True:
            print('Error Parsing')
            sys.exit(-1) 
