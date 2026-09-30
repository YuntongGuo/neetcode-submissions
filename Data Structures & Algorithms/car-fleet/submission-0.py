class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort
        cars = sorted(zip(position,speed))
        stack = []
        def one_fleet(c1,c2):
            # print(c1,c2)
            c2_arrive = float(target-c2[0])/c2[1]
            c1_arrive = float(target-c1[0])/c1[1]
            # print(c1_arrive >=c2_arrive)
            return c1_arrive >=c2_arrive
        
        for i in range(len(cars)-1,-1,-1):
            p,s = cars[i]
            if not stack:
                stack.append((p,s))
            elif not one_fleet(stack[-1],(p,s)):
                stack.append((p,s))
        # print(stack)
        return len(stack)

