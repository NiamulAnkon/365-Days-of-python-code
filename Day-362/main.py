def merge(intervals):
    if not intervals:
        return []


    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_meged = merged[-1]

        if  current[0] <= last_meged[1]:
            last_meged[1] = max(last_meged[1], current[1])

        else:
            merged.append(current)
    
    return merged

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    merge(intervals)
    print(merge(intervals))