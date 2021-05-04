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
            # Socials + Lightbulbs
            with tr().add(td(cls='padding social')):
                p('Follow us on our social media!')
                # Lightbulb
                with table(cls='column smColumn').add(tr()).add(td()).add(table()).add(tr()).add(td()):
                    img(cls='lightbulb', src=LOGO_IMG, alt='Logo Image')
                # Facebook
                with a(href=TSE_FB, target='_blank').add(table(cls='column mdColumn')).add(tr()).add(td()).add(table()).add(tr()):
                    with td():
                        img(cls='icon', src=FB_IMG, alt='Facebook Logo')
                    with td():
                        p('@TritonSE')
                # Instagram
                with a(href=TSE_IG, target='_blank').add(table(cls='column mdColumn')).add(tr()).add(td()).add(table()).add(tr()):
                    with td():
                        img(cls='icon', src=IG_IMG, alt='Instagram Logo')
                    with td():
                        p('@ucsd_tse')
                # LinkedIn
                with a(href=TSE_IN, target='_blank').add(table(cls='column lgColumn')).add(tr()).add(td()).add(table()).add(tr()):
                    with td():
                        img(cls='icon', src=IN_IMG, alt='LinkedIn Logo')
                    with td():
                        p('Triton Software Engineering')
                # Lightbulb
                with table(cls='column smColumn').add(tr()).add(td()).add(table()).add(tr()).add(td()):
                    img(cls='lightbulb right', src=LOGO_IMG, alt='Logo Image')

    return footer