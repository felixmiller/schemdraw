from .logic import AndDS, AndIEC, NandDS, NandIEC, OrDS, OrIEC, NorDS, NorIEC, XorDS, XorIEC, XnorDS, XnorIEC, Buf, Not, NotNot, Tristate, Tgate, Schmitt, SchmittNot, SchmittAnd, SchmittNand
from .kmap import Kmap
from .table import Table
from .timing import TimingDiagram
from ..elements import Arrow, Arrowhead, Dot, Line, Wire, Arc2, Arc3, ArcLoop

__all__ = ['And', 'AndDS', 'AndIEC', 'Nand', 'NandDS', 'NandIEC', 'Or', 'OrDS', 'OrIEC', 'Nor', 'NorDS', 'NorIEC',
           'Xor', 'XorDS', 'XorIEC', 'Xnor', 'XnorDS', 'XnorIEC', 'Buf', 'Not', 'NotNot', 'Tristate', 'Tgate', 'Schmitt', 'SchmittNot',
           'SchmittAnd', 'SchmittNand', 'Kmap', 'Table', 'TimingDiagram', 'Arrow', 'Arrowhead', 'Dot', 'Line',
           'Wire', 'Arc2', 'Arc3', 'ArcLoop']

STYLE_IEEE = {'And': AndDS,
              'Or': OrDS,
              'Nand': NandDS,
              'Nor': NorDS,
              'Xor': XorDS,
              'Xnor': XnorDS}
STYLE_IEC = {'And': AndIEC,
              'Or': OrIEC,
              'Nand': NandIEC,
              'Nor': NorIEC,
              'Xor': XorIEC,
              'Xnor': XnorIEC}


def style(style):
    ''' Set global element style

        Args:
            style: dictionary of elementname: Element
            to change the element module namespace.
            Use `elements.STYLE_IEEE` or `elements.STYLE_IEC`
            to define U.S./IEEE or European/IEC element styles.
    '''
    for name, element in style.items():
        globals()[name] = element
