from matplotlib import pyplot as plt
from nodepy import rk, semidisc, lm


rk4 = rk.loadRKM('RK44')
alpha = [0.1111111111, 0.55555555556, 0.33333333333]
beta = [0, 0, -1.777777777778]
# lm3 = lm.LinearMultistepMethod(alpha=alpha, beta=beta)
ab3=lm.Adams_Bashforth(3)
upwind = semidisc.upwind_advection_matrix(100,dx=0.1)


ab3.plot_stability_region()