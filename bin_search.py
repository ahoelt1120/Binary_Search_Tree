"""
Name: Amadnda Hoelting
Title: Binary Search Tree
"""
class Node(object):
    """Node object for binary search tree

            Represents a node in a binary search tree. Has all attributes that a node in
            a binary search tree would need (parent, left child, right child,and node data).

            Attributes
            ----------
            parent: Node
                Parent of the node
            left: Node
                Left of the node
            right: Node
                Right of the node
            data: Node
                Data of the node
            """
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """Binary search tree

        Supports most standard binary search tree operations (insert, traverse, delete).
        Can be used for building a priority queue or heapsort. The underlying implementation uses
        node objects to represent data in the tree. When initialized, Tree creates a new variable
        root that is set to None.

        Attributes
        ----------
        root: Node
            Root node of the tree

        Methods
        -------
        print(self):
            Print the data of all nodes in order
        __print(self, curr_node):
            Recursively print a subtree (in order), rooted at curr_node
        insert(self, data):
            Find the right spot in the tree for the new node and insert it
        min(self):
            Returns the minimum value held in the tree and returns None if the tree is empty
        max(self):
            Returns the maximum value held in the tree and returns None if the tree is empty
        __find_node(self, data):
            Returns the node with that particular data value else returns None
        contains(self, data):
            Return True of node containing data is present in the tree
        __iter__(self):
            Iterate over the nodes with inorder traversal using a for loop
        inorder(self):
            Traverse through the tree in order
        preorder(self):
            Traverse through the tree preorder
        postorder(self):
            Traverse through the tree postorder
        __traverse(self, curr_node, traversal_type)):
            Yield data of the correct nodes
        find_successor(self, data):
            Find the successor node of the data
        delete(self, data):
            Find the node to delete in the tree
        """
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        '''Print the data of all nodes in order.'''
        self.__print(self.root)


    def __print(self, curr_node):
        ''' Recursively print a subtree (in order), rooted at curr_node.'''
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)


    def insert(self, data):
        ''' Find the right spot in the tree for the new node
        and insert it.'''
        new_node = Node(data)
        comp = self.root # node being compared with new_node
        par = None # Will be parent of z
        while comp != None:
            # Descending until reaching a leaf
            par = comp
            if new_node.data < comp.data:
                comp = comp.left
            else:
                comp = comp.right
        new_node.parent = par
        if par == None:
            # Inserting new_node with parent par
            self.root = new_node # Tree was empty
        elif new_node.data < par.data:
            par.left = new_node
        else:
            par.right = new_node



    def min(self):
        '''Returns the minimum value held in the tree
        and returns None if the tree is empty.'''
        if self.root == None:
            return self.root
        else:
            cur = self.root
            while cur.left != None:
                cur = cur.left
            return cur.data



    def max(self):
        '''Returns the maximum value held in the tree
        and returns None if the tree is empty.'''
        if self.root == None:
            return self.root
        else:
            cur = self.root
            while cur.right != None:
                cur = cur.right
            return cur.data

    def __find_node(self, data):
        '''Returns the node with that particular data value else returns None.'''
        if self.root == None:
            return None
        cur = self.root
        while cur != None and data != cur.data:
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return cur


    def contains(self, data):
        '''Return True of node containing data is present in the tree.'''
        tree_data = self.__find_node(data)
        if tree_data == None:
            return False
        else:
            return True

    def __iter__(self):
        '''Iterate over the nodes with inorder traversal using a for loop.
        Yield keyword similar to return, but yield returns values while still running function (doesn't terminate execution).'''
        return self.inorder()

    def inorder(self):
        '''Traverse through the tree in order.'''
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        '''Traverse through the tree preorder.'''
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        '''Traverse through the tree postorder.'''
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        '''Yield data of the correct nodes.'''

        if curr_node == None:
            return

        # Need to yield curr_node here for preorder
        if traversal_type == self.PREORDER:
            yield curr_node.data

        if curr_node.left != None:
            yield from self.__traverse(curr_node.left, traversal_type)

        # Need to yield curr_node here for in order
        if traversal_type == self.INORDER:
            yield curr_node.data

        if curr_node.right != None:
            yield from self.__traverse(curr_node.right, traversal_type)

        # Need to yield curr_node here for post order
        if traversal_type == self.POSTORDER:
            yield curr_node.data


    def find_successor(self, data):
        '''Find the successor node of the data.'''
        if not self.contains(data):
            raise KeyError

        curr = self.__find_node(data)

        if curr.right != None:
            # Finding leftmost node in the right subtree
            x = curr.right
            next = curr.right.left
            while next != None:
                x = next
                next = next.left
            return x
        else:
            # Y is the lowest ancestor or x
            y = curr.parent
            while y != None and curr == y.right:
                curr = y
                y = y.parent
            return y




    def delete(self, data):
        '''Find the node to delete in the tree.'''

        if not self.contains(data):
            raise KeyError

        curr = self.__find_node(data)

        if curr.right == None and curr.left ==None:
            # Replace curr with None
            if curr.parent == None:
                self.root = None
            elif curr.data < curr.parent.data:
                curr.parent.left = None
            elif curr.data > curr.parent.data:
                curr.parent.right = None

        elif curr.left != None and curr.right == None:
            # Replace curr with curr.left
            if curr.parent == None:
                self.root = curr.left
                curr.left.parent = None
            elif curr.left.data < curr.parent.data:
                curr.parent.left = curr.left
            elif curr.left.data > curr.parent.data:
                curr.parent.right = curr.left
            curr.parent = curr.left
        elif curr.right != None and curr.left == None:
            # Replace curr with curr.right
            if curr.parent == None:
                self.root = curr.right
                curr.right.parent = None
            elif curr.right.data < curr.parent.data:
                curr.parent.left = curr.right
            elif curr.right.data > curr.parent.data:
                curr.parent.right = curr.right
        else:
            s = self.find_successor(data)

            # Testing if y is farther down the tree
            if s != curr.right:
                if s.parent == None:
                    self.root = s.right
                elif s == s.parent.left:
                    s.parent.left = s.right
                else:
                    s.parent.right = s.right
                if s.right != None:
                    s.right.parent = s.parent
                s.right = curr.right
                s.right.parent = s
            # Replace curr by its successor s
            if curr.parent == None:
                self.root = s
            elif curr == curr.parent.left:
                curr.parent.left = s
            else:
                curr.parent.right = s
            if s != None:
                s.parent = curr.parent
            # Give cur's child to s which had no left child
            s.left = curr.left
            s.left.parent = s









