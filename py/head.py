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
    with div(style='text-align: center;', cls='ef-wrapper'):
        h1("TEST")

print(doc)
