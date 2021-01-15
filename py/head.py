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
        h1("This is a sample table that has one row, two columns.")
        h2("The first column has styling for a vertical yellow line.")
        h2("The second column has another table inside of it with two rows.")
        with table().add(tbody()).add(tr()):
            td(div(style='border-left: 3px solid #FFD807; height: 100%', cls='myClass'))
            with td():
                with table().add(tbody()):
                    tr("this is the first row of my inner table")
                    tr("this is the second row of my inner table")

    print(doc)
