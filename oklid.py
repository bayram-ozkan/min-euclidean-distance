#Calculation of Minimum Euclidean Distance

import math
import random

points = []
with open('points.txt', 'r') as file:
    for line in file:
        x, y = map(int, line.strip().split(', '))
        points.append((x, y))


def euclideanDistance(point1, point2):

    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


point1, point2 = random.sample(points, 2)
x1, y1 = point1
x2, y2 = point2


distance = euclideanDistance(point1, point2)
print(f"Distance between {point1} and {point2} : {distance}")


distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append((distance, points[i], points[j]))
print("##############################")


min_distance, point1, point2 = min(distances, key=lambda x: x[0])


print(f"Minimum distance: {min_distance}\nBetween points {point1} and {point2}")
