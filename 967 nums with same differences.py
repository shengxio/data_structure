class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        # the actual DFS uses * 10 and 
        def get_sequence(i,n):
            if n==1:
                return [[i]]
            
            seq = []
            if k == 0:
                seq = get_sequence(i,n-1)
                for s in seq:
                    s.insert(0,i)
                return seq
            
            if i+k <10:
                sub = get_sequence(i+k,n-1).copy()
                
                for s in sub:
                    s.insert(0,i)
                seq.extend(sub)

            if i-k >=0:
                sub = get_sequence(i-k,n-1).copy()
                for s in sub:
                    s.insert(0,i)
                seq.extend(sub)

            return seq
        
        ls_2_str = lambda ls: int(''.join([str(c) for c in ls]))
        
        for j in range(1,10):
            ans += [ls_2_str(ls) for ls in get_sequence(j,n)]

        return ans


# official solutions - DFS
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        if N == 1:
            return [i for i in range(10)]

        ans = []
        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)

# official solutions - BFS
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        if N == 1:
            return [i for i in range(10)]

        # initialize the queue with candidates for the first level
        queue = [digit for digit in range(1, 10)]

        for level in range(N-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                # using set() to avoid duplicates when K == 0
                next_digits = set([tail_digit + K, tail_digit - K])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            # start the next level
            queue = next_queue

        return queue