import dominate
from dominate.tags import *
from entry_objects import *

def _bodylineright(title, entries):
    """Returns the HTML for a right-oriented body section with a vertical line on the right. The section has a 
    title, such as Recent Milestones, as well as images and entries for the section. Entries have their own title,
    an optional list of details, and a description that consists of text and links.
    Args:
        title (string) - The title of the newsletter section. Ex: "RECENT MILESTONES"
        entries (list of Entry objects) - A list of entries under the newsletter section. Ex: [Entry("TESC Funding", [Content([Text("We are now funded by TESC!")])])]
    Returns:
        An HTML document object that contains HTML for a right-oriented newsletter section with a vertical line on the right.
        The HTML consists of tables to orient each entry within the section.
    Raises:
        TypeError -
            1. If the title is not a string.
            2. If the elements of entries are not Entry or Image objects.
            3. If the elements of an entry's details are not Text, Link or Linebreak objects.
            4. If the elements of an entry's body are not Content or Image objects.
            5. If the elements of Content are not Text, Link or Linebreak objects.
    """
    with table(cls="height") as bodylineright:
        with tr().add(td(cls="td-valign right section-title-right")).add(div(cls="title-div")):
            # Makes section title and horizontal line.
            if isinstance(title, str):
                h1(title, cls="section-title")
                hr(cls="horiz")
            else:
                raise TypeError("Title must be a string.")
        with tr().add(td(cls="td-valign")).add(table(cls="height")).add(tr()):
            # Makes table for entries.
            with td(cls="td-valign right-pad").add(table()):
                for i in range(len(entries)):
                    entry = entries[i]
                    # Adjusts padding for the first entry of the section.
                    entry_class = "td-valign entry"
                    if i == 0:
                        entry_class = "td_valign first-entry"
                    if isinstance(entry, Entry):
                        # Creates table for the entry.
                        with tr().add(td(cls=entry_class)).add(table()):
                            tr().add(td(cls="td-valign")).add(h2(entry.title, cls="title right"))
                            # Adds details section if the entry has one.
                            if entry.details != []:
                                with tr().add(td(cls="td-valign detail-pad")):
                                    # Iterates through the details array and generates HTML depending on object type.
                                    for line in entry.details:
                                        if isinstance(line, Link):
                                            with p(cls="details").add(u()):
                                                a(line.text, cls="details_link", href=line.url, target="_blank")
                                        elif isinstance(line, Linebreak):
                                            for i in range(line.numBreaks):
                                                br()
                                        elif isinstance(line, Text):
                                            p(line.text, cls="details")
                                        else:
                                            raise TypeError("Elements of details must be either a Text, Linebreak or Link object.")
                            # Iterates through the body of the entry to create HTML for rendering a block of content or an image.
                            for elem in entry.body:
                                if isinstance(elem, Content):
                                    with tr().add(td(cls="td-valign right-desc-pad")):
                                        for line in elem.desc:
                                            if isinstance(line, Link):
                                                with p(cls="description right").add(u()):
                                                    a(line.text, cls="desc_link", href=line.url, target="_blank")
                                            elif isinstance(line, Linebreak):
                                                for i in range(line.numBreaks):
                                                    br()
                                            elif isinstance(line, Text):
                                                p(line.text, cls="description right")
                                            elif isinstance(line, UnorderedList):
                                                raise TypeError("UnorderedList can only be used for left-aligned entries")
                                            else:
                                                raise TypeError("Elements of Content object must be either a Text, Link or Linebreak object.")
                                elif isinstance(elem, Image):
                                    with tr().add(td(cls="td-valign entry")):
                                        img(cls="img-right", src=elem.url, alt=elem.alt)
                                else:
                                    raise TypeError("Elements of body must be either Content or Image objects")
                    # If the entry is an Image, then the image is rendered or the alt is displayed.
                    elif isinstance(entry, Image):
                        with tr().add(td(cls=entry_class)):
                            if entry.is_logo:
                                img(cls="img-right img-logo", src=entry.url, alt=entry.alt)
                            else:
                                img(cls="img-right", src=entry.url, alt=entry.alt)
                    else:
                        raise TypeError("Elements of entries must either be Entry or Image object.")
            # Creates vertical line
            td(cls="td-valign vertical-right")
            td(cls="td-valign right-line-pad")   
    return bodylineright