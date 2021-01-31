# import dominate
import dominate
from dominate.tags import *

# local imports
from head import _head
from greetings import _greetings
from bodylineleft import _bodylineleft
from bodylineright import _bodylineright
from bodynoline import _bodynoline
from foot import _foot
from entry_objects import *

# USER VARIABLES
# greetings
greet_title = 'HAPPY WEEK 7 EVERYONE'

# create a document titled 'TSE Newsletter'
doc = dominate.document(title='TSE Newsletter')

# import the newsletter css in the head
with doc.head:
    link(rel='stylesheet', href='newsletter.css')

# create the document body
with doc:
    # enclose all of the elements within div elements (currently set to ef-styling)
    with div(cls='sk-wrapper').add(div(cls='sk-webkit')).add(table(cls='sk-table sk-outer sk-height')):
        with tr().add(td(cls="sk-td")):
            _head()
        with tr().add(td(cls="sk-td")):
            _greetings()
        with tr().add(td(cls="sk-td")):
            _bodylineleft()
        with tr().add(td(cls="sk-td")):
            _bodylineright()
        with tr().add(td(cls="sk-td")):
            _bodynoline()
        with tr().add(td(cls="sk-td")):
            _foot()

# write out final output to newsletter.html
with open('newsletter.html', 'w') as out_file:
    out_file.write(doc.render())