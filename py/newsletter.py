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

# create a document titled 'TSE Newsletter'
doc = dominate.document(title='TSE Newsletter')

# import the newsletter css in the head
with doc.head:
    link(rel='stylesheet', href='newsletter.css')

# create the document body
with doc:
    # enclose all of the elements within a table cell.
    with table().add(tbody()).add(tr()).add(td()):
        _head()
        _greetings()
        _bodylineleft()
        _bodylineright()
        _bodynoline()
        _foot()

# write out final output to newsletter.html
with open('newsletter.html', 'w') as out_file:
    out_file.write(doc.render())
