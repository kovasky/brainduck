from itertools import chain

class Tree:
    def __init__(self,name='root'):
        self.name = name
        self.children = []

    def __repr__(self):
        return self.name

    def __str__(self,level=0):
        ret = "\t"*level+repr(self.name)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __iter__(self):
        return tree_iter(self)

    def add_child(self,node):
        self.children.append(node)

    def preorder_values(self):
        return tree_iter(self)

class tree_iter:
    def __init__(self, the_tree):
        self._work_queue = [ the_tree ]

    def __next__(self):
        while len(self._work_queue) > 0:
            subtree = self._work_queue.pop(0)# Get first item            
            if subtree == None:
                pass
            else:
                self._work_queue[0:0]=  subtree.children
                return subtree.name
        raise StopIteration
    
    def __iter__(self): 
        return self
