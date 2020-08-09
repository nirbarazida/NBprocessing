import re


def color_imbalanced(raw_input):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    pattern = re.compile(r'(\d+)')
    val = int(pattern.search(raw_input)[0])
    color = 'black' if 5 < val < 90 else 'red'
    return f'color: {color}'
