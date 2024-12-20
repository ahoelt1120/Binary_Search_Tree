"""
Name: Amanda Hoelting
Title: Unit Tests for Binary Search Tree Project
"""
import bin_search
import unittest

class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = bin_search.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")

    def test_unbalanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = bin_search.Tree()

        t.insert(7)
        t.insert(4)
        t.insert(8)
        t.insert(9)
        t.insert(1)
        t.insert(11)
        t.insert(2)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 7)
        self.assertEqual(t.root.left.data, 4)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.left.right.data, 2)
        self.assertEqual(t.root.right.data, 8)
        self.assertEqual(t.root.right.right.data, 9)
        self.assertEqual(t.root.right.right.right.data, 11)

        print("\n")




class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = bin_search.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = bin_search.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")

    def test_postorder_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = bin_search.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        postorder = [node for node in t.postorder()]


        print("postorder traversal")
        self.assertEqual(postorder, [1, 3, 2, 5, 7, 6, 4])
        print("\n")




class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = bin_search.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")

    def test_successor_after_delete(self):
        print("\n")
        print("successor function")
        tree_success = bin_search.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.delete(10)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.delete(6)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.delete(7)
        tree_success.insert(13)

        easy_success1 = tree_success.find_successor(8).data
        tough_success2 = tree_success.find_successor(1).data

        self.assertEqual(easy_success1, 13)
        self.assertEqual(tough_success2, 3)

        print("\n")

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = bin_search.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        with self.assertRaises(KeyError):
            tree_success.find_successor(1989).data

        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = bin_search.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]

        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

    def test_delete_while_inserting(self):
        print("\n")
        print("delete function")
        t = bin_search.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.delete(10)
        t.insert(6)
        t.insert(4)
        t.delete(8)
        t.insert(7)
        t.insert(14)
        t.delete(7)
        t.insert(13)



        l1 = [node for node in t]

        self.assertEqual(l1, [1, 3, 4, 6, 13, 14])

        print("\n")

    def test_delete_error(self):
        print("\n")
        print("delete function")
        t = bin_search.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.delete(10)
        t.insert(6)
        t.insert(4)
        t.delete(8)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        with self.assertRaises(KeyError):
            t.delete(25)

        print("\n")

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = bin_search.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

    def test_contains_with_deletions(self):
        print("\n")
        print("contains function")
        t = bin_search.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.delete(3)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.delete(7)
        t.insert(13)
        self.assertEqual(t.contains(7), False)
        self.assertEqual(t.contains(1), True)
        print("\n")

class T6_find_node(unittest.TestCase):

    def test_find_node(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = bin_search.Tree()
        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        found = t._Tree__find_node(5)
        self.assertEqual(found.data, 5)

        print("\n")



if __name__ == '__main__' :
    unittest.main()