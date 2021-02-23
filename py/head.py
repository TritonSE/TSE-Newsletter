import dominate
from dominate.tags import *

banner_img = 'https://drive.google.com/uc?export=view&id=1czSvLEq4b05e2ngXvCwL5OUUz-G92X_J'
fb_img = 'https://drive.google.com/uc?export=view&id=12a0jjtP5y-3BoSyxWQFXPEfli5rC9RyI'
ig_img = 'https://drive.google.com/uc?export=view&id=1pzLNGWWHnNxMgPXKl8UQREI4TblB6o-Y'
in_img = 'https://drive.google.com/uc?export=view&id=1vEoRqm-IqkHbhpHsSV5y0k6o_LlnG-hC'

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
        with tr().add(td()).add(table(cls='header')).add(tr()).add(td(cls='logo')).add(a(href='https://tse.ucsd.edu/', target='_blank')):
            # TSE Banner
            with table().add(tr()).add(td(cls='padding')).add(table()).add(tr()).add(td(cls='center')):
                img(cls='banner', src=banner_img)
        # Socials
        with tr().add(td()).add(table(cls='socials')).add(tr()).add(td(cls='social')):
            # Facebook
            with a(href='https://www.facebook.com/TritonSE/', target='_blank').add(table(cls='column columnLeft')).add(tr()).add(td()).add(table()).add(tr()):
                with td():
                    img(cls='icon', src=fb_img)
                with td():
                    p('@TritonSE')
            # Instagram
            with a(href='https://www.instagram.com/ucsd_tse/', target='_blank').add(table(cls='column columnLeft')).add(tr()).add(td()).add(table()).add(tr()):
                with td():
                    img(cls='icon', src=ig_img)
                with td():
                    p('@ucsd_tse')
            # LinkedIn
            with a(href='https://www.linkedin.com/company/tritonsoftwareengineering/', target='_blank').add(table(cls='column columnRight')).add(tr()).add(td()).add(table()).add(tr()):
                with td():
                    img(cls='icon', src=in_img)
                with td():
                    p('Triton Software Engineering')

    return header