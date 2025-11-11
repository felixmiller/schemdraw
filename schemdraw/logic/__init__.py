from .logic import DsBuf, DsNot, DsAnd, DsOr, DsNand, DsNor, DsXor, DsXnor, IecLogicGate, IecBuf, IecNot, IecAnd, IecNand, IecOr, IecNor, IecXor, IecXnor, And, Nand, Or, Nor, Xor, Xnor, Buf, Not, NotNot, Tristate, Tgate, Schmitt, SchmittNot, SchmittAnd, SchmittNand
from .kmap import Kmap
from .table import Table
from .timing import TimingDiagram
from ..elements import Arrow, Arrowhead, Dot, Line, Wire, Arc2, Arc3, ArcLoop

__all__ = ['DsBuf', 'DsNot', 'DsAnd', 'DsOr', 'DsNand', 'DsNor', 'DsXor', 'DsXnor'
           'IecLogicGate', 'IecBuf', 'IecNot', 'IecAnd', 'IecNand', 'IecOr', 'IecNor', 'IecXor', 'IecXnor',
           'And', 'Nand', 'Or', 'Nor', 'Xor', 'Xnor', 'Buf', 'Not', 'NotNot', 'Tristate', 'Tgate', 'Schmitt', 'SchmittNot',
           'SchmittAnd', 'SchmittNand', 'Kmap', 'Table', 'TimingDiagram', 'Arrow', 'Arrowhead', 'Dot', 'Line',
           'Wire', 'Arc2', 'Arc3', 'ArcLoop']

STYLE_DS = {'Not': DsNot,
            'Buf': DsBuf,
            'And': DsAnd,
            'Or': DsOr,
            'Nand': DsNand,
            'Nor': DsNor,
            'Xor': DsXor,
            'Xnor': DsXnor}
STYLE_IEC = { 'Not': IecNot,
              'Buf': IecBuf,
              'And': IecAnd,
              'Or': IecOr,
              'Nand': IecNand,
              'Nor': IecNor,
              'Xor': IecXor,
              'Xnor': IecXnor}


def style(style):
    ''' Set global element style

        Args:
            style: dictionary of elementname: Element
            to change the element module namespace.
            Use `elements.STYLE_DS` or `elements.STYLE_IEC`
            to define U.S./Distinctive Shape or European/IEC
            element styles.
    '''
    for name, element in style.items():
        globals()[name] = element
