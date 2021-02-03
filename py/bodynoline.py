import dominate
from dominate.tags import *
from entry_objects import *

def _bodynoline(title, entries):
    """Returns the HTML for a centered body section with no vertical lines. The section has a 
    title, such as Alumni Advice or Member Spotlight, as well as a body section that contains
    text along with images.

    Args:
        title (string) - The title of the newsletter section. Ex: "Alumni Advice"
        entries (list of Entry objects) - A list of entries under the newsletter section. Ex: [Entry("Aaron Yang", [Text("Don't be afraid to be ambitious.")])]

    Returns:
        An HTML document object that contains HTML for a centered newsletter section with no vertical line.
        The HTML consists of tables to orient each entry within the section.

    Raises:
        TypeError - If the object type of elements within the entry aren't acceptable types.
    """
    with table() as bodynoline:
        with tr().add(td(cls="td-valign center")).add(div(cls="title-div")):
            h1(title, cls="section-title center")
            hr(cls="horiz")
        for i in range(len(entries)):
            entry = entries[i]
            #Adjusts padding for the first entry of the section.
            entry_class = "td-valign"
            if(i == 0):
                entry_class += " first-entry"
            else:
                entry_class += " entry"
            #Creates table for the entry.
            with tr().add(td(cls=entry_class)).add(table()):
                #Generates the title for the entry.
                with tr().add(td(cls="td-valign")):
                    h2(entry.title, cls="title center")
                #Iterates through the body to generate HTML depending on if text or an image
                #needs to be displayed.
                for elem in entry.body:
                    if isinstance(elem, Content):
                        with tr().add(td(cls="td-valign center-desc-pad")):
                            #For every element in the description, HTML is dependent on if it represents
                            #plain text, linebreaks, or a link.
                            for line in elem.desc:
                                if isinstance(line, Text):
                                    p(line.text, cls="description center")
                                elif isinstance(line, Linebreaks):
                                    for i in range(line.numBreaks):
                                        br()
                                elif isinstance(line, Link):
                                    with p(cls="description center").add(u()):
                                        a(line.text, cls="link", href=line.url, target="_blank")
                                else:
                                    raise TypeError("Elements of Content object must be Text, Link, or Linebreak objects")
                    #If the element is an Image, renders the image or displays the alt
                    elif isinstance(elem, Image):
                        with tr().add(td(cls="td-valign entry")):
                            img(src=elem.url, cls="img-center", alt=elem.alt)
                    else:
                        raise TypeError("Elements of body must be either Content or Image objects")
    return bodynoline
