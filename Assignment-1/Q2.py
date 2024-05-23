import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.lines import Line2D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Defining the vertices of the first cube
p1 = [0,0,0]
p2 = [1,0,0]
p3 = [1,1,0]
p4 = [0,1,0]
p5 = [0,0,1]
p6 = [1,0,1]
p7 = [1,1,1]
p8 = [0,1,1]

vertices1 = [
    p1,p2,p3,p4,p5,p6,p7,p8
]

# Defining the faces of the first cube using the vertices
faces1 = [
    [vertices1[0], vertices1[1], vertices1[2], vertices1[3]],
    [vertices1[4], vertices1[5], vertices1[6], vertices1[7]],
    [vertices1[0], vertices1[1], vertices1[5], vertices1[4]],
    [vertices1[2], vertices1[3], vertices1[7], vertices1[6]],
    [vertices1[1], vertices1[2], vertices1[6], vertices1[5]],
    [vertices1[0], vertices1[3], vertices1[7], vertices1[4]]
]

#Question 2(i)
a = 0.2
p1_ = [x + y for x, y in zip(p1, [a*p1[0],0,0])]
p2_ = [x + y for x, y in zip(p2, [a*p2[0],0,0])]
p3_ = [x + y for x, y in zip(p3, [a*p3[0],0,0])]
p4_ = [x + y for x, y in zip(p4, [a*p4[0],0,0])]
p5_ = [x + y for x, y in zip(p5, [a*p5[0],0,0])]
p6_ = [x + y for x, y in zip(p6, [a*p6[0],0,0])]
p7_ = [x + y for x, y in zip(p7, [a*p7[0],0,0])]
p8_ = [x + y for x, y in zip(p8, [a*p8[0],0,0])]

# #Question 2(ii)
# a = 0.2
# b = 0.1
# p1_ = [x + y for x, y in zip(p1, [a*p1[0],-b*p1[1],-b*p1[2]])]
# p2_ = [x + y for x, y in zip(p2, [a*p2[0],-b*p2[1],-b*p2[2]])]
# p3_ = [x + y for x, y in zip(p3, [a*p3[0],-b*p3[1],-b*p3[2]])]
# p4_ = [x + y for x, y in zip(p4, [a*p4[0],-b*p4[1],-b*p4[2]])]
# p5_ = [x + y for x, y in zip(p5, [a*p5[0],-b*p5[1],-b*p5[2]])]
# p6_ = [x + y for x, y in zip(p6, [a*p6[0],-b*p6[1],-b*p6[2]])]
# p7_ = [x + y for x, y in zip(p7, [a*p7[0],-b*p7[1],-b*p7[2]])]
# p8_ = [x + y for x, y in zip(p8, [a*p8[0],-b*p8[1],-b*p8[2]])]

# #Question 2(iii)
# a = 0.2
# p1_ = [x + y for x, y in zip(p1, [-a*p1[0],-a*p1[1],-a*p1[2]])]
# p2_ = [x + y for x, y in zip(p2, [-a*p2[0],-a*p2[1],-a*p2[2]])]
# p3_ = [x + y for x, y in zip(p3, [-a*p3[0],-a*p3[1],-a*p3[2]])]
# p4_ = [x + y for x, y in zip(p4, [-a*p4[0],-a*p4[1],-a*p4[2]])]
# p5_ = [x + y for x, y in zip(p5, [-a*p5[0],-a*p5[1],-a*p5[2]])]
# p6_ = [x + y for x, y in zip(p6, [-a*p6[0],-a*p6[1],-a*p6[2]])]
# p7_ = [x + y for x, y in zip(p7, [-a*p7[0],-a*p7[1],-a*p7[2]])]
# p8_ = [x + y for x, y in zip(p8, [-a*p8[0],-a*p8[1],-a*p8[2]])]

# #Question 2(iv)
# a = 0.2
# p1_ = [x + y for x, y in zip(p1, [a*p1[1],0,0])]
# p2_ = [x + y for x, y in zip(p2, [a*p2[1],0,0])]
# p3_ = [x + y for x, y in zip(p3, [a*p3[1],0,0])]
# p4_ = [x + y for x, y in zip(p4, [a*p4[1],0,0])]
# p5_ = [x + y for x, y in zip(p5, [a*p5[1],0,0])]
# p6_ = [x + y for x, y in zip(p6, [a*p6[1],0,0])]
# p7_ = [x + y for x, y in zip(p7, [a*p7[1],0,0])]
# p8_ = [x + y for x, y in zip(p8, [a*p8[1],0,0])]

# #Question 2(v)
# a = 0.2
# p1_ = [x + y for x, y in zip(p1, [a*p1[1],a*p1[0],0])]
# p2_ = [x + y for x, y in zip(p2, [a*p2[1],a*p2[0],0])]
# p3_ = [x + y for x, y in zip(p3, [a*p3[1],a*p3[0],0])]
# p4_ = [x + y for x, y in zip(p4, [a*p4[1],a*p4[0],0])]
# p5_ = [x + y for x, y in zip(p5, [a*p5[1],a*p5[0],0])]
# p6_ = [x + y for x, y in zip(p6, [a*p6[1],a*p6[0],0])]
# p7_ = [x + y for x, y in zip(p7, [a*p7[1],a*p7[0],0])]
# p8_ = [x + y for x, y in zip(p8, [a*p8[1],a*p8[0],0])]

# #Question 2(vi)
# a = 0.2
# p1_ = [x + y for x, y in zip(p1, [a*(p1[1]+p1[2]),a*(p1[0]+p1[2]),a*(p1[0]+p1[1])])]
# p2_ = [x + y for x, y in zip(p2, [a*(p2[1]+p2[2]),a*(p2[0]+p2[2]),a*(p2[0]+p2[1])])]
# p3_ = [x + y for x, y in zip(p3, [a*(p3[1]+p3[2]),a*(p3[0]+p3[2]),a*(p3[0]+p3[1])])]
# p4_ = [x + y for x, y in zip(p4, [a*(p4[1]+p4[2]),a*(p4[0]+p4[2]),a*(p4[0]+p4[1])])]
# p5_ = [x + y for x, y in zip(p5, [a*(p5[1]+p5[2]),a*(p5[0]+p5[2]),a*(p5[0]+p5[1])])]
# p6_ = [x + y for x, y in zip(p6, [a*(p6[1]+p6[2]),a*(p6[0]+p6[2]),a*(p6[0]+p6[1])])]
# p7_ = [x + y for x, y in zip(p7, [a*(p7[1]+p7[2]),a*(p7[0]+p7[2]),a*(p7[0]+p7[1])])]
# p8_ = [x + y for x, y in zip(p8, [a*(p8[1]+p8[2]),a*(p8[0]+p8[2]),a*(p8[0]+p8[1])])]


# Plotting the first cube
cube1 = Poly3DCollection(faces1, linewidths=1, edgecolors='blue', facecolors='white', alpha=0.1)
ax.add_collection3d(cube1)

vertices2 = [
    p1_,p2_,p3_,p4_,p5_,p6_,p7_,p8_
]


# Defining the faces of the second cube using the vertices
faces2 = [
    [vertices2[0], vertices2[1], vertices2[2], vertices2[3]],
    [vertices2[4], vertices2[5], vertices2[6], vertices2[7]],
    [vertices2[0], vertices2[1], vertices2[5], vertices2[4]],
    [vertices2[2], vertices2[3], vertices2[7], vertices2[6]],
    [vertices2[1], vertices2[2], vertices2[6], vertices2[5]],
    [vertices2[0], vertices2[3], vertices2[7], vertices2[4]]
]

# Plotting the second cube
cube2 = Poly3DCollection(faces2, linewidths=2, edgecolors='blue', facecolors='white', alpha=0.1)
ax.add_collection3d(cube2)

#Arrows, legends and etc modifications
arrow_length = 0.4
ax.quiver(0, 0, 0, 0.4, 0, 0, color='black', arrow_length_ratio=0.25, linewidth=3)
ax.quiver(0, 0, 0, 0, 0.4, 0, color='black', arrow_length_ratio=0.25, linewidth=3)
ax.quiver(0, 0, 0, 0, 0, 0.4, color='black', arrow_length_ratio=0.25, linewidth=3)
legend_elements = [
    Line2D([0], [0], color='blue', lw=1, label='Initial cube'),
    Line2D([0], [0], color='blue', lw=3, label='Deformed cube')
]
ax.legend(handles=legend_elements)
ax.set_xlim(0, 1.5)
ax.set_ylim(0, 1.5)
ax.set_zlim(0, 1.5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
arrow_label_offset = 0.15
ax.text(arrow_length + arrow_label_offset, 0, 0, "X", color='black', fontsize=10, ha='right')
ax.text(0, arrow_length + arrow_label_offset, 0, "Y", color='black', fontsize=10, ha='right')
ax.text(0, 0, arrow_length + arrow_label_offset, "Z", color='black', fontsize=10, ha='right')
plt.show()
