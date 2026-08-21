class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board=[[' ']*3 for _ in range(3)]
        for i in range(len(moves)):
            if i%2==0:
                board[moves[i][0]][moves[i][1]]='X'
            else:
                board[moves[i][0]][moves[i][1]]='O'
        if board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X':
            return "A"
        elif board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O':
            return "B"
        elif board[2][0]=='X' and board[1][1]=='X' and board[0][2]=='X':
            return "A"
        elif board[2][0]=='O' and board[1][1]=='O' and board[0][2]=='O':
            return "B"
        elif board[0]==['X', 'X', 'X']:
            return "A"
        elif board[0]==['O','O','O']:
            return "B"
        elif board[1]==['X', 'X', 'X']:
            return "A"
        elif board[1]==['O','O','O']:
            return "B"
        elif board[2]==['X', 'X', 'X']:
            return "A"
        elif board[2]==['O','O','O']:
            return "B"
        elif board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X':
            return "A"
        elif board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O':
            return "B"
        elif board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X':
            return "A"
        elif board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O':
            return "B"
        elif board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X':
            return "A"
        elif board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O':
            return "B"
        elif len(moves)==9:
            return "Draw"
        else:
            return "Pending"
