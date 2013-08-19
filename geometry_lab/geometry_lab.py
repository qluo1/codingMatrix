from mat import Mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels,labels), {(a,a): 1 for a in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    ret = identity()
    ret[('x','u')] = x
    ret[('y','u')] = y
    return ret

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    ret = identity()
    ret[('x','x')] = a
    ret[('y','y')] = b
    return ret
import math
## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    ret = identity()
    ret['x','x'] = ret['y','y'] = math.cos(angle)
    ret['x','y'] = -math.sin(angle)
    ret['y','x'] = math.sin(angle)
    return ret

## Task 5
# https://class.coursera.org/matrix-001/forum/thread?thread_id=3543
# Our rotation matrix rotates points only about the origin.
# That means we can't use it directly to answer the question in Task 5.
# But we can overcome this "difficulty" by translating the point to the origin (by multiplying) first! This allows us to rotate the point using our rotation matrix. And finally translate that image back.

def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return  translation(x,y) * rotation(angle) *  translation(-x,-y) 

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    ret = identity()
    ret['x','x'] = -1
    return ret

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    ret = identity()
    ret['y','y'] = -1
    return ret
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    ret = identity({'r','g','b'})
    ret['r','r'] = scale_r
    ret['b','b'] = scale_b
    ret['g','g'] = scale_g
    return ret

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    ret = identity({'r','g','b'})
    ret['r','r'] = 77/256
    ret['g','r'] = 77/256
    ret['b','r'] = 77/256
    ret['r','g'] = 151/256
    ret['g','g'] = 151/256
    ret['b','g'] = 151/256
    ret['r','b'] = 28/256
    ret['g','b'] = 28/256
    ret['b','b'] = 28/256
    return ret

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


