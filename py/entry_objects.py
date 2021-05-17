class Entry:
    """
    Each section on the newsletter, such as upcoming events and milestones, can have multiple entries.
    This class is used to represent a single entry which consists of a title, a description, and details regarding logistics.
    Attributes:
    1. title (string) - The title of the entry.
    2. body (list of Content and Image objects) - Each element in the list is displayed on a new line.
    3. details (list of Content objects) - Each element in the list represents a new detail regarding the event.
    """
    def __init__(self, title, body, details=[]):
        self.title = title
        self.body = body
        self.details = details

class Content:
    """
    Represents a block of text within an entry's body and details.
    Attributes:
    1. desc (list of Text, Link, UnorderedList, and Linebreaks objects) - Each element in the list represents one aspect of the details/body.
    """
    def __init__(self, desc):
        self.desc = desc 

class Image:
    """
    Represents an image to be displayed.
    Attributes:
    1. url (string) - The url of the image to be displayed.
    2. alt (string) - Alternative text to be displayed if the image is not rendered.
    3. is_logo (string) - Whether or not the image is a logo
    """
    def __init__(self, url, alt, is_logo=False):
        self.url = url
        self.alt = alt
        self.is_logo = is_logo
        
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

class Linebreak:
    """
    Represents linebreaks within the body of an entry.
    Placed between Text and Image objects within a list for an entry's body to create 
    whitelines between bodies of text and images.
    Attributes:
    1. numBreaks - The number of extra lines to be added.
    """
    def __init__(self, numBreaks):
        self.numBreaks = numBreaks

class UnorderedList:
    """
    Represents an unordered list within the body of an entry.
    Only applicable to left-oriented entries.
    Attributes:
    1. listLines - A list of the lines in the unordered list.
    """
    def __init__(self, list_lines = []):
        self.list_lines = list_lines