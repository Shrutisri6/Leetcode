class Solution:
    def allpossiblestates(self, state):
        states=[]
        n0=0
        m0=0
        f=False
        for i in range(self.n):
            for j in range(self.m):
                if state[i][j]==0:
                    n0=i 
                    m0=j 
                    f=True
                    break
            if f:
                break 
        eg=[row[:] for row in state]
        if n0==0:
            states.append(state)
        else:
            eg[n0][m0],eg[n0-1][m0]=eg[n0-1][m0],eg[n0][m0]
            states.append(eg)
            eg=[row[:] for row in state]
        if m0==0:
            states.append(state)
        else:
            eg[n0][m0],eg[n0][m0-1]=eg[n0][m0-1],eg[n0][m0]
            states.append(eg)
            eg=[row[:] for row in state]
        if n0==self.n-1:
            states.append(state)
        else:
            eg[n0][m0],eg[n0+1][m0]=eg[n0+1][m0],eg[n0][m0]
            states.append(eg)
            eg=[row[:] for row in state]
        if m0==self.m-1:
            states.append(state)
        else:
            eg[n0][m0],eg[n0][m0+1]=eg[n0][m0+1],eg[n0][m0]
            states.append(eg)
            eg=[row[:] for row in state]
        return states
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque
        n=len(board)
        m=len(board[0])
        self.n=n
        self.m=m
        self.board=board
        sol=[[0]*m for _ in range(n)]
        k=1
        for i in range(n):
            for j in range(m):
                if i==n-1 and j==m-1:
                    continue
                sol[i][j]=k 
                k+=1
        visited=[]
        visited.append(board)
        queue=deque([(board, 0)])
        while queue:
            cboard, dist=queue.popleft()
            
            if cboard == sol:
                return dist
                
            for state in self.allpossiblestates(cboard):
                if state not in visited:
                    visited.append(state)
                    queue.append((state, dist+1))
        return -1
                
