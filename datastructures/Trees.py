class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root is None:
        return
    stack = []

    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        print(node.data, end=" ")

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    """
    if root is not None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
    """


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# using queue (BFS)
def levelorder(root):
    if root is None:
        return
    queue = []

    # append the root node
    queue.append(root)
    while len(queue) > 0:

        print(queue[0].data, end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))


def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def deleteNode(root, data):
    if root is None:
        return root

    # if data is less than root node value then,it lies in the left subtree
    if data < root.data:
        root.left = deleteNode(root.left, data)

    # if data is greater than root node value then,it lies in the right subtree
    elif data > root.data:
        root.right = deleteNode(root.right, data)

    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:Get the inorder successor of the node
        temp = minValueNode(root.right)

        # copy the inorder successor's content into this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)

    return root


def searchtree(root, data):
    if root == None:
        return False
    if root.data == data:
        return True

    leftTree = searchtree(root.left, data)
    if leftTree:
        return True

    rightTree = searchtree(root.right, data)

    return rightTree


if __name__ == "__main__":

    r = Node(50)

    insert(r, Node(30))
    insert(r, Node(20))
    insert(r, Node(40))
    insert(r, Node(70))
    insert(r, Node(60))
    insert(r, Node(80))

    print("Level Order")
    levelorder(r)

    print("\nPre Order")
    preorder(r)
    # print('Height of the tree is {}'.format(height(r)))

    # r = deleteNode(r,20)
    # inorder(r)

    # r = deleteNode(r,30)
    # inorder(r)

    # print("\n")
    # r = deleteNode(r,50)
    # inorder(r)

    if searchtree(r, 70):
        print("\nYES")
    else:
        print("\nNO")
