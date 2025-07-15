class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        print(f"({self.start}, {self.end})")

    def __lt__(self, other):
        return self.start < other.start

def merge_overlapping_intervals(intervals):
    if not intervals:
        return None
    #intervals.sort(key=lambda x: x.start) # Alternate way to sort
    intervals.sort()
    merged_intervals = [intervals[0]]
    for B in intervals[1:]:
        A = merged_intervals[-1]
        if B.start > A.end:
            merged_intervals.append(B)
        else:
            merged_intervals[-1] = Interval(A.start, max(A.end, B.end))
    return merged_intervals

print("\n")

intervals = [Interval(3, 4), Interval(7, 8), Interval(2, 5), Interval(6, 7), Interval(1, 4)]

for merged in merge_overlapping_intervals(intervals):
    print(f"{merged.start}, {merged.end}")
          
