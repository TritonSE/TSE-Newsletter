import html
import dominate
from dominate.tags import *

def _greetings():
    """This function generates a greetings section below the header using table elements and returns it as HTML. 
    The greetings consists of two subheaders separated by a horizontal line. The first subheader prints, "HAPPY WEEK # EVERYONE"
    and the second subheader prints, "Here are some things to get excited about!". The horizontal line in the middle is a bordered
    yellow div. The only part of this section that should be edited is the week number (indicated with a comment in the code below).

    Args:
        None

    Returns:
        An HTML document object containing the newsletter's greetings. The greetings consists of two table elements within 
        a single table row. Each of the two rows contains the messages described above and the rows are separated by the horizontal
        line div.

    Raises:
        None
    """

    with div() as greeting:
        # Greeting
        with tr().add(td(cls='ef-td')).add(table(cls='ef-table')).add(tr()).add(td(cls='ef-td ef-greeting')):
            # First subheader
            with table(cls='ef-table ef-center').add(tr()).add(td(cls='ef-td')):
                # Edit # according to week
                h2('HAPPY WEEK 7 EVERYONE!')
            # Horizontal line
            hr(cls='sk-horizontal')
            # Second subheader
            with table(cls='ef-table ef-center').add(tr()).add(td(cls='ef-td')):
                h3('Here are some things to get excited about!')

    return greeting