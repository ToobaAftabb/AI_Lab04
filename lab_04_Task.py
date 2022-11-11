#Task no: 01
class Node :

    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.totalCost=totalCost
def DFS():
    initial= input("Enter initial Node: ")
    goal = input("Enter destination Node: ")
    
    graph={
        'Oradea' : Node('Oradea',None,['Zerind','Sibiu'],[71,151] ),
        'Zerind' : Node('Zerind',None,['Arad', 'Oradea'],[75,71 ]),
        'Arad' : Node('Arad',None,['Zerind','Timisoara','Sibiu'],[75,118,140] ),
        'Sibiu' : Node('Sibiu',None,['Fagaras','Rimnicu Vilcea','Oradea','Arad'],[99,80,151,140] ),
        'Fagaras' : Node('Fagaras',None,['Sibiu','Bucharest'],[99,211] ),
        'Bucharest' : Node('Bucharest',None,['Fagaras','Pitesti','Urziceni','Giurgiu'],[211,101,85,90] ),
        'Pitesti' : Node('Pitesti',None,['Rimnicu Vilcea','Bucharest','Craiova'],[97,101,138] ),
        'Urziceni' : Node('Urziceni',None,['Bucharest','Hirsova','Vaslui'],[85,98,142] ),
        'Hirsova' : Node('Hirsova',None,['Urziceni','Eforie'],[98,86] ),
        'Timisoara':Node('Timisoara',None,['Lugoj','Arad'],[111,118]),
        'Lugoj':Node('Lugoj',None,['Mehadia','Timisoara'],[70,111]),
        'Mehadia':Node('Mehadia',None,['Drobeta','Lugoj'],[75,70]),
        'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,['Sibiu','Pitesti'],[70,111]),
        'Drobeta' : Node('Drobeta',None,['Craiova','Mehadia'],[120,75] ),
        'Craiova' : Node('Craiova',None,['Pitesti','Rimnicu Vilcea'],[138,146] ),
        'Eforie' : Node('Eforie',None,['Hirsova'],[86] ),
        'Vaslui' : Node('Vaslui',None,['Urziceni','Iasi'],[142,92] ),
        'Iasi' : Node('Iasi',None,['Vaslui','Neamt'],[92,87] ),
        'Giurgiu' : Node('Giurgiu',None,[],[]),
        'Neamt' : Node('Neamt',None,[],[] ),
        }
    front=[initial]
    explore=[]
    while(len(front)!=0):
         cNode=front.pop(len(front)-1)
         print (cNode)
         explore.append(cNode)
         cChild=0
         
         for i in graph[cNode].actions :
            if i not in front and i not in explore : 
                if graph[i].state==goal:
                    return actionSequence(graph,initial,goal)
                cChild=cChild+1
                front.append(i)
         if cChild==0:
            del explore[len(explore)-1]
def actionSequence(graph,initial,goal):
    sol=[goal]
    cp=graph[goal].parent
    while cp!=None:
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol

sol=DFS()
print(sol)


#Task no: 02
class Trie:
    def __init__(self):
        self.character = {}
        self.isLeaf = False  # true when the node is a leaf node
 
 
# Iterative function to insert a string into a Trie
def insert(root, s):
    # start from the root node
    curr = root
 
    for ch in s:
        curr = curr.character.setdefault(ch, Trie())
 
    curr.isLeaf = True
 
 
# (top, right, bottom, left, and four diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
def isSafe(x, y, processed, board, ch):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0])) and \
           not processed[x][y] and (board[x][y] == ch)
 

def searchBoggle(root, board, i, j, processed, path, result):
    if root.isLeaf:
        result.add(path)
        processed[i][j] = True
 
    for key, value in root.character.items():
 
        for k in range(len(row)):
 
            if isSafe(i + row[k], j + col[k], processed, board, key):
                searchBoggle(value, board, i + row[k], j + col[k],
                             processed, path + key, result)
 
    processed[i][j] = False
 
 
def searchInBoggle(board, words):
    
    result = set()
     # base case
    if not board or not len(board):
        return
 
    
    root = Trie()
    for word in words:
        insert(root, word)
 
    # `M × N` board
    (M, N) = (len(board), len(board[0]))
 
    processed = [[False for x in range(N)] for y in range(M)]
 
    # consider each character in the matrix
    for i in range(M):
        for j in range(N):
            ch = board[i][j]  
 
            if ch in root.character:
                searchBoggle(root.character[ch], board, i, j, processed, ch, result)
 return result

board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
  ]

words = ['START', 'NOTE', 'SAND', 'STONED']
searchInBoggle(board, words)

validWords = searchInBoggle(board, words)
print(validWords)
