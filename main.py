from point_cloud import PointCloud
from copy import deepcopy
import matplotlib.pyplot as plt



def main():

    ########################### 2D PLOT ###########################


    cloud2d_a = PointCloud(100,"2d")

    cloud2d_b = deepcopy(cloud2d_a)
    cloud2d_b.randomize()


    plt.scatter(cloud2d_a.get_x_values(),cloud2d_a.get_y_values(),label="Cloud A",c="b", marker="s")
    plt.scatter(cloud2d_b.get_x_values(),cloud2d_b.get_y_values(),label="Cloud B",c="r", marker="o")
    plt.legend(loc="upper right")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    ########################### 3D PLOT ###########################
    """
    cloud3d_a = PointCloud(100,"3d")
    print(cloud3d_a.point_cloud)

    cloud3d_b = PointCloud(100,"3d")
    print(cloud3d_b.point_cloud)

    print(cloud3d_a.point_cloud)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(cloud3d_a.get_x_values(),cloud3d_a.get_y_values(),cloud3d_a.get_z_values(),c="b", marker ="s")
    ax.scatter(cloud3d_b.get_x_values(),cloud3d_b.get_y_values(),cloud3d_b.get_z_values(),label="Cloud A",c="r", marker ="o")
    plt.show()
    """
if  __name__ == "__main__":
    main()