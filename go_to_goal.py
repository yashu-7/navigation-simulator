import math

def linear_angular(x,y,g_x,g_y):
    distance = math.sqrt((x-g_x)**2 + (y-g_y)**2)
    orientation = math.atan2(g_y-y,g_x-x)
    
    return distance,orientation

def move_towards_goal(robo, ori):
    angle_diff = (math.degrees(ori) - robo.angle + 180) % 360 - 180
    
    if abs(angle_diff) > robo.turn_rate:
        robo.angle += robo.turn_rate * (1 if angle_diff > 0 else -1)
    else:
        robo.angle += angle_diff  
    
    robo.angle = robo.angle % 360 
    
    vel_x = robo.vel * math.cos(math.radians(robo.angle))
    vel_y = robo.vel * math.sin(math.radians(robo.angle))
    
    robo.x += vel_x
    robo.y += vel_y

    return robo.x,robo.y