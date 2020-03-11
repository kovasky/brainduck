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

    def loopParse(self):
        val = self.consume()
        while self.listOfPrefixes [0] != ']' and self.listOfPrefixes[0] != None:
            val.addChild(self.operation())
        if self.listOfPrefixes [0] == ']':
            val.addChild(self.consume())
        else:
            self.errorFlag = True
        return val

    def operation(self):
        if self.listOfPrefixes[0] == ']':
            self.errorFlag = True
            return None
        elif self.listOfPrefixes[0] == '[':
            return self.loopParse()
        elif self.listOfPrefixes[0] == None:
            return None
        else:
            return self.consume()

    def parse(self,fileLocation):
        self.errorFlag = False
        self.listOfPrefixes = []
        self.tree = Tree()
        self.readFile(fileLocation)
        while self.listOfPrefixes[0] is not None:
            val = self.operation()
            if val != None:
                self.tree.addChild(val)
            elif self.errorFlag == True:
                break
        if self.errorFlag == True:
            print('Parsing Error')
            sys.exit(-1) 

    def buildMap(self,operations):
        val = []
        loopMap = {}
        for index,operation in enumerate(operations):
            if operation == '[':
                val.append(index)
            if operation == ']':
                beginning = val.pop()
                loopMap[beginning] = index
                loopMap[index] = beginning
        return loopMap
        
    def run(self,fileLocation):
        self.parse(fileLocation)
        tape = [0]
        cellPointer = 0
        operations = self.tree.preOrderValues()[1:]
        loopMap = self.buildMap(operations)
        codePointer = 0

        while(codePointer < len(operations)):
            if operations[codePointer] == '<':
                if cellPointer - 1 >= 0: 
                    cellPointer = cellPointer - 1
            elif operations[codePointer] == '>':
                cellPointer = cellPointer + 1
                if len(tape) == (cellPointer):
                    tape.append(0)
            elif operations[codePointer] == '-': 
                if tape[cellPointer] - 1 < 0:
                    tape[cellPointer] = 255
                else:
                    tape[cellPointer] = tape[cellPointer] - 1
            elif operations[codePointer] == '+':
                if tape[cellPointer] + 1 > 255:
                    tape[cellPointer] = 0
                else:
                    tape[cellPointer] = tape[cellPointer] + 1
            elif operations[codePointer] == '.':
                print(chr(tape[cellPointer]),end="")
            elif operations[codePointer] == ',':
                tape[cellPointer] = int(input())
            elif operations[codePointer] == '[':
                if tape[cellPointer] == 0:
                    codePointer = loopMap[codePointer]
            elif operations[codePointer] == ']':
                if tape[cellPointer] != 0:
                    codePointer = loopMap[codePointer]
            codePointer = codePointer + 1
        print("\n")
