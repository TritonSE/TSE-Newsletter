import dominate
from dominate.tags import *
from constants import *

def _foot():
    """This function generates a footer using table elements and returns it as HTML. The footer consists of a horizontal line
    with left- and right- aligned TSE lightbulb logos below.This section of the newsletter should not need to be changed
    since no new information needs to be added. DO NOT EDIT!

    Args:
        None

    Returns:
        An HTML document object containing the newsletter's footer. The footer consists of a horizontal rule with two tables
        side-by-side below it. Each table contains a left- or right-aligned TSE lightbulb logo.

    Raises:
        None
    """

    with div() as footer:
        with tr().add(td()).add(table()).add(tr()).add(td(cls='footer')):
            hr(cls='horiz')
            with table(cls='columnLeft').add(tr()).add(td(cls='padding')).add(table()).add(tr()).add(td()):
                img(cls='logoLeft', src=LOGO_IMG, alt='Logo Image')
            with table(cls='columnRight').add(tr()).add(td(cls='padding')).add(table()).add(tr()).add(td()):
                img(cls='logoRight', src=LOGO_IMG, alt='Logo Image')

    return footer