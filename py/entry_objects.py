class Entry:
    """
    Each section on the newsletter, such as upcoming events and milestones, can have multiple entries.
    This class is used to represent a single entry which consists of a title and a description.
    Attributes:
    1. title (string) - The title of the entry
    2. body (list of line, text or image objects) - Each element in the list represents a new line
    """
    def __init__(self, title, body):
        self.title = title
        self.body = body

class UpcomingEvent(Entry):
    """
    Inherits from Entry class and represents one upcoming event entry.
    An upcoming event entry includes the title of the event, details regarding logistics,
    and a description of the event.
    Attributes:
    1. details (list of link or text objects) - Each element in the list represents a new detail regarding the event.
    """
    def __init__(self, title, details, body):
        super().__init__(title, body)
        self.details = details
    
class Milestones(Entry):
    """
    Inherits from Entry class and represents one milestone entry.
    A milestone entry includes the title of the milestone as well as a description regarding 
    the milestone.
    """
    def __init__(self, title, body):
        super().__init__(title, body)

class ExecUpdates(Entry):
    """
    Inherits from Entry class and represents one executive board updates entry.
    An executive board updates entry includes the title of an update given from the 
    executive board as well a description for the update.
    """
    def __init__(self, title, body):
        super().__init__(title, body)

class AlumniAdvice(Entry):
    """
    Inherits from Entry class and represents an alumni advice entry.
    An alumni advice entry includes the name of the alumni as the title and their
    quote and image as the body.
    """
    def __init__(self, title, body):
        super().__init__(title, body)
        
class Text:
    """
    Represents a portion of text of an entry's body.
    Attributes:
    1. text (string) - The actual text that needs to be displayed.
    """
    def __init__(self, text):
        self.text = text

class Link(Text):
    """
    Inherits from the Text class.
    Represents a portion of text of an entry's body that is linked to a url.
    Attributes:
    1. url (string) - The url that the text is being mapped to.
    """
    def __init__(self, text, url):
        super().__init__(text)
        self.url = url

class Image:
    """
    Represents an image to be displayed.
    Attributes:
    1. url (string) - The url of the image to be displayed.
    2. alt (string) - Alternative text to be displayed if the image is not rendered.
    """
    def __init__(self, url, alt):
        self.url = url
        self.alt = alt

class Linebreaks:
    """
    Represents linebreaks within the body of an entry.
    Placed between Text or Image objects within a list for an entry's body to create 
    whitelines between bodies of text and images.
    Attributes:
    1. numBreaks - The number of extra lines to be added.
    """
    def __init__(self, numBreaks):
        self.numBreaks = numBreaks