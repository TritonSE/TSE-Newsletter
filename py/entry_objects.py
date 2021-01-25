class UpcomingEvent:
    """
    Represents one entry of an upcoming event
    Attributes:
    1. title (string) - The title of the event
    2. details (array of link or text objects) - Each element in the array represents a new line
    3. body (array of line or text objects) - Each element in the array represents a new line
    """
    def __init__(self, title, details, body):
        self.title = title
        self.details = details
        self.body = body
    
class Entry:
    """
    Represents one entry of all other sections other than upcoming events
    Attributes:
    1. title (string) - The title of the entry
    2. body (array of line, text or image objects) - Each element in the array represents a new line
    """
    def __init__(self, title, body):
        self.title = title
        self.body = body

class Milestones(Entry):
    """
    Inherits from Entry class and represents one milestone entry.
    """
    def __init__(self, title, body):
        super().__init__(title, body)

class ExecUpdates(Entry):
    """
    Inherits from Entry class and represents one milestone entry.
    """
    def __init__(self, title, body):
        super().__init__(title, body)

class AlumniAdvice(Entry):
    """
    Inherits from Entry class and represents one milestone entry.
    """
    def __init__(self, title, body):
        super().__init__(title, body)
        
class Text:
    """
    Represents a portion of text of an entry's body.
    Attributes:
    1. text (string) - The actual text that needs to be displayed
    2. linebreaks (integer) - The number of empty lines that needs to follow the text
    """
    def __init__(self, text, linebreaks):
        self.text = text
        self.linebreaks = linebreaks

class Link(Text):
    """
    Inherits from the Text class.
    Represents a portion of text of an entry's body that is linked to a url.
    Attributes:
    1. url (string) - The url that the text is being mapped to.
    """
    def __init__(self, text, url, linebreaks):
        super().__init__(text, linebreaks)
        self.url = url

class Image:
    """
    Represents an image
    Attributes:
    1. url (string) - The url of the image to be displayed.
    """
    def __init__(self, url):
        self.url = url