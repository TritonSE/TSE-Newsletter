import dominate
from dominate.tags import *

logo_img = 'https://drive.google.com/uc?export=view&id=1gq2ARk8HOCKw9MBrUfrEYe3GJjHGyBta'

def _foot():
    """Returns the generated HTML footer. TODO: edit this description

    TODO: A description here, according to Google's Python style guide https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

    Args:
        TODO

    Returns:
        TODO

    Raises:
        None
    """

    with div() as footer:
        with tr().add(td()).add(table()).add(tr()).add(td(cls='footer')):
            hr(cls='horiz')
            with table(cls='columnLeft').add(tr()).add(td(cls='padding')).add(table()).add(tr()).add(td()):
                img(cls='logoLeft', src=logo_img, alt='Logo Image')
            with table(cls='columnRight').add(tr()).add(td(cls='padding')).add(table()).add(tr()).add(td()):
                img(cls='logoRight', src=logo_img, alt='Logo Image')

    return footer