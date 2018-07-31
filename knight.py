class KnightProblem:

    possMove=[[-2,1],[2,1],[2,-1],[-1,2],[1,2],[1,-2],[-1,-2],[-2,-1]]
    _count=0

    def checkNode(self,node):
        if(node[0]>=0 and node[1]>=0 and node[0]<=7 and node[1]<=7):
            return True
        else:
            return False

    def printPath(self,sol):
        print("P" + str(KnightProblem._count) + ": " + str(sol) + "\n")

    def solveKnightProblem(self,s,d):
        sol=[s]
        if(not self.findPath(sol,d)):
            print("Path don't exist")

    def findPath(self,sol,d):
        for x in KnightProblem.possMove:
            nextNode=[sol[-1][0]+x[0],sol[-1][1]+x[1]]
            if(self.checkNode(nextNode) and nextNode not in sol):
                sol.append(nextNode)
                if(nextNode==d):
                    KnightProblem._count+=1
                    self.printPath(sol)
                    if(KnightProblem._count==10):
                        exit()
                    sol.pop()
                    continue 
                if(not self.findPath(sol,d)):
                    sol.pop()
                    continue
        else:
            return False    

obj=KnightProblem()
obj.solveKnightProblem([2,3],[7,7])