import html
import dominate
from dominate.tags import *

def _greetings(week):
    """This function generates a greetings section below the header using table elements and returns it as HTML. 
    The greetings consists of two subheaders separated by a horizontal line. The first subheader prints the function argument,
    which will most likely be "HAPPY WEEK # EVERYONE" and the second subheader prints, "Here are some things to get excited about!".
    The horizontal line in the middle is a bordered yellow div.

    Args:
        week: A string containing the current week number.

    Returns:
        An HTML document object containing the newsletter's greetings. The greetings consists of two table elements within 
        a single table row. Each of the two rows contains the messages described above and the rows are separated by the horizontal
        line div.

    Raises:
        None
    """

    with div() as greeting:
        # Greeting
        with tr().add(td(cls='td')).add(table(cls='table')).add(tr()).add(td(cls='td greeting')):
            # First subheader
            with table(cls='table').add(tr()).add(td(cls='td')):
                # Changes according to argument week
                h2(week)
            # Horizontal line
            hr(cls='horiz')
            # Second subheader
            with table(cls='table').add(tr()).add(td(cls='td')):
                h3('Here are some things to get excited about!')

    return greeting