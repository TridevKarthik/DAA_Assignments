# implement closest pair algorithm using divide and conquer


#calculates euclidean distance between 2 points
def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx**2 + dy**2)**0.5

#brute force method to find the closest pair
def brute_force(points):
    min_dist = float('inf')
    best_pair = (None, None)
    n = len(points)

    #compare points.
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                best_pair = (points[i], points[j])

    return min_dist, best_pair

def closest_recursive(points_sorted):
    n = len(points_sorted)
    if n <= 3:
        return brute_force(points_sorted)

    mid = n // 2
    left = points_sorted[:mid]
    right = points_sorted[mid:]

    mid_x = points_sorted[mid - 1][0]

    d1, pair1 = closest_recursive(left)
    d2, pair2 = closest_recursive(right)

    if d1 < d2:
        min_dist = d1
        best_pair = pair1
    else:
        min_dist = d2
        best_pair = pair2

    strip = [p for p in points_sorted if abs(p[0] - mid_x) < min_dist]
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            d = distance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                best_pair = (strip[i], strip[j])

    return min_dist, best_pair

def closest_pair(points):
    if len(points) < 2:
        return float('inf'), (None, None)

    sorted_points = sorted(points, key=lambda p: p[0])
    return closest_recursive(sorted_points)


points = [
    (10, 20), (15, 24), (30, 35), (18, 22),
    (50, 60), (12, 21), (25, 30), (17, 23)
]

min_dist, pair = closest_pair(points)


print("input points:")
for pt in points:
    print(" ", pt)

print("\nclosest pair:")
print(" ", pair[0], "and", pair[1])
print("distance:", round(min_dist, 4))