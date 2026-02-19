
import math
import matplotlib.pyplot as plt

def compute_vertices(lines):
    x, y = 0, 0
    vertices = [(x, y)]

    for bearing, distance in lines:
        angle = math.radians(bearing)
        dx = distance * math.cos(angle)
        dy = distance * math.sin(angle)
        x += dx
        y += dy
        vertices.append((x, y))

    return vertices

def check_closure(vertices):
    start = vertices[0]
    end = vertices[-1]
    error = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    return error

def compute_area(vertices):
    area = 0
    n = len(vertices)
    for i in range(n - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2

def plot_polygon(vertices):
    xs = [v[0] for v in vertices]
    ys = [v[1] for v in vertices]

    plt.figure()
    plt.plot(xs, ys, marker='o')
    plt.title("Land Parcel Plot")
    plt.xlabel("X Coordinates")
    plt.ylabel("Y Coordinates")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    lines = [
        (0, 100),
        (90, 50),
        (180, 100),
        (270, 50)
    ]

    vertices = compute_vertices(lines)
    closure_error = check_closure(vertices)
    area = compute_area(vertices)

    print("Vertices:", vertices)
    print("Closure Error:", closure_error)
    print("Area:", area)

    plot_polygon(vertices)
