# Author : Nihar Kanungo

from functools import lru_cache
import math
'''
    This is a polygon class which has been designed to perform the following functions
    It initializes a Polygon object by taking input as edge and circumradius
    then it creates a sequence for all the Area versus Permmeter for all the Convex Polygons
    It also returns the Polygon with maximum area to perimeter ratio
'''
class Polygon:

    def __init__(self, edge,circumradius):
        '''
        where initializer takes in:
        number of vertices for largest polygon in the sequence
        common circumradius for all polygons
        '''
        self.edge, self.circumradius = edge,circumradius

    def __len__(self):
        '''
        Length for an arithmetic range which is created
        '''
        return self.edge

    def __getitem__(self,n):
        '''
        This method helps to create the virtual sequence
        '''
        if isinstance(n, int):
            if n < 3 or n >=self.edge:
                raise IndexError
            elif n < 2:
                return 0
            else:
                return Polygon._efficiency(n,self.circumradius)
    def __repr__(self):
        '''
        Represents the method properly
        '''
        return '{}({}, {})'.format(
            type(self).__name__, self.edge, self.circumradius)

    @staticmethod #Static methods are methods that are bound to a class rather than its object.
    @lru_cache(2**10) #powers of 2
    def _efficiency(edge,circumradius):
        '''
        Calculates the Area to Perimeter ratio for the Polygons
        '''
        edge = edge +1
        return round((1/2) * circumradius * math.cos((math.pi/edge)),3)

    def _max_eff(self,seq_list):
        '''
        Returns the Polygon with maximum Area to Perimeter ratio
        '''
        return f' The Maximum ratio is for the Polygon {seq_list.index(max(seq_list)) +1} and the ratio is {max(seq_list)}'
