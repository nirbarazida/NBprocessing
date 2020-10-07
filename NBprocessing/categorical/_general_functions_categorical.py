import re
from NBprocessing.src import constance_object

def color_imbalanced(raw_input):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """

    color = constance_object.BLACK
    if raw_input != "0.00":
        pattern = re.compile(r'(: )(\d+)')
        val = int(pattern.search(raw_input)[2])
        if val >= 90:
            color =  constance_object.RED
    return constance_object.OUTPUT.format(color)



