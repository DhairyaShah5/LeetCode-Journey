class DetectSquares:
    def __init__(self):
        # Dictionary to count occurrences of points
        self.pointsCount = defaultdict(int)
        # List to store all added points
        self.points = []

    def add(self, point: List[int]) -> None:
        # Increment count for the point
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point

        for x, y in self.points:
            # Check for valid diagonal (i.e., must form a square)
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            # Count valid square formations using matching horizontal and vertical points
            result += self.pointsCount[(x, py)] * self.pointsCount[(px, y)]

        return result

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)