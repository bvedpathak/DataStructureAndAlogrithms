class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        print(f"({self.start}, {self.end})")

    def __lt__(self, other):
        return self.start < other.start
    
def identify_all_interval_overlaps(Intervals1, Intervals2):
    if not Intervals1 or not Intervals2:
        return None
    overlap = []
    i = 0
    j = 0

    while i < len(Intervals1) and j < len(Intervals2):
        if Intervals1[i].start < Intervals2[j].start:
            A, B = Intervals1[i], Intervals2[j]
        else:
            B, A = Intervals1[i], Intervals2[j]
        
        if B.start <= A.end:
            overlap.append(Interval(B.start, min(A.end, B.end)))

        if Intervals1[i].end < Intervals2[j].end:
            i += 1
        else:
            j += 1
    
    return overlap

print("\n")

Intervals1 = [Interval(1,4), Interval(5,6), Interval(9,10)]
Intervals2 = [Interval(2,7), Interval(8,9)]

for overlapped in identify_all_interval_overlaps(Intervals1, Intervals2):
    print(f"({overlapped.start}, {overlapped.end})")
