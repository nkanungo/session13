# Author : Nihar Kanungo

import math
'''
    A regular strictly convex polygon is a polygon that has the following characteristics:
    all interior angles are less than 180
    all sides have equal length
    This class facilitates creation of objects which can get the properties
    edges
    vertices
    interior angle
    edge length
    apothem
    area
    perimeter
'''
class Polygon:

    def __init__(self ,edge , circumradius):
        '''
        where initializer takes in:
        number of vertices for largest polygon in the sequence
        common circumradius for all polygons
        '''
        self.edge, self.circumradius = edge,circumradius

    @property
    def edge(self):
        '''
        Returns the number of edges of the polygon
        '''
        return self._edge

    @edge.setter
    def edge(self, edge):
        '''
        Sets the edge of the Polygon
        '''
        if edge <3:
            raise ValueError("Edge in a regular polygon  must be positive and be minimum 3 to form a closed figure")
        else:
            #print("I was called")
            self._edge = edge

    @property
    def circumradius(self):
        '''
        Returns the circumradius of the polygon
        '''
        return self._circumradius

    @circumradius.setter
    def circumradius(self, circumradius):
        '''
        Sets the circum radius of the Polygon
        '''
        if circumradius <=0:
            raise ValueError("Circum radius must be positive")
        else:
            self._circumradius = circumradius

    @property
    def interior_angle(self): #method
        '''
        Returns the interior angle of the polygon
        '''
        return (self.edge - 2) * (180/self.edge)

    @property
    def edge_length(self):
        '''
        Returns the edge length of the polygon
        '''
        return 2 * self.circumradius * math.sin((math.pi/self.edge))

    @property
    def apothem(self):
        '''
        Returns the apothem of the polygon
        '''
        return self.circumradius * math.cos(math.pi/self.edge)

    @property
    def area(self):
        '''
        Returns the Area of the polygon
        '''
        return (1/2) * self.edge * self.edge_length * self.apothem

    @property
    def perimeter(self):
        '''
        Returns the perimeter of the polygon
        '''
        return (1/2) * self.edge * self.edge_length


    def __str__(self):
        return 'Polygon: edge={0}, circumradius={1}'.format(self.edge, self.circumradius)

    def __repr__(self):
        return 'Polygon({0}, {1})'.format(self.edge, self.circumradius)

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.edge == other.edge and self.circumradius == other.circumradius

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.edge > other.edge
        else:
            return NotImplemented
