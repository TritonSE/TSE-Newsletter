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
    # enclose all of the elements within div/table elements
    with div(cls='wrapper').add(div(cls='container')).add(table(cls='outer height')):
        with tr().add(td()):
            _head()
        with tr().add(td()):
            _greetings(greet_title)
        # with tr().add(td()):
        #     _bodylineleft()
        # with tr().add(td()):
        #     _bodylineright()
        # with tr().add(td()):
        #     _bodynoline()
        with tr().add(td()):
            _foot()
    # google analytics that tracks email opens
    img(src='https://www.google-analytics.com/collect?v=1&tid=UA-192012371-2&cid=CLIENT_ID_NUMBER&t=event&ec=email&ea=open&el=recipient_id&cs=newsletter&cm=email&cn=TSE_NEWSLETTER&dp=%2Femail%2Fnewsletter&dt=TSE%20Newsletter')

# write out final output to newsletter.html
with open('newsletter.html', 'w') as out_file:
    out_file.write(doc.render())