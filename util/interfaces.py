from dataclasses import dataclass
from typing import Callable, Sequence, Tuple
import sympy as sp

Numeric = float | int # TODO: add jax numeric type
SymbolicNumeric = Numeric | sp.Expr

@dataclass
class EqInfo:
    name: str
    function: Callable[[dict[str, sp.Expr]], sp.Expr]

@dataclass
class VarInfo:
    bounds: Tuple[Numeric, Numeric]
    integrable: bool

@dataclass
class Hyperparameters:
    lr: Numeric
    cellcount: int

@dataclass
class Config:
    eq: EqInfo
    vars: dict[str, VarInfo]
    conditions: Sequence[tuple[Numeric, Callable[[dict[str, sp.Expr]], sp.Expr]]]
    preoperations: Sequence[Callable[..., SymbolicNumeric]]
    operations: Sequence[Callable[[SymbolicNumeric], SymbolicNumeric]]
    hyperparameters: Hyperparameters
    epochs: int
    batchsize: int
    verbosity: int