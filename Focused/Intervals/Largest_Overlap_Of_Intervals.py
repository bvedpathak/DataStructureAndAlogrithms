class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def largest_overlap_of_intervals(intervals):
    if not intervals:
        return None
    
    points = []
    for interval in intervals:
        points.append((interval.start, 'S'))
        points.append((interval.end, 'E'))
    
    points.sort(key=lambda x: (x[0], x[1]))
    active_intervals = 0
    max_overlaps = 0
    
    for time, point_type in points:
        if point_type == 'S':
            active_intervals += 1
        else:
            active_intervals -= 1
        max_overlaps = max(max_overlaps, active_intervals)
    return max_overlaps

intervals = [Interval(1,3), Interval(2,6), Interval(4,8), Interval(6,7), Interval(5,7)]

print("\n")
print(f"Largest overlap Intervals is: {largest_overlap_of_intervals(intervals)}")
