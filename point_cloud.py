from random import randint 
from math import cos,sin,pi,radians
from mpl_toolkits.mplot3d import Axes3D


class Point(object):
    @staticmethod
    def factory(type):
        if type == "Point_2D": 
            return Point_2D()

        if type == "Point_3D":
            return Point_3D()
    
class Point_2D(Point):
    def __init__(self):
        """
        Initializes a 2D point object with x and y coordinates.
        """
        self.x = randint(0,50)
        self.y = randint(0,50)
    
    def __str__(self):
        return f"X: {self.x} Y: {self.y}"

    def __repr__(self):
        return f"X: {self.x} Y: {self.y}"

class Point_3D(Point):
    def __init__(self):
        """
        Initializes a 3D point object with x,y and z coordinates.
        """
        self.x = randint(0,50)
        self.y = randint(0,50)
        self.z = randint(0,50)
    
    def __str__(self):
        return f"X: {self.x} Y: {self.y} Z: {self.z}"

    def __repr__(self):
        return f"X: {self.x} Y: {self.y} Z: {self.z}"


class PointCloud:   
    def __init__(self,size,dimension):
        """
        Initializes a random Point cloud within a 2D or 3D coordinate system.

        Args:
            size (integer): number of points
            dimension (string): either "2d" or "3d"
        """
        self.point_cloud = []
        self.dimension = dimension
    
        if dimension == "3d":
            for _ in range(size):
                self.point_cloud.append(Point_3D())
        if dimension == "2d":
            for _ in range(size):
                self.point_cloud.append(Point_2D())
        
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

    def get_z_values(self):
        """
        Returns z values of all points.

        Returns:
            list: z-axis values
        """
        values = []
        if self.dimension == "3d":
            for point in self.point_cloud:
                values.append(point.z)
            
            return values 

        else:
            print("There is no 3rd dimension.")

        
    def rotate(self,rotation):
        """
        Rotation of the point cloud around the z achsis with the angle [rotation].

        Args:
            rotation (integer | float): angle of rotation
        """
        rotation = radians(rotation)
        for point in self.point_cloud:
            x = point.x
            y = point.y

            point.x = round((x*cos(rotation)) - (y*sin(rotation)),2)
            point.y = round((y*cos(rotation)) + (x*sin(rotation)),2)

        return

    def translate(self,x ,y):
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
        self.rotate(randint(0,360))
        return

    def random_translation(self):
        """
        Applies a random translation to the point cloud.
        """
        self.translate(randint(0,5),randint(0,5))
        return 

    def randomize(self):
        """
        Applize random translation and rotation to the point cloud.
        """
        self.random_translation()
        self.random_rotation()
        return
    
        