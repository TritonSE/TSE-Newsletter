import dominate
from dominate.tags import *

def _bodynoline(title, entries):
    """Returns a body section with no vertical lines. TODO: edit this description

    TODO: A description here, according to Google's Python style guide https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

    Args:
        TODO

    Returns:
        TODO

    Raises:
        TODO
    """
    with table(cls="sk-table"):
        with tr().add(td(cls="sk-td sk-center")).add(div(cls="sk-title-div")):
            h1(title, cls="sk-section-title sk-center")
            hr(cls="sk-horiz")
        for i in range(len(entries)):
            entry = entries[i]
            if(i == 0):
                entry_class = "sk-td sk-first-entry"
            else:
                entry_class = "sk-td"
            with tr().add(td(cls=entry_class)).add(table(cls="sk-table")):
                with tr().add(td(cls="sk-td")):
                    h2(entry.title, cls="sk-title sk-center")
                with tr().add(td(cls="sk-td sk-center-desc-pad")):
                    for text in entry.body:
                        p(text, cls="sk-description sk-center")
    return p('This is the body with a no line.')
