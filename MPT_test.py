import math
import numpy as np
import unittest
from MPT import MinVarianceAllocation


class MinVarianceAllocationTests(unittest.TestCase):

    def test_1(self):
        hist = np.asarray([[1,1.11111111111,1.22222222222,1.33333333333,1.44444444444,1.55555555556,1.66666666667,
                            1.77777777778,1.88888888889,2],
                            [2,
                            2.11111111111,
                            2.22222222222,
                            2.33333333333,
                            2.44444444444,
                            2.55555555556,
                            2.66666666667,
                            2.77777777778,
                            2.88888888889,
                            3]
                           ])

        budget_strategy, success = MinVarianceAllocation(hist)
        print budget_strategy

    def test_2(self):
        hist = np.asarray([[0,
                            3,
                            1,
                            3.5,
                            1.2,
                            4,
                            1.4,
                            4.5,
                            1.6,
                            2],
                           [2,
                            1.5,
                            2.22222222222,
                            1.7,
                            2.44444444444,
                            1.9,
                            2.66666666667,
                            2.1,
                            2.88888888889,
                            3]
                                    ])

        budget_strategy, success = MinVarianceAllocation(hist)
        print budget_strategy

    def test_3(self):
        hist = np.asarray([[1,
                            1.1,
                            1,
                            1.3,
                            1,
                            1.1,
                            1,
                            1.5,
                            1,
                            2],
                           [2,
                            1.5,
                            2,
                            1.9,
                            2,
                            1.7,
                            2,
                            1.9,
                            2,
                            1]
                                    ])

        budget_strategy, success = MinVarianceAllocation(hist)
        print budget_strategy

    def test_4(self):
        hist = np.asarray([[1.05,
                            1.05,
                            1.05,
                            1.05,
                            1.05,
                            1.05,
                            1.05,
                            1.4,
                            1.6,
                            1.1],
                           [1.025,
                            1.025,
                            1.025,
                            1.025,
                            1.025,
                            1.025,
                            1.025,
                            .7,
                            .4,
                            .9],
                           [1,
                            1,
                            1,
                            1,
                            1,
                            1,
                            1,
                            .6,
                            .5,
                            1]
                           ])

        budget_strategy, success = MinVarianceAllocation(hist)
        print budget_strategy

    def test_generate_points(self):
        res = line(10, start=0, end=10, slope=-.01, intercept=1.1)
        s = ''
        for r in res:
            s += ','.join(map(str, r)) + '\n'

        with open('points.xls', 'w') as f:
            f.write(s)

def scale(values, lower, upper):
    val_range = upper - lower
    result = [lower + val*val_range for val in values]
    return result

def sigmoid_curve(number_of_points, speed=1):
    xy = [[x, 1 / (1 + math.exp(speed*-x))] for x in np.linspace(-2,2,number_of_points)]
    return xy

def normal_curve(number_of_points, left_tail=-2, right_tail=2):
    xy = [[x, 1 / (.399*math.sqrt(2*math.pi)) * math.exp (-(x**2)/(2*.399**2))]
         for x in np.linspace(left_tail,right_tail,number_of_points)]
    return xy

def line(number_of_points, start=0, end=1, slope=1, intercept=0):
    xy = [[x, slope*x+intercept] for x in np.linspace(start,end,number_of_points)]
    return xy

