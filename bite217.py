from contextlib import redirect_stdout
from io import StringIO
from types import BuiltinFunctionType


def get_len_help_text(builtin: BuiltinFunctionType) -> int:
    """Receives a builtin, and returns the length of its help text.
       You need to redirect stdout from the help builtin.
       If the the object passed in is not a builtin, raise a ValueError.
    """
    if type(builtin) != BuiltinFunctionType:
        raise ValueError
    out = StringIO()
    with redirect_stdout(out):
        help(builtin)
    a = out.getvalue()

    return len(a)


print(get_len_help_text(len))