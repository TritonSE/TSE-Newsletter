import dominate
from dominate.tags import *

def _bodynoline(title, entries):
    """Returns the HTML for a centered body section with no vertical lines. The section has a 
    title, such as Alumni Advice or Member Spotlight, as well as a body section that contains
    text along with images.

    Args:
        title (string) - The title of the newsletter section.
        entries (list of Entry objects) - A list of entries under the newsletter section.

    Returns:
        An HTML document object that contains HTML for a centered newsletter section with no vertical line.
        The HTML consists of tables to orient each entry within the section.

    Raises:
        None
    """
    return p('This is the body with a no line.')
