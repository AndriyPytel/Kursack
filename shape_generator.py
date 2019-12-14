import numpy as np
import random

import matplotlib.pyplot as plt


def save_points_to_file(filename, points):
    with open(filename, "w") as f:
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


def gen_shape(a, b, x0, y0, func, radian_low=0, radian_high=np.pi):
    return [func(t, a, b, x0, y0) for t in np.arange(radian_low, radian_high, np.pi/60)]


def gen_rand_shape(min_p, max_p, func, random_limit=10):
    a = random.randint(-random_limit, random_limit)
    b = random.randint(-random_limit, random_limit)

    x0 = random.randint(-random_limit, random_limit)
    y0 = random.randint(-random_limit, random_limit)

    return [func(t, a, b, x0, y0) for t in np.arange(0, np.pi, 4*np.pi / random.randint(min_p, max_p))]


def line(t, a, b, x0, y0):
    return a*t + x0, b*t + y0


def zigzag_line(t, a, b, x0, y0):
    return a*t + x0, b*t + + random.normalvariate(y0, y0 / 100)


def ellipse(t, a, b, x0, y0):
    return a*np.cos(t) + x0, b*np.sin(t) + y0


def plot_points(points):
    plt.plot(*zip(*points), marker='o', markersize=3, color='r', ls='')
    plt.savefig("output//points_plot.png")


if __name__ == "__main__":
    points = gen_shape(10, 10, 30, 20, ellipse, radian_high=np.pi/3)
    points = points + gen_shape(5, 5, 0, 20, ellipse, radian_low=2*np.pi/3, radian_high=1.2*np.pi)
    points = points + gen_shape(1, -0.1, 5, 5, zigzag_line, radian_high=3*np.pi)
    points = points + gen_shape(1.5, 0.5, 20, 8, zigzag_line, radian_high=3*np.pi)
    points = points + gen_shape(1.5, -0.2, 10, 30, line, radian_high=2*np.pi)


    save_points_to_file("points/line.txt", points)
    plot_points(points)



