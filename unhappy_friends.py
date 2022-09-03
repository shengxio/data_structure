class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        n_unhappy = 0
        rank_ls = [0 for _ in range(n)]
        
        for p in pairs:    
            rank_ls[p[0]] = preferences[p[0]].index(p[1])
            rank_ls[p[1]] = preferences[p[1]].index(p[0])
            
        for i in range(n):
            if rank_ls[i] != 0:
                for j in range(rank_ls[i]):
                    target = preferences[i][j]
                    if preferences[target].index(i)< rank_ls[target]:
                        n_unhappy += 1
                        break
            pass
        return n_unhappy