import os
from PIL import Image
import re
import time


ROOT: str = os.path.dirname(__file__)
TIMESTAMP: time.struct_time = time.localtime()
FORMMATED_TIME: str = f'{TIMESTAMP[0]}-{TIMESTAMP[1]}-{TIMESTAMP[2]}_{TIMESTAMP[3]}-{TIMESTAMP[4]}-{TIMESTAMP[5]}'


def main() -> None:
    print(f'Simple Skybox Generator | Made by TheKliko')
    generate_skybox(
        color=get_color()
    )


def get_color() -> str:
    """Function that returns a string representing a color (hexadecimal format)"""
    while True:
        print()
        print('Choose a color')
        response = input('My color: #')
        if not is_hex_color(f'#{response}'):
            print()
            print('Error, invalid color!')
            print('Please make sure that you enter your color in hexadecimal format (#RGB or #RRGGBB)')
            continue
        return f'#{response}'


def is_hex_color(color: str) -> bool:
    """Function that returns True if the given input is a valid hexadecimal color, otherwise False"""
    pattern = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$')
    return bool(pattern.match(color))


def generate_skybox(color: str) -> None:
    """Function that generates a Roblox skybox using the PIL library"""

    FILENAMES: list[str] = ['sky512_bk','sky512_dn','sky512_ft','sky512_lf','sky512_rt','sky512_up']
    PATH: str = os.path.join(ROOT, f'{FORMMATED_TIME}_{color}', 'PlatformContent', 'pc', 'textures', 'sky')

    create_directories(color)

    image = Image.new(mode='RGB', size=(1024, 1024), color=color)
    for filename in FILENAMES:
        image.save(os.path.join(PATH, f'{filename}.png'))
        os.rename(os.path.join(PATH, f'{filename}.png'), os.path.join(PATH, f'{filename}.tex'))


def create_directories(color) -> None:
    PATH: str = os.path.join(ROOT, f'{FORMMATED_TIME}_{color}', 'PlatformContent', 'pc', 'textures', 'sky')
    os.makedirs(PATH)


if __name__ == '__main__':
    main()