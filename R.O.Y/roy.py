import random as r

def roy_create_rand(count_roy,lim):
    count = len(lim)
    res = [[] for i in range(count)]
    for j in range(count_roy):
        for i in range(count):
            res[i].append(r.uniform(lim[i][0], lim[i][1]))
    return res

def speed(omega, v_start, a1, a2, local_r, global_r, x):
    return omega * v_start + a1 * r.uniform(0, 1) * (local_r - x) + a2 * r.uniform(0, 1) * (global_r - x)

def moving(x_start, v):
    return x_start + v

def operation(a1, a2, omega,v_max, v_start_x, x_start, local_x, global_x):
    v_end_x = speed(omega, v_start_x, a1, a2, local_x, global_x, x_start)

    if v_end_x > v_max:
        v_end_x = v_max
    if abs(v_end_x) > v_max and v_end_x < 0:
        v_end_x = -v_max

    x_end = x_start + v_end_x

    return x_end, v_end_x