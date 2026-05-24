import matplotlib.pyplot as plt
import numpy as np

def f(U):
    Umin = 1
    if U < Umin:
        U = Umin
    U0 = 1.2
    U1 = 2
    f0 = 1
    f1 = 1.8

    # f(U) is mostly linear
    return (U - U0) / (U1 - U0) * (f1 - f0) + f0


def voltage(f):
    f0, f1 = 1.0, 1.8
    U0, U1 = 1.2, 2.0
    if f <= f0:
        return U0
    elif f >= f1:
        return U1
    else:
        # f(U) is mostly linear
        return U0 + (U1 - U0) * (f - f0) / (f1 - f0)

def power(C, f):
    U = voltage(f)
    return C * U * U * f

Ceff, Cperf = 1.0, 4.0
IPCeff, IPCperf = 1.0, 2.0

P_min = 0.0

P_vals = np.linspace(0.01, 3.0, 500)

power_eff = []
power_perf = []
for P in P_vals:
    f_eff = P / IPCeff
    if f_eff > 1.8:
        power_eff.append(np.inf)
    else:
        power_eff.append(power(Ceff, f_eff))
    
    f_perf = P / IPCperf
    if f_perf > 1.8:
        power_perf.append(np.inf)
    else:
        power_perf.append(power(Cperf, f_perf))

power_best = np.minimum(power_eff, power_perf)

plt.plot(P_vals, power_eff, '--', label='Efficient core')
plt.plot(P_vals, power_perf, '--', label='Performance core')
plt.plot(P_vals, power_best, 'g-.', label='Best')
plt.xlabel('Performance')
plt.ylabel('Power')
plt.legend()
plt.grid(True)
plt.savefig("Plot.png")
