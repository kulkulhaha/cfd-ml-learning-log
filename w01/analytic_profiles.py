"""W1: 해석해 두 개 - 평행판 포아즈이유 유동, 1D 정상 열전도."""
from pathlib import Path

import numpy as np


def poiseuille_u(y, mu, dpdx, h):
    """평행판 사이 속도 u(y) [m/s]."""
    # TODO 1: 학습서의 u(y) 식을 코드로 옮긴다
    uy = -dpdx*(h*y-y*y)/(2*mu)
    return uy


def u_max_theory(mu, dpdx, h):
    """최대 속도의 이론값 [m/s]."""
    # TODO 2: du/dy = 0 인 위치를 찾아 u(y)에 대입한 식
    return poiseuille_u(h/2, mu, dpdx, h)


def flow_rate(y, u):
    """단위 폭당 유량 Q = ∫ u dy [m^2/s], 수치 적분."""
    # TODO 3: 사다리꼴 공식으로 적분
    return np.trapezoid(u, y)


def flow_rate_theory(mu, dpdx, h):
    """단위 폭당 유량의 이론값 [m^2/s]."""
    return (-dpdx) * h**3 / (12.0 * mu)


def conduction_T(x, T0, T1, L):
    """1D 정상 열전도(생성항 없음) 온도 T(x), T(0)=T0, T(L)=T1."""
    # TODO 4: 직선 분포
    return T0 + x*(T1-T0)/L


def main():
    import matplotlib.pyplot as plt

    mu, dpdx, h = 1.0e-3, -1.0, 0.01        # Pa·s, Pa/m, m
    y = np.linspace(0.0, h, 101)
    u = poiseuille_u(y, mu, dpdx, h)

    L, T0, T1 = 1.0, 100.0, 20.0            # m, °C, °C
    x = np.linspace(0.0, L, 101)
    T = conduction_T(x, T0, T1, L)

    print(f"u_max (numeric) = {u.max():.6f} m/s")
    print(f"u_max (theory)  = {u_max_theory(mu, dpdx, h):.6f} m/s")
    print(f"Q (trapezoid)   = {flow_rate(y, u):.6e} m^2/s")
    print(f"Q (theory)      = {flow_rate_theory(mu, dpdx, h):.6e} m^2/s")

    fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
    ax[0].plot(u, y * 1e3)
    ax[0].set_xlabel("u [m/s]"); ax[0].set_ylabel("y [mm]")
    ax[0].set_title("Poiseuille flow (analytic)")
    ax[1].plot(x, T)
    ax[1].set_xlabel("x [m]"); ax[1].set_ylabel("T [°C]")
    ax[1].set_title("1D steady conduction (analytic)")
    fig.tight_layout()

    out = Path(__file__).with_name("analytic_profiles.png")
    fig.savefig(out, dpi=150)
    print(f"그림 저장: {out}")


if __name__ == "__main__":
    main()