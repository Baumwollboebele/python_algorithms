from random import randint
from math import cos, sin, radians


class _Point2D:
    def __init__(self, x=None, y=None):
        """
        Initializes a 2D point object with x and y coordinates.
        """
        if x is None:
            x = randint(0, 50)
        if y is None:
            y = randint(0, 50)

        self.x = x
        self.y = y

    def __str__(self):
        return f"X: {self.x} Y: {self.y}"

    def __repr__(self):
        return f"X: {self.x} Y: {self.y}"


class _Point3D:
    def __init__(self, x=None, y=None, z=None):
        """
        Initializes a 3D point object wit x,y and z coordinates.

        Args:
            x (integer, optional): X coordinate. Defaults to randint(0, 50).
            y (integer, optional): Y coordinate. Defaults to randint(0, 50).
            z (integer, optional):Z. Defaults to randint(0, 50).
        """

        if x is None:
            x = randint(0, 50)
        if y is None:
            y = randint(0, 50)
        if z is None:
            z = randint(0, 50)

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"X: {self.x} Y: {self.y} Z: {self.z}"

    def __repr__(self):
        return f"X: {self.x} Y: {self.y} Z: {self.z}"


class _PointCloud:

    def __init__(self, size):
        self.size = size
        self.point_cloud = []

    def get_x_values(self):
        """
        Returns x values of all points.

        Returns:
            list: x-axis values
        """
        values = []
        for point in self.point_cloud:
            values.append(point.x)

        return values

    def get_y_values(self):
        """
        Returns y values of all points.

        Returns:
            list: y-axis values
        """
        values = []
        for point in self.point_cloud:
            values.append(point.y)

        return values


class PointCloud2D(_PointCloud):
    def __init__(self, size):
        """
    Initializes a random Point cloud within a 2D coordinate system.

    Args:
        size (integer): number of points
    """
        super().__init__(size)

        for _ in range(size):
            self.point_cloud.append(_Point2D())

    def rotate(self, rotation):
        """
        Rotation of the point cloud around the z axis
        with the angle [rotation].

        Args:
            rotation (integer | float): angle of rotation
        """
        rotation = radians(rotation)
        for point in self.point_cloud:
            x = point.x
            y = point.y

            point.x = round((x*cos(rotation)) - (y*sin(rotation)), 2)
            point.y = round((y*cos(rotation)) + (x*sin(rotation)), 2)

        return

    def translate(self, x, y):
        """
        Translate the coordinates of the point cloud by x and y.

        Args:
            x (integer | float): translation by x
            y (integer | float ): translation by y
        """
        for point in self.point_cloud:
            point.x += x
            point.y += y

        return

    def random_rotation(self):
        """
        Applies a random rotation to the point cloud.
        """
        self.rotate(randint(0, 360))
        return

    def random_translation(self):
        """
        Applies a random translation to the point cloud.
        """
        self.translate(randint(0, 5), randint(0, 5))
        return

    def randomize(self):
        """
        Applize random translation and rotation to the point cloud.
        """
        self.random_translation()
        self.random_rotation()
        return

    def get_centroid(self):
        x = sum(self.get_x_values()) / len(self.get_x_values())
        y = sum(self.get_y_values()) / len(self.get_y_values())

        return _Point2D(x,y)
class PointCloud3D(_PointCloud):
    def __init__(self, size):
        """
        Initializes a random Point cloud within a 3D coordinate system.

        Args:
            size (integer): number of points
        """

        super().__init__(size)

        for _ in range(size):
            self.point_cloud.append(_Point3D())

    def get_z_values(self):
        """
        Returns z values of all points.

        Returns:
            list: z-axis values
        """
        values = []
        
        for point in self.point_cloud:
            values.append(point.z)

        return values

    def rotate_x_axis(self, rotation):
        """
        Rotation of the Point Cloud around the X-Axis.

        Args:
            rotation (integer): angle of rotation
        """

        rotation = radians(rotation)

        for point in self.point_cloud:
            point.y = round((point.y*cos(rotation)) - (point.z*sin(rotation)), 2)
            point.z = round((point.y*sin(rotation)) + (point.z*cos(rotation)), 2)
        return

    def rotate_y_axis(self, rotation):
        """
        Rotation of the Point Cloud around the Y-Axis

        Args:
            rotation (integer): angle of rotation
        """

        rotation = radians(rotation)

        for point in self.point_cloud:
            point.x = round((point.x*cos(rotation)) + (point.z*sin(rotation)), 2)
            point.z = round((-point.x*sin(rotation)) + (point.z*cos(rotation)), 2)
        return

    def rotate_z_axis(self, rotation):

        rotation = radians(rotation)

        for point in self.point_cloud:
            point.x = round((point.x*cos(rotation)) - (point.y*sin(rotation)), 2)
            point.x = round((point.x*sin(rotation)) + (point.y*cos(rotation)), 2)
        return

    def translate(self, x, y, z):
        """
        Translate the coordinates of the point cloud by x and y.

        Args:
            x (integer | float): translation by x
            y (integer | float): translation by y
            z (integer | float): translation by z
        """
        for point in self.point_cloud:
            point.x += x
            point.y += y
            point.z += z
        return

    def random_rotation(self):
        """
        Applies a random rotation to the point cloud.
        """
        self.rotate_x_axis(randint(0, 360))
        self.rotate_y_axis(randint(0, 360))
        self.rotate_z_axis(randint(0, 360))
        return

    def random_translation(self):
        """
        Applies a random translation to the point cloud.
        """
        self.translate(randint(0, 5), randint(0, 5), randint(0, 5))
        return

    def randomize(self):
        """
        Applize random translation and rotation to the point cloud.
        """
        self.random_translation()
        self.random_rotation()
        return

    def get_centroid(self):
        x = sum(self.get_x_values()) / len(self.get_x_values())
        y = sum(self.get_y_values()) / len(self.get_y_values())
        z = sum(self.get_z_values()) / len(self.get_z_values())

        return _Point3D(x, y, z)
