""" There are 8 prison cells in a row, and each cell is either occupied or vacant.
Each day, whether the cell is occupied or vacant changes according to the following rules:

    If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.) """

# SOLUTION

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        found_dic = {}
        for i in range(N):
            cells_str = str(cells)
            if cells_str in found_dic:
                loop_len = i - found_dic[cells_str]
                return self.prisonAfterNDays(cells, (N - i) % loop_len)
            else:
                found_dic[cells_str] = i 
                cells = self.next_step(cells) 
                
        return cells
    
    def next_step(self, cells):
        res = [0] * 8
        for i in range(1,7):
            res[i] = int(cells[i-1] == cells[i+1])
        return res