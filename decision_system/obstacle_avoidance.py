import math

class ObstacleAvoidance:
    def __init__(self, safe_distance=2.0):
        self.safe_distance = safe_distance

    def detect_obstacle(self, distance):
        return distance < self.safe_distance

    def generate_avoidance_vector(self, angle):
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        return (-x, -y)

if __name__ == '__main__':
    obstacle_system = ObstacleAvoidance()

    obstacle_detected = obstacle_system.detect_obstacle(1.5)

    if obstacle_detected:
        vector = obstacle_system.generate_avoidance_vector(45)
        print(f"Avoidance Vector: {vector}")
