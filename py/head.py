import dominate
from dominate.tags import *

# Remove when finished testing
doc = dominate.document(title='Sample Table Description')

# Remove when finished testing
with doc.head:
    link(rel='stylesheet', href='newsletter.css')

def _head():
    """This function generates a header using tables and returns it as HTML. DO NOT EDIT!

    Args:
        None

    Returns:
        The generated HTML header

    Raises:
        None
    """
# Add to function when finished testing (indent)
with doc:
    with div(cls='ef-wrapper').add(div(cls='ef-webkit')).add(table(cls='ef-table ef-outer')):
        with tr().add(td(cls='ef-td')).add(table(cls='ef-table ef-header')).add(tr()).add(td(cls='ef-td ef-logo')).add(a(href='https://tse.ucsd.edu/', target='_blank')):
            with table(cls='ef-table ef-column ef-columnLogo').add(tr()).add(td(cls='ef-td ef-padding')).add(table(cls='ef-table ef-content')).add(tr()).add(td(cls='ef-td')):
                img(cls='ef-lightbulb', src='https://drive.google.com/uc?export=view&id=1gq2ARk8HOCKw9MBrUfrEYe3GJjHGyBta')
            with table(cls='ef-table ef-column ef-columnLogo').add(tr()).add(td(cls='ef-td ef-padding')).add(table(cls='ef-table ef-content')).add(tr()).add(th()):
                p('TRITON SOFTWARE ENGINEERING')

print(doc)
