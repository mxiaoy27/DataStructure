class Node(object):
    def __init__(self, item):
        self.elem = item
        self.l_child = None
        self.r_child = None
        self.visit = False


class BTree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.l_child is None:
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)

            if cur_node.r_child is None:
                cur_node.r_child = node
                return
            else:
                queue.append(cur_node.r_child)

    def bread_travel(self):
        if self.root is Node:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end="")
            if cur_node.l_child is not None:
                queue.append(cur_node.l_child)
            if cur_node.r_child is not None:
                queue.append(cur_node.r_child)

    """递归先序"""

    def pre_travel_recur(self, node):
        if node is None:
            return
        print(node.elem, end="")
        self.pre_travel_recur(node.l_child)
        self.pre_travel_recur(node.r_child)

    """先序非递归"""

    def pre_travel(self):
        if self.root is None:
            return
        stack = [self.root]

        while stack:
            cur_node = stack.pop()
            print(cur_node.elem, end="")
            if cur_node.r_child is not None:
                stack.append(cur_node.r_child)
            if cur_node.l_child is not None:
                stack.append(cur_node.l_child)

    """递归中序"""

    def mid_travel_recur(self, node):
        if node is None:
            return
        self.mid_travel_recur(node.l_child)
        print(node.elem, end="")
        self.mid_travel_recur(node.r_child)

    """非递归中序0"""

    def mid_travel_0(self):
        if self.root is None:
            return
        stack = []
        cur_node = self.root
        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.l_child

            if stack:
                cur_node = stack.pop()
                print(cur_node.elem, end="")
                cur_node = cur_node.r_child

    """非递归中序1"""

    def mid_travel_1(self):
        if self.root is None:
            return
        stack = []
        cur_node = self.root
        while stack or cur_node:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.l_child
            else:
                cur_node = stack.pop()
                print(cur_node.elem, end="")
                cur_node = cur_node.r_child

    """递归后续"""

    def post_travel_recur(self, node):
        if node is None:
            return
        self.post_travel_recur(node.l_child)
        self.post_travel_recur(node.r_child)
        print(node.elem, end="")

    """非递归后续"""

    def post_travel(self):
        if self.root is None:
            return

        stack = []
        cur_node = self.root

        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node.visit = False
                cur_node = cur_node.l_child
            if stack:
                temp = stack[-1]
                if temp.visit is False:
                    temp.visit = True
                    cur_node = temp.r_child
                else:
                    print(temp.elem, end="")
                    stack.pop()


if __name__ == "__main__":
    tree = BTree()
    for i in range(10):
        tree.add(i)

    print("层序：")
    tree.bread_travel()
    print("")
    print(" ")
    print("先序：")
    tree.pre_travel_recur(tree.root)
    print("")
    tree.pre_travel()
    print("")
    print(" ")
    print("中序：")
    tree.mid_travel_recur(tree.root)
    print("")
    tree.mid_travel_1()
    print("")
    tree.mid_travel_0()
    print("")
    print(" ")
    print("后序：")
    tree.post_travel_recur(tree.root)
    print("")
    tree.post_travel()
    print("")
