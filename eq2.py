import sympy as sp
from util.interfaces import Config, EqInfo, Hyperparameters, VarInfo
from main import run

a = 1

config = Config(
  eq = EqInfo(
    name = 'u',
    function = lambda s: s.dudx2 + s.dudy2 + s.dudy ** 2 - 2 * s.y + s.x ** 4,
  ),
  vars = {
    'x': VarInfo(bounds=(-1, 1), integrable=False),
    'y': VarInfo(bounds=(-1, 1), integrable=False),
  },
  conditions = [
    (1., lambda s: s.u.subs(s.x, 0)),
    (1., lambda s: s.u.subs(s.x, 1) - s.y - a),
    (1., lambda s: s.u.subs(s.y, 0) - a * s.x),
    (1., lambda s: s.u.subs(s.y, 1) - s.x * (s.x + a))
  ],
  preoperations = [],
  operations = [
    lambda z: 0,
    lambda z: 1,
    lambda z: z,
    lambda z: -z,
    lambda z: 1 + z,
    lambda z: -z,
    lambda z: z**2,
    lambda z: z**3,
    lambda z: sp.exp(z) + 0,
  ],
  hyperparameters = Hyperparameters(
    lr = 0.0001,
    cellcount = 4,
  ),
  epochs = 10,
  batchsize = 16,
  verbosity = 1,
)

run(config)
