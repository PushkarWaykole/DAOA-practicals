# get character frequency from the user
'''
n = int(input("Enter the number of characters: "))
chars = []
for i in range(n):
    ch = input("Enter the character: ")
    freq = int(input("Enter the frequency: "))
    node = Node(ch, freq)
    chars.append(node)
'''
class Node():
    def __init__(self,ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None
        self.code = ""

n = 5
chars= [Node('a', 35),
        Node('b', 12),
        Node('c', 8),
        Node('d', 25),
        Node('e', 20)]
# sort the characters based on their frequency
chars.sort(key=lambda x: x.freq)

for i in range(len(chars)):
        print(chars[i].ch,chars[i].freq)
print("\n----")

while(True):
    if len(chars) == 1:        
        break
    node = Node("*", chars[0].freq + chars[1].freq)
    node.left = chars[0]
    node.right = chars[1] 
    node.left.code = "0"
    node.right.code = "1" 
    # print(chars) 
    del chars[0]
    del chars[0]
    # print(chars) 
    chars.append(node)
    # print(chars) 
    chars.sort(key=lambda x: x.freq)
    for i in range(len(chars)):
        print(chars[i].ch,chars[i].freq)
    print("\n----")


def huffmanCode(node,val=''):
    node.code = val+node.code
    if node.left != None:
        huffmanCode(node.left, node.code)
    if node.right != None:
        huffmanCode(node.right, node.code)
    if node.left is None and node.right is None:
        print(node.ch,node.code)

root = chars[0]
code = ""

huffmanCode(root, code)


    
    






