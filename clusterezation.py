from shape_generator import get_points_from_file
import matplotlib.pyplot as plt

colors = {0: "b", 1: "g", 2: "r", 3: "c", 4: "m", 5: "y", 6: "k"}


class Cluster:
    def __init__(self, point):
        self.id = id
        self.points = []
        self.points.append(point)
        self.left = point
        self.right = point

    @staticmethod
    def dist(p1, p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

    def add(self, point, max_dist):
        if self.dist(self.left, point) < max_dist:
            self.points.append(point)
            self.left = point
            return True
        elif self.dist(self.right, point) < max_dist:
            self.points.append(point)
            self.right = point
            return True
        else:
            dist = min(self.dist(self.left, point), self.dist(self.right, point))
            return False

    def get_xy(self):
        return list(zip(*self.points))[0], list(zip(*self.points))[1]


def clustered(points, max_dist):
    points.sort(key=lambda k: k[0])

    clusters = [Cluster(points[0])]

    for point in points[1:]:
        # sout.flush()
        # sout.write(f"\r{len(clusters)}, {points.index(point) / len(points)} %")

        clustered = False
        for cluster in clusters:
            if cluster.add(point, max_dist):
                clustered = True
                break
        if not clustered:
            clusters.append(Cluster(point))
    return clusters


def correlation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    sum_xy = sum([x_i * y_i for x_i, y_i in zip(x, y)])

    square_sum_x = sum([x_i ** 2 for x_i in x])
    square_sum_y = sum([y_i ** 2 for y_i in y])

    try:
        corr = (n * sum_xy - sum_x * sum_y) /\
               (((n * square_sum_x - sum_x**2) * (n * square_sum_y - sum_y**2))**0.5)
        return corr
    except ZeroDivisionError:
        return 0


def find_lines(clusters, cor):
    lines = []
    for cluster in clusters:
        x, y = cluster.get_xy()
        if abs(correlation(x, y)) > cor:
            lines.append(cluster.points)
    plot_lines(lines)
    return lines


def reg_coef(x, y):
    n = len(x)
    m_x = sum(x) / n
    m_y = sum(y) / n

    ss_xy = sum([x_i*y_i for x_i, y_i in zip(x, y)]) - n * m_y * m_x
    ss_xx = sum([x_i**2 for x_i in x]) - n * m_x * m_x

    b_1 = ss_xy / ss_xx
    b_0 = m_y - b_1 * m_x

    return b_0, b_1


def plot_lines(lines):
    plt.clf()
    for line in lines:
        x = list(zip(*line))[0]
        y = list(zip(*line))[1]
        b = reg_coef(x, y)
        y_p = [b[0] + b[1]*x_i for x_i in x]
        plt.plot(x, y_p, color='g')
    plt.savefig("output//lines.png")


def plot_clusters(clusters):
    plt.clf()
    c = 0
    for cluster in clusters:
        plt.plot(*zip(*cluster.points), marker='o', markersize=3, color=colors[c % 7], ls='')
        c += 1
    plt.savefig("output//clusters_plot.png")


if __name__ == "__main__":
    star_points = get_points_from_file("line.txt")
    clusters = clustered(star_points, 5)
    plot_clusters(clusters)
    find_lines(clusters, 0.9)
