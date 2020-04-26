class Position(object):
    def __init__(self, elemento, pai = None, filho_esquerdo = None, filho_direito = None):
        self.elemento = elemento
        self.pai = pai
        self .filho_esquerdo = filho_esquerdo
        self.filho_direito = filho_direito
    
class LinkedBinaryTree():

    def __init__(self):
        
        self.tamanho = 0
        self.raiz = None

    def getraiz(self):
        return self.raiz
    def setraiz(self, elemento):
        if (self.raiz.elemento = 0):
            self.root.elemento = elemento
    
    def gettamanho(self):
        return self.tamanho
    def settamanho(self, tamanho):
        self.tamanho = tamanho

    def isEmpty(self):
        if (self.tamanho == None):
            return True
        else:
            False

    def isInternal(self, no_cego):
        if not(no_cego.filho_direito is None):
            return True
        elif not(no_cego.filho_esquerdo is None):
            return True
        else:
            return False

    def isExternal(self, no_cego):
        if(no_cego.filho_direito is None):
            return True
        elif(no_cego.filho_esquerdo is None):
            return True
        else:
            return False

    def isRoot(self, no_cego):
        if(no_cego.pai == None):
            return True
        else:
            return False
    
    def hasLeft(self, no_cego):
        if not(no_cego.filho_esquerdo is None):
            return True
        else:
            return False

    def hasRight(self, no_cego):
        if not(no_cego.filho_direito is None):
            return True
        else:
            return False

    def left(self, no_cego):
        if(hasLeft(no_cego) is True):
            return no_cego.filho_esquerdo
        else:
            return None

    def right(self, no_cego):
        if(hasRight(no_cego) is True):
            return no_cego.filho_direito
        else:
            return None

    def pai(self, no_cego):
        if not(no_cego.pai is None):
            return no_cego.pai
        else:
            return None

    # # função add + insertRight + insertLeft
    # def add(self, no_cego):
    #     if (no_cego.pai < self.pai):
    #         if(self.filho_esquerdo is None):
    #             self.filho_esquerdo = no_cego
    #         else:
    #             self.filho_esquerdo.add(no_cego)
        
    #     else:
    #         if(self.filho_direito is None):
    #             self.filho_direito = no_cego
    #         else:
    #             self.filho_direito.add(no_cego)

    def addRaiz(self, element):
        self.setraiz(elemento)
        self.tamanho = self.tamanho + 1

    def insertRight(self, no_cego, elemento):
        no_cego.filho_direito = Position(elemento)
        self.tamanho = self.tamanho + 1

    def insertLeft(self, no_cego, elemento):
        no_cego.filho_esquerdo = Position(elemento)
        self.tamanho = self.tamanho + 1 

    def toStringPreOrder(self, visit, order = "Pre"):
        if(order == "Pre"):
            visit(self)
        elif not(self.filho_esquerdo is None):
            self.filho_esquerdo.toStringPreOrder(visit, order)
        
    def toStringPosOrder(self, visit, order = "Pre"):
        if(order == "Pos"):
            visit(self)

    # def gett(self ,elemento):
    #     if (self == elemento):
    #         return self
        
    #     no_cego = self.filho_esquerdo if elemento < self.elemento else self.filho_direito
    #     if no_cego is not None:
    #         return no_cego.get(elemento)


#   def depth(self, no_cego)

#   Não consegui fazer
    
if __name__ == "__main__":

    arvore = LinkedBinaryTree()

    arvore.addRaiz(1)
    arvore.insertRight(arvore.raiz, 2)
    arvore.insertLeft(arvore.raiz, 3)
    arvore.insertLeft(arvore.raiz.filho_esquerdo, 4)
    arvore.insertLeft(arvore.raiz.filho_esquerdo, 5)
    arvore.insertRight(arvore.raiz.filho_direito, 6)
    arvore.insertLeft(arvore.raiz.filho_esquerdo.filho_direito, 7)

    print(arvore.toStringPreOrder)
    print(arvore.toStringPosOrder)




    
    

