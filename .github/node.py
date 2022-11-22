class Node:

    def __init__(self, cargo, tree, root = None, direita = None, esquerda = None ):
        self.cargo = cargo
        self.tree = tree
        self.root = root
        self.direita = direita
        self.esquerda = esquerda

    def setDireita(self, direita):
        self.direita = direita

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda
    
    def __str__(self):
     return str(self.cargo)
        
