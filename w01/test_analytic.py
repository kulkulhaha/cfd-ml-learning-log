"""W1 테스트: pytest w01 -v 로 실행한다."""
import numpy as np
import pytest

from analytic_profiles import (conduction_T, flow_rate, flow_rate_theory,
                               poiseuille_u, u_max_theory)

MU, DPDX, H = 1.0e-3, -1.0, 0.01


def test_no_slip_at_walls():
    # 벽(y=0, y=h)에서 속도 0
    u = poiseuille_u(np.array([0.0, H]), MU, DPDX, H)
    assert u == pytest.approx([0.0, 0.0], abs=1e-12)


def test_max_at_center():
    # 최대 속도는 중앙 y=h/2에서, 값은 0.0125 m/s
    y = np.linspace(0.0, H, 101)
    u = poiseuille_u(y, MU, DPDX, H)
    assert y[np.argmax(u)] == pytest.approx(H / 2)
    assert u.max() == pytest.approx(u_max_theory(MU, DPDX, H), rel=1e-12)
    assert u_max_theory(MU, DPDX, H) == pytest.approx(0.0125)


def test_flow_rate_matches_theory():
    # 사다리꼴 적분 유량이 이론값 h^3(-dp/dx)/(12 mu)와 0.1% 이내로 일치
    y = np.linspace(0.0, H, 101)
    u = poiseuille_u(y, MU, DPDX, H)
    assert flow_rate(y, u) == pytest.approx(flow_rate_theory(MU, DPDX, H), rel=1e-3)


def test_conduction_endpoints_and_linear():
    # 양 끝 온도가 경계조건과 같고, 기울기가 일정
    x = np.linspace(0.0, 1.0, 11)
    T = conduction_T(x, 100.0, 20.0, 1.0)
    assert T[0] == pytest.approx(100.0)
    assert T[-1] == pytest.approx(20.0)
    assert np.diff(T) == pytest.approx(np.full(10, -8.0))