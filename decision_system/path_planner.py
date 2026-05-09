import math

class PathPlanner:
    def __init__(self):
        self.waypoints = []

    def add_waypoint(self, x, y, z):
        self.waypoints.append((x, y, z))

    def calculate_distance(self, point1, point2):
        return math.sqrt(
            (point2[0] - point1[0]) ** 2 +
            (point2[1] - point1[1]) ** 2 +
            (point2[2] - point1[2]) ** 2
        )

    def get_total_path_distance(self):
        total = 0
        for i in range(len(self.waypoints) - 1):
            total += self.calculate_distance(
                self.waypoints[i],
                self.waypoints[i + 1]
            )
        return total

if __name__ == '__main__':
    planner = PathPlanner()

    planner.add_waypoint(0, 0, 0)
    planner.add_waypoint(5, 5, 3)
    planner.add_waypoint(10, 10, 5)

    print('Total Path Distance:', planner.get_total_path_distance())
