A regular strictly convex polygon is a polygon that has the following characteristics:
all interior angles are less than 180
all sides have equal length

In this Repository we have created 2 modules 

Module 1
=========
Created a Polygon Class: where initializer takes in: number of edges/vertices circumradius
and creates the following properties:
edges
vertices
interior angle
edge length
apothem
area
perimeter
We have also created the following functionalities:
a proper __repr__ function
implements equality (==) based on # vertices and circumradius (__eq__)
implements > based on number of vertices only (__gt__)

Module 2
========

Implemented a Custom Polygon sequence type:
where initializer takes in:
number of vertices for largest polygon in the sequence , common circumradius for all polygons that can provide these properties:
max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
that has these functionalities:
functions as a sequence type (__getitem__)
supports the len() function (__len__)
has a proper representation (__repr__)
