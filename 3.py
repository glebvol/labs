import matplotlib.pyplot as plt
from prettytable import PrettyTable
import math


M = 2150
m = 1000
M = M + m
v_r = 3660.0
g_lunar = 1.62
v_land = 3.0
a_max = 29.43
y_start = -4.0
y_end = 4.0
S = 250 * 1000

table = PrettyTable()
table.field_names = ['v_x', 'v_y', 'x', 'y', 'alpha', 'delta m', 't']



def predict_coordinates(cur_x, cur_y, cur_v_x, cur_v_y, M, angle, dm, t, cur_time):
    table.add_row([cur_v_x, cur_v_y, cur_x, cur_y, angle, dm, t])
    dt = 1
    epochs = t / dt
    for i in range(int(epochs)):
        time = dt * (i + 1)
        ts.append(cur_time + time)

        a, a_x, a_y, v_x, v_y, x, y = predict(cur_x, cur_y, cur_v_x, cur_v_y, M, angle, dm, time)

        a_s.append(a)
        a_xs.append(a_x)
        a_ys.append(a_y)
        xs.append(x)
        ys.append(y)
        v_xs.append(v_x)
        v_ys.append(v_y)

    a, a_x, a_y, v_x, v_y, x, y = predict(cur_x, cur_y, cur_v_x, cur_v_y, M, angle, dm, t)
    M = M - dm * t
    return x, y, v_x, v_y, M, t + cur_time


def predict(x, y, v_x, v_y, M, angle, dm, dt):
    angle = math.radians(angle)
    a_x = v_r * math.sin(angle) * dm / (M - dm * dt)
    a_y = v_r * math.cos(angle) * dm / (M - dm * dt) - g_lunar
    a = math.sqrt(a_x * a_x + a_y * a_y)
    if dm == 0:
        x = x + dt * v_x
        y = y + dt * v_y - g_lunar * dt * dt / 2
        v_y = v_y - g_lunar * dt
    else:
        y = y + dt * v_y + v_r * math.cos(angle) * (
                math.log(M / (M - dm * dt)) * (dt - M / dm) + dt) - g_lunar * dt * dt / 2
        x = x + dt * v_x + v_r * math.sin(angle) * (math.log(M / (M - dm * dt)) * (dt - M / dm) + dt)
        v_y = v_y - g_lunar * dt + (v_r * math.cos(angle)) * (math.log(M) - math.log(M - dm * dt))

    v_x = v_x + v_r * math.sin(angle) * (math.log(M) - math.log(M - dm * dt))
    return a, a_x, a_y, v_x, v_y, x, y


a_final = a_max * 0.9
y_leg = g_lunar + a_final / math.sqrt(2)
x_leg = a_final / math.sqrt(2)
angle = int(math.degrees(math.atan(x_leg / y_leg)))

dm = M * a_final / v_r

fuel_percent = 0.51

time_acceleration = (M - 2150) * fuel_percent / dm

ts = [0]
xs = [0.0]
ys = [y_start]
v_xs = [0.0]
v_ys = [0.0]
a_xs = [0.0]
a_ys = [0.0]
a_s = [0.0]

x = 0.0
y = y_start
v_x = 0.0
v_y = 0.0


x, y, v_x, v_y, M, t = predict_coordinates(x, y, v_x, v_y, M, 42, 21, 24.5, 0)

time = int(2 * v_y / g_lunar)


x, y, v_x, v_y, M, t = predict_coordinates(x, y, v_x, v_y, M, 0, 0, time, t)


x, y, v_x, v_y, M, t = predict_coordinates(x, y, v_x, v_y, M, -43, 20, 12, t)

x, y, v_x, v_y, M, t = predict_coordinates(x, y, v_x, v_y, M, -43, 19, 6, t)

x, y, v_x, v_y, M, t = predict_coordinates(x, y, v_x, v_y, M, -43, 18, 3, t)


cur_x = x
cur_y = y
cur_v_x = v_x
cur_v_y = v_y
cur_M = M
cur_time = round((2 * (250000 - x) / cur_v_x), 1)
acc_x = cur_v_x / cur_time
acc = a_max / 15
dm = round(M * acc / v_r, 1)
angle = round(math.degrees(math.asin(acc_x / acc)))


x, y, v_x, v_y, M, t = predict_coordinates(x, y, v_x, v_y, M, -15, 1.6, 23.5, t)

x, y, v_x, v_y, M, t = predict_coordinates(x, y, v_x, v_y, M, 0, 0, 3, t)


while y > y_end:
    dm = round(g_lunar * M / v_r, 1)
    if v_y < -3.5:
        dm = round(dm * 1.1, 1)
    if v_y < -10:
         dm = round(dm * 1.1, 1)

    cur_angle = 0
    time_per_maneuver = 1
    x, y, v_x, v_y, M, t = predict_coordinates(x, y, v_x, v_y, M, 0, dm, time_per_maneuver, t)
table.add_row([v_x, v_y, x, y_end, 0, 0, 0])
print(table)

plt.plot(ts, v_xs)
plt.ylabel('v_x')
plt.xlabel('time')
plt.show()

plt.plot(ts, v_ys)
plt.ylabel('v_y')
plt.xlabel('time')
plt.show()


plt.plot(xs, ys)
plt.ylabel('y coordinate')
plt.xlabel('x coordinate')
plt.show()

plt.plot(ts, a_s)
plt.ylabel('acceleration')
plt.xlabel('time')
plt.show()
