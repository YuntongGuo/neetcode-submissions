class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        lens = [str(len(s)) for s in strs]
        header = ','.join(lens)
        result = header+'|'+ ''.join(strs)
        # print(result)
        return result

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        splitter = s.find('|')
        # print(splitter)
        header = s[:splitter]
        lens = header.split(',')
        lens = [int(l) for l in lens]
        # print(lens)
        result = []
        acc_len = splitter+1
        for l in lens:
            result.append(s[acc_len:acc_len+l])
            acc_len += l
        return result