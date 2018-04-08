import math
import sys
def find_cos_sin(A):
    div = 10**6
    for i in xrange(0, div+1):
        degNow = (i * math.pi)/(4.000000 * div)
        area = math.cos(degNow) + math.sin(degNow)
        if abs(area-A) < 10**-7:
            sys.stderr.write('area = ' + str(area))
            return degNow
        if area > A:
            return degNow

def rotate(x, y, theta):
    rotated_x = math.cos(theta) * x - math.sin(theta) * y
    rotated_y = math.sin(theta) * x + math.cos(theta) * y
    return str(rotated_x), str(rotated_y)


def cubic_ufo(A):
    theta = find_cos_sin(A)
    sys.stderr.write('degrees = ' + str(math.degrees(theta)))
    rotated_x, rotated_y = rotate(0.5, 0, theta)
    print '{0} {1} {2}'.format(rotated_x, rotated_y, '0')
    rotated_x, rotated_y = rotate(0, 0.5, theta)
    print '{0} {1} {2}'.format(rotated_x, rotated_y, '0')
    print '0 0 0.5'

def __main__():
    t = int(raw_input())
    for i in xrange(t):
        A = float(raw_input())
        print 'Case #{0}:'.format(i + 1)
        cubic_ufo(A)

if __name__ == '__main__':
    __main__()
