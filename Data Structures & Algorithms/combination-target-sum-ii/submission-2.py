class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def cS(i,acc,targets):
            if i >= len(candidates):
                return 
            if candidates[i] > target:
                return 
            if targets == candidates[i]:
                repeat = False
                can = acc + [candidates[i]]
                # for j in range(len(result)):
                #     if result[j] == can:
                #         repeat = True
                #         break
                # if not repeat:   
                result.append(can)
            
            if targets > candidates[i]:
                cS(i+1,acc+[candidates[i]],targets - candidates[i])
            
            while i + 1 <len(candidates) and candidates[i+1] == candidates[i]:
                i += 1

            cS(i+1,acc,targets)
        
        cS(0,[],target)
        return result
        