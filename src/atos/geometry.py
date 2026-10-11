import math

def eccentric_offset(e1_mm, e2_mm, theta_deg):
    if e1_mm<0 or e2_mm<0: raise ValueError('eccentricities must be non-negative')
    theta=math.radians(theta_deg); x=e1_mm+e2_mm*math.cos(theta); y=e2_mm*math.sin(theta); mag=math.hypot(x,y)
    return {'x_mm':x,'y_mm':y,'magnitude_mm':mag,'direction_deg':math.degrees(math.atan2(y,x)) if mag else 0.0,'theoretical_min_mm':abs(e1_mm-e2_mm),'theoretical_max_mm':e1_mm+e2_mm}
