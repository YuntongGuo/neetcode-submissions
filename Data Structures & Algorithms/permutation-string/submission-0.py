class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        count = len(s1)
        for i,c in enumerate(s2):
            print(c)
            print(counter)
            
            if i >= len(s1):
                l = i - len(s1)
                if s2[l] in counter:
                    print("add",s2[l])
                    if counter[s2[l]]>=0:
                        print("increase")
                        count +=1
                    counter[s2[l]]+=1
            if c in counter:
                if counter[c]>0:
                    print("reduce")
                    count -=1
                    if count == 0:
                        return True
                counter[c]-=1
            print(count)
                
        return False