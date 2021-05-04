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
        with tr().add(td(cls='footer')):
            hr(cls='horiz')

        # Socials
        with tr().add(td()).add(table(cls='socials')).add(tr()).add(td(cls='social')):
            p('Follow us on our social media!')
            # Facebook
            with a(href=TSE_FB, target='_blank').add(table(cls='column columnLeft')).add(tr()).add(td()).add(table()).add(tr()):
                with td():
                    img(cls='icon', src=FB_IMG, alt='Facebook Logo')
                with td():
                    p('@TritonSE')
            # Instagram
            with a(href=TSE_IG, target='_blank').add(table(cls='column columnLeft')).add(tr()).add(td()).add(table()).add(tr()):
                with td():
                    img(cls='icon', src=IG_IMG, alt='Instagram Logo')
                with td():
                    p('@ucsd_tse')
            # LinkedIn
            with a(href=TSE_IN, target='_blank').add(table(cls='column columnRight')).add(tr()).add(td()).add(table()).add(tr()):
                with td():
                    img(cls='icon', src=IN_IMG, alt='LinkedIn Logo')
                with td():
                    p('Triton Software Engineering')

        # Lightbulbs
        with tr().add(td(cls='footer')):
            with table(cls='columnLeft').add(tr()).add(td(cls='padding')).add(table()).add(tr()).add(td()):
                img(cls='logoLeft', src=LOGO_IMG, alt='Logo Image')
            with table(cls='columnRight').add(tr()).add(td(cls='padding')).add(table()).add(tr()).add(td()):
                img(cls='logoRight', src=LOGO_IMG, alt='Logo Image')

    return footer