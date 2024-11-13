'''
A Solid cube 10cm * 10 cm * 10cm resets on the ground. it has a beetle on it, and
some sweet honey sweets at various locations on the surface of the cube. the beetle starts at 
a point on the surface of the cube and goes to the honey spots in order along
the surface of the cube

1 if it goes form a point to another point on the same face (say x to y) it goes
in an arc of a circle that subtends an angle of 60 degrees at the center of the circle

2. if it goes form one point to another on a different face, it goes by the
shortest path on the surface of the cube except that it never travels along the bottom of the cube

the  beetle is a student of cartesian gemotery and knows the coordinated x, y, z of all the points
it needs to go to. the origin of coordinates it uses is one corner of the cube on the ground, and the z axis point up . hence
the bootm surface on which it does not crewl is z=0 and the top surface is z=10 , the beetle keeps track of all the distance travelled and rounds the distance travelled to the two deciamal places onece it reaches the next spot, so that the final
distance is a sum of the rounded distance from spot to spot


input format:
the first line gives an integer N , the total number of points (including point) the beetle visits
the second line is a set of 3M cooma separated non negative numbers with up to two decimal places each. these are to be interpreted in groupss of three as the x, y, z coordinate of the points the beetle needs to visist in the given order

output format:
one line with a number giving the total distance travelled by the beetle accurate to two decimal places. even if the distance travelled is an intger the output should be deicimal places
'''