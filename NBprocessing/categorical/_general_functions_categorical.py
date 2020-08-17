import re
from NBprocessing.src import constance_object

def color_imbalanced(raw_input):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    pattern = re.compile(r'(\d+)')
    val = int(pattern.search(raw_input)[0])
    color = constance_object.BLACK if val < 90 else constance_object.RED
    return constance_object.OUTPUT.format(color)
