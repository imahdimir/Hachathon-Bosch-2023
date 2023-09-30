"""

    """

from pathlib import Path

import pandas as pd
import numpy as np

class FPN :
    dta = 'DevelopmentData.xlsx'

class Cols :
    rx1 = 'FirstObjectDistance_X'
    ry1 = 'FirstObjectDistance_Y'
    rx2 = 'SecondObjectDistance_X'
    ry2 = 'SecondObjectDistance_Y'
    rx3 = 'ThirdObjectDistance_X'
    ry3 = 'ThirdObjectDistance_Y'
    rx4 = 'FourthObjectDistance_X'
    ry4 = 'FourthObjectDistance_Y'

    v = 'VehicleSpeed'

    rvx1 = 'FirstObjectSpeed_x'
    rvy1 = 'FirstObjectSpeed_y'
    rvx2 = 'SecondObjectSpeed_x'
    rvy2 = 'SecondObjectSpeed_y'
    rvx3 = 'ThirdObjectSpeed_x'
    rvy3 = 'ThirdObjectSpeed_y'
    rvx4 = 'FourthObjectSpeed_x'
    rvy4 = 'FourthObjectSpeed_y'

    yr = 'YawRate'
    t = 'Timestamp'

    dt = 'Delta_T'
    da = 'Delta_Angle'
    a = 'Angle'
    vx = 'VehicleSpeed_X'
    vy = 'VehicleSpeed_Y'
    dx = 'Delta_X'
    dy = 'Delta_Y'
    x = 'Vehicle_X'
    y = 'Vehicle_Y'

    x1 = 'Object1_X'
    y1 = 'Object1_Y'
    x2 = 'Object2_X'
    y2 = 'Object2_Y'
    x3 = 'Object3_X'
    y3 = 'Object3_Y'
    x4 = 'Object4_X'
    y4 = 'Object4_Y'

    vx1 = 'Object1Speed_x'
    vy1 = 'Object1Speed_y'
    vx2 = 'Object2Speed_x'
    vy2 = 'Object2Speed_y'
    vx3 = 'Object3Speed_x'
    vy3 = 'Object3Speed_y'
    vx4 = 'Object4Speed_x'
    vy4 = 'Object4Speed_y'

fpn = FPN()
c = Cols()

def main() :
    pass

    ##
    df = pd.read_excel(fpn.dta , index_col = 0)

    ##
    # assert time is monotonic increasing and unique across dataset
    assert df[c.t].is_monotonic_increasing
    assert df[c.t].is_unique

    ##
    # calculate delta time
    df[c.dt] = df[c.t].diff()

    ##
    # calculate delta angle
    df[c.da] = df[c.yr] * df[c.dt]

    ##
    # calculate angle
    df[c.a] = df[c.da].cumsum()

    ##
    # calculate vehicle speed x and y
    df[c.vx] = df[c.v] * np.cos(df[c.a])
    df[c.vy] = df[c.v] * np.sin(df[c.a])

    ##
    # calculate delta x and y
    df[c.dx] = df[c.vx] * df[c.dt]
    df[c.dy] = df[c.vy] * df[c.dt]

    ##
    # calculate x and y
    df[c.x] = df[c.dx].cumsum()
    df[c.y] = df[c.dy].cumsum()

    ##
    # calculate objects x positions (absolute)
    duo = {
            c.x1 : c.rx1 ,
            c.x2 : c.rx2 ,
            c.x3 : c.rx3 ,
            c.x4 : c.rx4 ,
            }

    for ax , rx in zip(duo.keys() , duo.values()) :
        df[ax] = df[c.x] + df[rx]

    ##
    # calculate objects y positions (absolute)
    duo = {
            c.y1 : c.ry1 ,
            c.y2 : c.ry2 ,
            c.y3 : c.ry3 ,
            c.y4 : c.ry4 ,
            }

    for ay , ry in zip(duo.keys() , duo.values()) :
        df[ay] = df[c.y] + df[ry]

    ##
    # calculate objects x speeds (absolute)
    duo = {
            c.vx1 : c.rvx1 ,
            c.vx2 : c.rvx2 ,
            c.vx3 : c.rvx3 ,
            c.vx4 : c.rvx4 ,
            }

    for avx , rvx in zip(duo.keys() , duo.values()) :
        df[avx] = df[rvx] + df[c.vx]

    ##
    # calculate objects y speeds (absolute)
    duo = {
            c.vy1 : c.rvy1 ,
            c.vy2 : c.rvy2 ,
            c.vy3 : c.rvy3 ,
            c.vy4 : c.rvy4 ,
            }

    for avy , rvy in zip(duo.keys() , duo.values()) :
        df[avy] = df[rvy] + df[c.vy]

    ##
    
    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


def test() :
    pass

    ##

    ##

    ##
