class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_2_idx = {nums[i]:i for i in range(len(nums))}
        possible_start = {}
        for n in nums:
            if n-1 not in num_2_idx:
                possible_start[n] = [n,1]
        max_len = 0
        for num in possible_start:
            n=num+1
            while n in num_2_idx: 
                if n in possible_start and possible_start[n][0] != possible_start[num][0]:
                    p1,s1 = possible_start[num]
                    p2,s2 = possible_start[n]
                    if s1 < s2:
                        possible_start[num] = (p2,s1+s2)
                        possible_start[n] = (p2,s1+s2)
                    else:
                        possible_start[n] = (p1,s1+s2)
                        possible_start[num] = (p1,s1+s2)
                else:
                    possible_start[num][1] +=1
                n+=1
        for n in possible_start:
            if possible_start[n][0] == n:
                max_len = max(max_len,possible_start[n][1])

        return max_len

            