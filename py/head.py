import dominate
from dominate.tags import *

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
        with tr().add(td(cls='td')).add(table(cls='table header')).add(tr()).add(td(cls='td logo')).add(a(href='https://tse.ucsd.edu/', target='_blank')):
            # Left lightbulb
            with table(cls='table column columnLogo').add(tr()).add(td(cls='td padding')).add(table(cls='table')).add(tr()).add(td(cls='td')):
                img(cls='lightbulb', src='https://drive.google.com/uc?export=view&id=1gq2ARk8HOCKw9MBrUfrEYe3GJjHGyBta')
            # TSE
            with table(cls='table column columnTitle').add(tr()).add(td(cls='td padding')).add(table(cls='table')).add(tr()).add(th()):
                h1('TRITON SOFTWARE ENGINEERING')
            # Right lightbulb
            with table(cls='table column columnLogo').add(tr()).add(td(cls='td padding')).add(table(cls='table')).add(tr()).add(td(cls='td')):
                img(cls='lightbulb', src='https://drive.google.com/uc?export=view&id=1gq2ARk8HOCKw9MBrUfrEYe3GJjHGyBta')
        # Socials
        with tr().add(td(cls='td')).add(table(cls='table socials')).add(tr()).add(td(cls='td social')):
            # Facebook
            with a(href='https://www.facebook.com/TritonSE/', target='_blank').add(table(cls='table column columnLeft')).add(tr()).add(td(cls='td')).add(table(cls='table')).add(tr()):
                with td(cls='td'):
                    img(cls='icon', src='https://drive.google.com/uc?export=view&id=12a0jjtP5y-3BoSyxWQFXPEfli5rC9RyI')
                with td(cls='td'):
                    p('@TritonSE')
            # Instagram
            with a(href='https://www.instagram.com/ucsd_tse/', target='_blank').add(table(cls='table column columnLeft')).add(tr()).add(td(cls='td')).add(table(cls='table')).add(tr()):
                with td(cls='td'):
                    img(cls='icon', src='https://drive.google.com/uc?export=view&id=1pzLNGWWHnNxMgPXKl8UQREI4TblB6o-Y')
                with td(cls='td'):
                    p('@ucsd_tse')
            # LinkedIn
            with a(href='https://www.linkedin.com/company/tritonsoftwareengineering/', target='_blank').add(table(cls='table column columnRight')).add(tr()).add(td(cls='td')).add(table(cls='table')).add(tr()):
                with td(cls='td'):
                    img(cls='icon', src='https://drive.google.com/uc?export=view&id=1vEoRqm-IqkHbhpHsSV5y0k6o_LlnG-hC')
                with td(cls='td'):
                    p('Triton Software Engineering')

    return header