import math

def calculate_thermal_feeling(tuple):
    t = float(tuple['TEMPERATURA'])
    v = float(tuple['VELOCIDA VIENTO (m/s)'])
    st =  13.12 + 0.6215*t - 11.37*(math.pow(v,0.16)) +0.3965*t*(math.pow(v,0.16))
    return st