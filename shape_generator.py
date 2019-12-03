import numpy as np
import random

import matplotlib.pyplot as plt


def save_points_to_file(filename, points):
    with open('points/'+filename, "w") as f:
        for point in points:
            f.write(f"{point[0]} {point[1]}\n")


def get_points_from_file(filename):
    with open('points/'+filename) as f:
        points = []
        lines = f.read().splitlines()
        for line in lines:
            x, y = map(float, line.split())
            points.append((x, y))
        return points


def gen_shape(min_p, max_p, func, limit=10):
    a = random.randint(-limit, limit)
    b = random.randint(-limit, limit)

    x0 = random.randint(-limit**2, limit**2)
    y0 = random.randint(-limit**2, limit**2)

    return [func(t, a, b, x0, y0) for t in np.arange(0, 2*np.pi, 4*np.pi / random.randint(min_p, max_p))]


def line(t, a, b, x0, y0):
    return a*t + x0, b*t + y0


def zigzag_line(t, a, b, x0, y0):
    return a*t + x0, np.cos(t) + b*t + y0


def ellipse(t, a, b, x0, y0):
    return a*np.cos(t) + x0, b*np.sin(t) + y0


def plot_points(points):
    plt.plot(*zip(*points), marker='o', color='r', ls='')
    plt.savefig("output//points_plot.png")


if __name__ == "__main__":
    points = gen_shape(50, 100, zigzag_line)
    points = points + gen_shape(50, 100, ellipse)
    points = points + gen_shape(50, 100, line)
    points = points + gen_shape(50, 100, zigzag_line)
    points = points + gen_shape(50, 100, zigzag_line)
    save_points_to_file("line.txt", points)
    plot_points(points)



