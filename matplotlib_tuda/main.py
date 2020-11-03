import matplotlib.colors
from cycler import cycler

TUDA_COLOR_NAMES = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
TUDA_COLORS = {
    '0': {'a': '#DCDCDC', 'b': '#B5B5B5', 'c': '#898989', 'd': '#535353'},
    '1': {'a': '#5D85C3', 'b': '#005AA9', 'c': '#004E8A', 'd': '#243572'},
    '2': {'a': '#009CDA', 'b': '#0083CC', 'c': '#00689D', 'd': '#004E73'},
    '3': {'a': '#50B695', 'b': '#009D81', 'c': '#008877', 'd': '#00715E'},
    '4': {'a': '#AFCC50', 'b': '#99C000', 'c': '#7FAB16', 'd': '#6A8B22'},
    '5': {'a': '#DDDF48', 'b': '#C9D400', 'c': '#B1BD00', 'd': '#99A604'},
    '6': {'a': '#FFE05C', 'b': '#FDCA00', 'c': '#D7AC00', 'd': '#AE8E00'},
    '7': {'a': '#F8BA3C', 'b': '#F5A300', 'c': '#D28700', 'd': '#BE6F00'},
    '8': {'a': '#EE7A34', 'b': '#EC6500', 'c': '#CC4C03', 'd': '#A94913'},
    '9': {'a': '#E9503E', 'b': '#E6001A', 'c': '#B90F22', 'd': '#961C26'},
    '10': {'a': '#C9308E', 'b': '#A60084', 'c': '#951169', 'd': '#732054'},
    '11': {'a': '#804597', 'b': '#721085', 'c': '#611C73', 'd': '#4C226A'}
}


def tuda_color(code: str):
    code = code.lower()
    if code == 'blue':
        return tuda_color('1b')
    elif code == 'orange':
        return tuda_color('7b')
    elif code == 'green':
        return tuda_color('3b')
    elif code == 'red':
        return tuda_color('9b')
    elif code == 'purple':
        return tuda_color('11b')
    elif code == 'brown':
        return tuda_color('8d')
    elif code == 'pink':
        return tuda_color('10a')
    elif code == 'gray':
        return tuda_color('0c')
    elif code == 'olive':
        return tuda_color('4b')
    elif code == 'cyan':
        return tuda_color('2a')
    else:
        hue_code = code[:-1]
        brightness_code = code[-1]
        if hue_code not in TUDA_COLORS:
            raise Exception('Unknown TUDa hue code %s!' % hue_code)
        if brightness_code not in TUDA_COLORS[hue_code]:
            raise Exception('Unknown TUDa brightness code %s for hue code %s!' % (brightness_code, hue_code))
        return TUDA_COLORS[hue_code][brightness_code]


def load():
    colors_map = matplotlib.colors.get_named_colors_mapping()
    tuda_color_codes = list([f'tuda:{color_name}' for color_name in TUDA_COLOR_NAMES])
    for color_code, color_name in zip(tuda_color_codes, TUDA_COLOR_NAMES):
        color = tuda_color(color_name)
        colors_map[color_name] = color
        colors_map[color_code] = color

    matplotlib.rcParams['axes.prop_cycle'] = cycler(color=tuda_color_codes)
