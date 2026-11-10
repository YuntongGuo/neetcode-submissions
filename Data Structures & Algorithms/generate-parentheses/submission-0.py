class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        aggregate = []
        open = 0
        close =0
        def gen(cur,op, clo):
            if len(cur) == 2*n:
                aggregate.append(cur)
            else:
                if op < n:
                    # gen('(' + cur, op+1,clo)
                    gen( cur+'(', op+1,clo)

                if clo < op:
                    gen(cur+')', op, clo+1)
        gen("",0,0)
        return aggregate