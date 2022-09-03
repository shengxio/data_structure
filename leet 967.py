class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        return_ls = []
        def get_sequence(i,n,k):
            if n==1:
                return [[i]]
            
            seq = []
            if k == 0:
                seq = get_sequence(i,n-1,k)
                for s in seq:
                    s.insert(0,i)
                return seq
            
            if i+k <10:
                sub = get_sequence(i+k,n-1,k).copy()
                
                for s in sub:
                    s.insert(0,i)
                seq.extend(sub)

            if i-k >=0:
                sub = get_sequence(i-k,n-1,k).copy()
                for s in sub:
                    s.insert(0,i)
                seq.extend(sub)

            return seq
        
        ls_2_str = lambda ls: int(''.join([str(c) for c in ls]))
        
        for j in range(1,10):
            return_ls += [ls_2_str(ls) for ls in get_sequence(j,n,k)]

        return return_ls