import bisect
class TimeMap:

    def __init__(self):
        self.name_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.name_dict[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        words = self.name_dict[key]
        if words == []:
            return ""
        left_most_index = bisect.bisect_right(words,timestamp,key=lambda x: x[1])
        if left_most_index == len(words):
            if words[-1][1] == timestamp:
                return words[-1][0]
            return words[-1][0]
        elif left_most_index == 0:
            return ''
        return words[left_most_index-1][0]
