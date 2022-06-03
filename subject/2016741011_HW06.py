import random
from timeit import default_timer as timer

class Node :
    def __init__(self, data) :
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = "Red"
        

class red_black_tree :
    def __init__(self) :
        self.root = None;
        self.inserted_node = None
        
    def find(self, data):
        return self._find_data(self.root, data)
    
    def _find_data(self, root, data) :
        if root is None or root.data == data :
            return root
        elif root.data >= data :
            return self._find_data(root.left, data)
        elif root.data < data :
            return self._find_data(root.right, data)
        
    def insert(self, data):
        self.root = self._insert_node(self.root, data, None)
        self._balancing(self.inserted_node)
        return
    
    def _insert_node(self, cur, data, parent) :
        if cur is None :
            cur = Node(data)
            cur.parent = parent
            self.inserted_node = cur
            
        else :
            if data < cur.data :
                cur.left = self._insert_node(cur.left, data, cur)
            elif data > cur.data :
                cur.right = self._insert_node(cur.right, data, cur)
                
        return cur
    
    def _balancing(self, node):
        P = node.parent
        if P is None :
            node.color = "Black"
            
        else :
            if P.color == "Red" :
                G = P.parent
                U = None
                if G.left == P :
                    U = G.right
                elif G.right == P :
                    U = G.left
                    
                if U is not None and U.color == "Red" :
                    P.color, U.color = "Black", "Black"
                    G.color = "Red"
                    
                    self._balancing(G)
                    
                else :
                    if P == G. left and P.left == node:
                        G.color, P.color = P.color, G.color
                        self._right_rotate(G)
                        
                    elif P == G.left and P.right == node :
                        self._left_rotate(P)
                        G.color, node.color = node.color, G.color
                        self._right_rotate(G)
                        
                    elif P == G.right and P.right == node:
                        G.color, P.color = P.color, G.color
                        self._left_rotate(G)
                        
                    elif P == G.right and P.left == node :
                        self._right_rotate(P)
                        G.color, node.color = node.color, G.color
                        self._left_rotate(G)
                        
                        
    def delete(self, data) :
        node = self._get_delete_node(self.root, data)
        
        if node is None:
            return False
        self._delete_node(node)
        return True
    
    def _get_delete_node(self, node, data):
        if node.data > data :
            return self._get_delete_node(node.left, data)
        elif node.data < data :
            return self._get_delete_node(node.right, data)
        elif node.data == data :
            left = node.left
            right = node.right
            
            if left is not None and right is not None :
                min_successor = self._find_min_successor(node.right)
                node.data, min_successor.data = min_successor.data, node.data
                return min_successor
            
            else :
                return node
            
    def _delete_node(self, V) :
        C, S = None, None 
        P = V.parent
        
        if V.left is not None :
            C = V.left
        elif V.right is not None :
            C = V.right
        if P is None :
            self.root = None
            return
        elif V == P.left :
            S = P.right
        elif V == P.right :
            S = P.left
        if C is None :
            C = Node(None)
            C.parent = V
            C.color = "Black"
        if V.color == "Red" or C.color == "Red":
            if P is None:
                self.root = V
            else:
                if C.data is not None:
                    C.parent = P
                    C.color = "Black"
                    if P.left == V:
                        P.left = C
                    elif P.right == V:
                        P.right = C
                elif C.data is None:
                    if P.left == V:
                        P.left = None
                    elif P.right == V:
                        P.right = None
                V = C

        elif V.color == "Black" and C.color == "Black":
            C.parent = P
            if V == P.left:
                if C.data is None:
                    P.left = None
                else:
                    P.left = C
            elif V == P.right:
                if C.data is None:
                    P.right = None
                else:
                    P.right = C
            V = C
            V.color = "BBlack"
            if P is None:
                V.color = "Black"
                self.root = V
            else:
                self._delete_balancing(V, P, S)

    def _delete_balancing(self, V, P, S):
        S_l, S_r = S.left, S.right
        if S_l is None:
            S_l = Node(None)
            S_l.parent = S
            S_l.color = "Black"
        if S_r is None:
            S_r = Node(None)
            S_r.parent = S
            S_r.color = "Black"
        if S.color == "Black" and (S_l.color == "Red" or S_r.color == "Red"):
            if S == P.left and S_l.color == "Red":
                S_l.color = "Black"
                self._right_rotate(P)
            elif S == P.left and S_r.color == "Red":
                S_r.color = "Black"
                self._left_rotate(S)
                self._right_rotate(P)
            elif S == P.right and S_r.color == "Red":
                S_r.color = "Black"
                self._left_rotate(P)
            elif S == P.right and S_l.color == "Red":
                S_l.color = "Black"
                self._right_rotate(S)
                self._left_rotate(P)
        elif S.color == "Black" and S_l.color == S_r.color and S_l.color == "Black":
            V.color = "Black"
            if P.color == "Red":
                P.color = "Black"
                return
            else:
                P.color = "BBlack"
                S.color = "Red"
                PP = P.parent
                if PP and P == PP.left:
                    S = PP.right
                elif PP and P == PP.right:
                    S = PP.left
                if PP is None:
                    S = None
                self._delete_balancing(P, PP, S)
        elif S.color == "Red":
            S.color, P.color = P.color, S.color
            if S == P.left:
                self._right_rotate(P)
            elif S == P.right:
                self._left_rotate(P)
            self._delete_balancing(V, P, S)

    def _find_min_successor(self, node):
        if node.left is None:
            return node
        else:
            return self._find_min_successor(node.left)

    def _left_rotate(self, node):
        c = node.right
        p = node.parent

        if c.left is not None:
            c.left.parent = node

        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        if p is None:
            self.root = c
        elif p is not None:
            if p.left == node:
                p.left = c
            elif p.right == node:
                p.right = c

    def _right_rotate(self, node):
        c = node.left
        p = node.parent

        if c.right is not None:
            c.right.parent = node

        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p
        if p is None:
            self.root = c
        elif p is not None:
            if p.left == node:
                p.left = c
            elif p.right == node:
                p.right = c

def check(node):
    if node.left is not None:
        check(node.left)
    if node.parent != None:
        print(f'key: {node.data}, parent: {node.parent.data}, color: {node.color}')
    else:
        print(f'key: {node.data}, root: {node.parent}, color: {node.color}')
    if node.right is not None:
        check(node.right)
        



x = random.sample(range(5000), 1000)
value = x[800]

tree = red_black_tree()
for i in x :
    tree.insert(i)

start = timer()
found = tree.find(value)
print(timer() - start)

check(tree.root)

if found is not None :
    print('value', value, 'found', found.data)
    print(True if found.data == value else False)
    