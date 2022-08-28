# testing my_atan
# let's divide a circle into max points
max = 100;
r = 10;
rad=0;
debug=0;
delta_rad = 4 * np.pi/max;
x_array = [];
y_array = [];
for i in range(0, max):
    if (debug): print("--------",i,"---------------");
    x_pt = r * np.cos(rad);
    y_pt = r * np.sin(rad);
    if (debug): print("delta_x=",x_pt, "  delta_y=", y_pt);
    calc_rad = my_atan(y_pt, x_pt)
    if (debug): print("rad=",rad," calc_rad=",calc_rad, "  diff=",(rad-calc_rad));
    x_pt2 = r * np.cos(calc_rad);
    y_pt2 = r * np.sin(calc_rad);
    if (debug): print("delta_x2=",x_pt2, "  delta_y2=", y_pt2);
    if (debug): print("diff_x:",(x_pt2-x_pt),"  diff_y:",(y_pt2-y_pt));

    x_array.append(x_pt);
    y_array.append(y_pt);
    rad += delta_rad;
    # if (rad > np.pi): rad -= 2*np.pi

    

plt.scatter(x_array, y_array, marker ="+", linewidths = 1)
plt.show()
