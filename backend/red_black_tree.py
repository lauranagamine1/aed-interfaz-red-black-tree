class Node:
    def __init__(self, key):
        self.key = key
        self.color = 'red'
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)  # Nodo NULO (tendría un valor por defecto)
        self.TNULL.color = 'black'
        self.root = self.TNULL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotate_left(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.key = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 'black'
            return

        if node.parent.parent == None:
            return

        self.insert_fixup(node)

    def transplant(self, u, v):
        """Reemplaza el subárbol con raíz en u por el subárbol con raíz en v"""
        if u.parent == None:
            self.root = v  # Si u es la raíz, entonces v se convierte en la nueva raíz
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fixup(self, x):
        """Repara el árbol después de la eliminación de un nodo"""
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':  # Caso 1: El hermano es rojo
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':  # Caso 2: El hermano es negro y ambos hijos son negros
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':  # Caso 3: El hermano es negro y el hijo derecho es negro
                        w.left.color = 'black'
                        w.color = 'red'
                        self.rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'black'

    def delete(self, key):
        """Elimina el nodo con el valor `key` del árbol"""
        z = self.root
        while z != self.TNULL:
            if z.key == key:
                break
            elif key < z.key:
                z = z.left
            else:
                z = z.right
        
        if z == self.TNULL:  # Si el nodo no existe
            print("El nodo con valor {} no fue encontrado.".format(key))
            return
        
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            self.delete_fixup(x)

    def minimum(self, node):
        """Devuelve el nodo con el valor mínimo en el subárbol de `node`"""
        while node.left != self.TNULL:
            node = node.left
        return node

    def clear(self):
        self.root = self.TNULL

    def inorder_helper(self, node):
        if node != self.TNULL:
            self.inorder_helper(node.left)
            print(node.key, end=" ")
            self.inorder_helper(node.right)

    def print_tree(self):
        self.inorder_helper(self.root)
        print()


# Test de la clase RedBlackTree
if __name__ == "__main__":
    rbt = RedBlackTree()

    # Insertar elementos en el árbol
    keys = [20, 15, 25, 10, 5, 1, 30, 1, 10]
    for key in keys:
        rbt.insert(key)

    # Imprimir los elementos en el árbol
    print("Árbol Red-Black (in-order):")
    rbt.print_tree()
