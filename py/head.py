import dominate
from dominate.tags import *
from constants import *

def _head():
    """This function generates a header using table elements and returns it as HTML. The header consists of the banner logo
    (lightbulbs and title) and the social media handles with their icons. The banner links to the main TSE website and each
    social media handle links to their respective accounts. This section of the newsletter should not need to be changed
    since no new information needs to be added. DO NOT EDIT!

    Args:
        None

    Returns:
        An HTML document object containing the newsletter's header. The header consists of table elements split into two rows. 
        The top row contains the banner and the bottom row contains the social media handles. Within each row are more tables 
        and columns containing the contents with anchor tags, namely the lightbulbs, title, social media icons, and social media handles.

    Raises:
        None
    """
    with div() as header:
        # Logo
        with tr().add(td()).add(table(cls='header')).add(tr()).add(td(cls='logo')).add(a(href=TSE_SITE, target='_blank')):
            # TSE Banner
            with table().add(tr()).add(td(cls='padding')).add(table()).add(tr()).add(td(cls='center')):
                img(cls='banner', src=BANNER_IMG, alt='TSE Banner')

    return header