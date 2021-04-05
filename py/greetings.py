import dominate
from dominate.tags import *

def _greetings(greet_title, greet_sub = 'Here are some things to get excited about!'):
    """This function generates a greetings section below the header using table elements and returns it as HTML. 
    The greetings consists of a title and subtitle separated by a horizontal line. The title is the first function argument,
    which will be printed as a heading 2. The subtitle is the second function argument, which will be printed as a heading 3.
    The subtitle has a default value of 'Here are some things to get excited about!'. The horizontal line in the middle is a bordered
    yellow horizontal rule.

    Args:
        greet_title: A string containing the greetings title. (Ex. 'HAPPY WEEK 7 EVERYONE')
        greet_sub: A string containing the greetings subtitle with default value 'Here are some things to get excited about!'.

    Returns:
        An HTML document object containing the newsletter's greetings. The greetings consists of two table elements within 
        a single table row. Each of the two rows contains the messages described above and the rows are separated by the horizontal
        line div.

    Raises:
        None
    """

    with div() as greeting:
        # Greeting
        with tr().add(td(cls='greeting')):
            # Title
            with table().add(tr()).add(td(cls='center')):
                # Changes according to argument week
                h2(greet_title)
            # Horizontal rule
            hr(cls='horiz')
            # Subtitle
            with table().add(tr()).add(td(cls='center')):
                h3(greet_sub)

    return greeting