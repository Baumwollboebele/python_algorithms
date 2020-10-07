from Helper.point_cloud import PointCloud2D, PointCloud3D
from copy import deepcopy
import matplotlib.pyplot as plt


def main():

    ########################### 2D PLOT ###########################

    cloud2d_a = PointCloud2D(100)

    cloud2d_b = deepcopy(cloud2d_a)
    cloud2d_b.random_translation()

    plt.scatter(cloud2d_a.get_x_values(), cloud2d_a.get_y_values(),
                label="Cloud A", c="b", marker="s")
    plt.scatter(cloud2d_b.get_x_values(), cloud2d_b.get_y_values(),
                label="Cloud B", c="r", marker="o")
    plt.scatter(cloud2d_a.get_centroid().x ,cloud2d_a.get_centroid().y,
                label="Centroid A", c="g", marker="h")
    plt.scatter(cloud2d_b.get_centroid().x, cloud2d_b.get_centroid().y,
                label="Centroid A", c="g", marker="h")

    plt.legend(loc="upper right")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    ########################### 3D PLOT ###########################
    
    cloud3d_a = PointCloud3D(100)

    cloud3d_b = deepcopy(cloud3d_a)
    cloud3d_b.random_translation()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(cloud3d_a.get_x_values(), cloud3d_a.get_y_values(),
                cloud3d_a.get_z_values(), c="b", marker ="s")

    ax.scatter(cloud3d_b.get_x_values(), cloud3d_b.get_y_values(),
                cloud3d_b.get_z_values(), label="Cloud A",c="r", marker ="o")
    ax.scatter(cloud3d_a.get_centroid().x, cloud3d_a.get_centroid().y,
                cloud3d_a.get_centroid().z, label="Centroid A", c="g", marker="h")
    ax.scatter(cloud3d_b.get_centroid().x, cloud3d_b.get_centroid().y,
                cloud3d_b.get_centroid().z, label="Centroid A", c="g", marker="h")
    plt.show()


if  __name__ == "__main__":
    main()
