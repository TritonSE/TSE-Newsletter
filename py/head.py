import dominate
from dominate.tags import *

def _head():
    """This function generates a header using tables and returns it as HTML. DO NOT EDIT!

    Args:
        None

    Returns:
        The generated HTML header

    Raises:
        None
    """
    with doc:
        # Outer layers
        with div(cls='ef-wrapper').add(div(cls='ef-webkit')).add(table(cls='ef-table ef-outer')):
            # Header
            # Logo
            with tr().add(td(cls='ef-td')).add(table(cls='ef-table ef-header')).add(tr()).add(td(cls='ef-td ef-logo')).add(a(href='https://tse.ucsd.edu/', target='_blank')):
                # Left lightbulb
                with table(cls='ef-table ef-column ef-columnLogo').add(tr()).add(td(cls='ef-td ef-padding')).add(table(cls='ef-table ef-content')).add(tr()).add(td(cls='ef-td')):
                    img(cls='ef-lightbulb', src='https://drive.google.com/uc?export=view&id=1gq2ARk8HOCKw9MBrUfrEYe3GJjHGyBta')
                # TSE
                with table(cls='ef-table ef-column ef-columnLogo').add(tr()).add(td(cls='ef-td ef-padding')).add(table(cls='ef-table ef-content')).add(tr()).add(th()):
                    h1('TRITON SOFTWARE ENGINEERING')
                # Right lightbulb
                with table(cls='ef-table ef-column ef-columnLogo').add(tr()).add(td(cls='ef-td ef-padding')).add(table(cls='ef-table ef-content')).add(tr()).add(td(cls='ef-td')):
                    img(cls='ef-lightbulb', src='https://drive.google.com/uc?export=view&id=1gq2ARk8HOCKw9MBrUfrEYe3GJjHGyBta')
            # Socials
            with tr().add(td(cls='ef-td')).add(table(cls='ef-table ef-socials')).add(tr()).add(td(cls='ef-td ef-social')):
                # Facebook
                with a(href='https://www.facebook.com/TritonSE/', target='_blank').add(table(cls='ef-table ef-column ef-columnLeft')).add(tr()).add(td(cls='ef-td')).add(table(cls='ef-table ef-content')).add(tr()):
                    with td(cls='ef-td'):
                        img(cls='ef-icon', src='https://drive.google.com/uc?export=view&id=12a0jjtP5y-3BoSyxWQFXPEfli5rC9RyI')
                    with td(cls='ef-td'):
                        p('@TritonSE')
                # Instagram
                with a(href='https://www.instagram.com/ucsd_tse/', target='_blank').add(table(cls='ef-table ef-column ef-columnLeft')).add(tr()).add(td(cls='ef-td')).add(table(cls='ef-table ef-content')).add(tr()):
                    with td(cls='ef-td'):
                        img(cls='ef-icon', src='https://drive.google.com/uc?export=view&id=1pzLNGWWHnNxMgPXKl8UQREI4TblB6o-Y')
                    with td(cls='ef-td'):
                        p('@ucsd_tse')
                # LinkedIn
                with a(href='https://www.linkedin.com/company/tritonsoftwareengineering/', target='_blank').add(table(cls='ef-table ef-column ef-columnRight')).add(tr()).add(td(cls='ef-td')).add(table(cls='ef-table ef-content')).add(tr()):
                    with td(cls='ef-td'):
                        img(cls='ef-icon', src='https://drive.google.com/uc?export=view&id=1vEoRqm-IqkHbhpHsSV5y0k6o_LlnG-hC')
                    with td(cls='ef-td'):
                        p('@Triton Software Engineering')

    print(doc)