class Node:
    def __init__(self,data,left=None,right = None):
        self.data=data
        self.left=left
        self.right=right
     
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root ==None:
            self.root = Node(data)
            return
        temp = self.root
        while True:
            if data < temp.data:
                if temp.left is not None:
                    temp=temp.left
                else:
                    temp.left=Node(data)
                    break
            elif data > temp.data:
                if temp.right is not None:
                    temp = temp.right
                else:
                    temp.right = Node(data)
                    break
            else:
                print ('data repeated : ', data)
                break
        return self.root

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left) 
        print(root.data,end=" ")
        self.inorder(root.right)

    def preorder(self,root):
        if root == None:
            return
        print(root.data,end=" ")
        self.preorder(root.left) 
        self.preorder(root.right)

    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left) 
        self.postorder(root.right)
        print(root.data,end=" ")
        

def main():
    print('code started')
    obj = BinarySearchTree()
    root =   obj.insert(15)
    root =   obj.insert(12)
    root =   obj.insert(7)
    root =   obj.insert(14)
    root =   obj.insert(27)
    root =   obj.insert(20)
    root =   obj.insert(23)
    root =   obj.insert(88)
    root =   obj.insert(88)
    print("---------   InOrder ----------")
    obj.inorder(root)
    print("\n---------   PreOrder ----------")
    obj.preorder(root)
    print("\n---------   PostOrder ----------")
    obj.postorder(root)

if __name__ == "__main__":
    main()

        
        
        

        