# W1 노트 — 지배방정식과 일반 수송방정식

## 1. 세 보존식 (식 + 각 항의 물리적 의미 한 줄)
- 연속: 

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0
$$

  - $\partial \rho / \partial t$: 한 점에서 밀도가 시간에 따라 변하는 양
  - $\nabla \cdot (\rho \mathbf{u})$: 그 점에서 빠져나가는 순 질량 유속
- 운동량:

$$
\frac{\partial (\rho \mathbf{u})}{\partial t} + \nabla \cdot (\rho \mathbf{uu}) = -\nabla p + \nabla \cdot \tau + \mathbf{f}
$$

  - $\partial (\rho \mathbf{u})/ \partial t$: 단위 체적당 운동량의 시간 변화율
  - $\nabla \cdot (\rho \mathbf{uu})$: 그 점에서 대류로 빠져나가는 순 운동량
  - $-\nabla p$: 압력구배가 만드는 힘(단위체적당 표면력)
  - $\nabla \cdot \tau$: 점성항
  - $\mathbf{f}$: 체적력(중력, 부력)
- 에너지:

$$
\rho c_p (\frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T) = k \nabla^2 T + \Phi + \dot{q}
$$

  - $\frac{\partial T}{\partial t}$: 온도의 시간 변화율
  - $\mathbf{u} \cdot \nabla T$: 대류로 빠져나가는 에너지량
  - $k \nabla^2 T$: 전도항
  - $\Phi$: 점성 마찰이 유체의 운동에너지를 열로 바꾸는 양. 항상 ≥ 0.
  - $\dot{q}$: 생성되는 발열(체적열)

## 2. 일반 수송방정식

$$
\frac{\partial (\rho \phi)}{\partial t} + \nabla \cdot (\rho \mathbf{u} \phi) = \nabla \cdot (\Gamma \nabla \phi) + S_\phi
$$

  - $\partial (\rho \phi) / \partial t$: 시간항
  - $\nabla \cdot (\rho \mathbf{u} \phi)$: 대류항
  - $\nabla \cdot (\Gamma \nabla \phi)$: 확산항
  - $S_\phi$: 생성항

| 보존량 | φ | Γ | Sφ |
|---|---|---|---|
| 질량 | 1 | 0 | 0 |
| 운동량(x) | u | μ | −∂p/∂x + fx |
| 에너지 | T | k/cp | (Φ+q̇)/cp |

## 3. 코드로 확인한 것
- u_max 수치 vs 이론: 0.012500 vs 0.012500 m/s (일치)
- Q 수치 vs 이론: 8.332500e-05 vs 8.333333e-05 m²/s (상대오차 1e-4)
- 차이가 나는 이유: 실제 속도 그래프는 포물선을 그리며 올라가는데 사다리꼴은 그 보다 적은 면적을 표현하기 때문에 수치값이 이론값보다 작았어.

## 4. 자가점검 질문 답 (학습서 W1)
1. 적분형 셀 사이의 이동이 상쇄
2. 질량보존을 지키는 속도를 정하는 역할
3. 대류, 대류가 지배적인 상황에서 중심차분을 쓰면 값이 진동 따라서 upwind 사용
4. Re = 관성 ÷ 점성
    - Re 100: 점성이 상대적으로 큼 → 흐름이 매끈하고 단순할 것
    - Re 1000: 관성이 큼 → 흐름이 더 복잡하고, 벽 근처 변화가 급할 것