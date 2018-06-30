
import numpy as np

rx1_o = 11.801208
ry1_o = 8.6773586

rx1_s = 13.5
ry1_s = 10.5

def A(rx,ry):
    return rx*ry*np.pi

A1_before = A(rx1_o,ry1_o)
A1_stdp   = A(rx1_s,ry1_s)

dA_stdp = A1_stdp-A1_before

rx2_o = 7
ry2_o = 5

def infer_second_r(rx_o, ry_o, r_new, dA):
    target_A = A(rx_o,ry_o) + dA
    ry_new = target_A/(np.pi*r_new)
    return ry_new

r_new = 9.5
print(infer_second_r(rx2_o, ry2_o, r_new, dA_stdp))


rx3_o = 15.25
ry3_o = 12

r_new = 16.85
print(infer_second_r(rx3_o, ry3_o, r_new, dA_stdp))


#height_arrow = 9.828+21.608
height_arrow = 21.608+7

def get_orange_rect_height(rx_o, ry_o, dA_stdp):
    return dA_stdp/(A(rx_o, ry_o)+dA_stdp)*height_arrow

print(get_orange_rect_height(rx1_o, ry1_o, dA_stdp))
print(get_orange_rect_height(rx2_o, ry2_o, dA_stdp))
print(get_orange_rect_height(rx3_o, ry3_o, dA_stdp))

print(0.25/1.25*height_arrow)


    

