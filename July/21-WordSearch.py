""" Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once. """

# SOLUTION

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.search(board, r, c, word, 0):
                    return True
        return False
    
    def search(self, board, row, col, word, i):
        if i == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        if board[row][col] != word[i]:
            return False
        char = board[row][col]
        board[row][col] = " "
        res = self.search(board,row+1,col,word,i+1)  \
            or self.search(board,row,col+1,word,i+1) \
            or self.search(board,row-1,col,word,i+1) \
            or self.search(board,row,col-1,word,i+1)
        board[row][col] = char
        return res
    
# It's not efficient to slice the word at every recursive call. Just pass the word and the index along instead.