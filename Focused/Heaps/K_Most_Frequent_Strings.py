import heapq

def k_most_frequent_strings(strs, k):
    if not strs:
        return None
    if k >= len(strs):
        return strs

    class Pair:
        def __init__(self, str, freq):
            self.str = str
            self.freq = freq
        
        def __lt__(self, other):
            if self.freq == other.freq:
                return self.str < other.str
            return self.freq > other.freq

    freqs = {}

    for str in strs:
        freqs[str] = freqs.get(str, 0) + 1
    max_heap = [Pair(str, freq) for str, freq in freqs.items()]
    heapq.heapify(max_heap)

    return [heapq.heappop(max_heap).str for _ in range(k)]


print("\n")
strs = ["go", "hi", "byte", "go", "No", "byte"]
k = 2
print(f"Top k = {k} most frequent strings in {strs} are: {k_most_frequent_strings(strs,k)}")
print("\n")