from node import Node

class binary_tree:

  def adicionar(root, no, chave, esquerda, direita):
     if  root == None:
             root = no

      #direita
     elif root.chave < no.chave:
        if root.direita == None:
            root.direita = no
        else:
           adicionar(root.direita, no)

      #esquerda
        else:
          if root.esquerda is None:
            root.esquerda = no
          else:
            adicionar(root.esquerda, no)
          
  def total(tree):
      if tree == None : return 0
      return total(tree.left) + total(tree.right) + tree.cargo


  
  def Mostrar(self, tree):
    if self.left:
      self.left.Mostrar()
      print( self.tree),
    if self.right:
      self.right.Mostrar()
        
      
  def remover(self)