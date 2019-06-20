"""
相关练习题
1. 第226题 翻转二叉树 https://leetcode.com/problems/invert-binary-tree/
2. 第104题 求二叉树的最大深度 https://leetcode.com/problems/maximum-depth-of-binary-tree/
3. 第112题 找一个路径上节点的和等于给定值 https://leetcode.com/problems/path-sum/
4. 第144题 二叉树先序遍历 https://leetcode.com/problems/binary-tree-preorder-traversal/
5. 第94题 二叉树中序遍历 https://leetcode.com/problems/binary-tree-inorder-traversal/
6. 第145题 二叉树后序遍历 https://leetcode.com/problems/binary-tree-postorder-traversal/
7. 第199题 层序遍历实现树的左右视图 https://leetcode.com/problems/binary-tree-right-side-view/
8. 第889题 根据树的先序和后序遍历返回完整的树 https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from_list(cls, arr):
        node_dict = {}
        for item in arr:
            data = item["data"]
            node_dict[data] = Node(data)
        for item in arr:
            data = item["data"]
            node = node_dict[data]
            if item["is_root"]:
                root = node
            node.left = node_dict.get(item["left"])
            node.right = node_dict.get(item["right"])
        return cls(root)

    # 先序遍历
    def preorder_trav(self, subtree, callback=print):
        if subtree is not None:
            if callback == print:
                callback(subtree.data, end=" ")
            else:
                callback(subtree.data)
            self.preorder_trav(subtree.left, callback)
            self.preorder_trav(subtree.right, callback)

    # 中序遍历
    def inorder_trav(self, subtree):
        if subtree is not None:
            self.inorder_trav(subtree.left)
            print(subtree.data, end=" ")
            self.inorder_trav(subtree.right)

    # 后序遍历
    def postorder_trav(self, subtree):
        if subtree is not None:
            self.postorder_trav(subtree.left)
            self.postorder_trav(subtree.right)
            print(subtree.data, end=" ")

    # 层序遍历
    def layer_trav(self, subtree):
        current_nodes = [subtree]  # 当前层
        next_nodes = []  # 下一层
        while current_nodes or next_nodes:
            for node in current_nodes:
                print(node.data, end=" ")
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            current_nodes = next_nodes
            next_nodes = []

    # 翻转二叉树
    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


node_list = [
    {"data": "A", "left": "B", "right": "C", "is_root": True},
    {"data": "B", "left": "D", "right": "E", "is_root": False},
    {"data": "D", "left": None, "right": None, "is_root": False},
    {"data": "E", "left": "H", "right": None, "is_root": False},
    {"data": "H", "left": None, "right": None, "is_root": False},
    {"data": "C", "left": "F", "right": "G", "is_root": False},
    {"data": "F", "left": None, "right": None, "is_root": False},
    {"data": "G", "left": "I", "right": "J", "is_root": False},
    {"data": "I", "left": None, "right": None, "is_root": False},
    {"data": "J", "left": None, "right": None, "is_root": False},
]


def test_btree():
    btree = BinaryTree.build_from_list(node_list)
    btree.iter_result = []
    btree.preorder_trav(btree.root, btree.iter_result.append)
    assert btree.iter_result == ["A", "B", "D", "E", "H", "C", "F", "G", "I", "J"]

    btree.reverse_res = []
    btree.reverse(btree.root)
    btree.preorder_trav(btree.root, btree.reverse_res.append)
    assert btree.reverse_res == ["A", "C", "G", "J", "I", "F", "B", "E", "H", "D"]


if __name__ == "__main__":
    test_btree()
    btree = BinaryTree.build_from_list(node_list)
    print("====先序遍历=====")
    btree.preorder_trav(btree.root)
    print()

    print("====中序遍历=====")
    btree.inorder_trav(btree.root)
    print()

    print("====后序遍历=====")
    btree.postorder_trav(btree.root)
    print()

    print("====层序遍历=====")
    btree.layer_trav(btree.root)
    print()

    btree.reverse(btree.root)
    print("====反转之后的结果=====")
    btree.preorder_trav(btree.root)
