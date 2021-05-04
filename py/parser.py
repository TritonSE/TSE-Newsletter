from entry_objects import *
from newsletter import *
import enum

class CurrentSection(enum.Enum):
    title = 1
    details = 2
    description = 3
    image = 4

def parser():
    content = open("newsletter.txt", "r")
    file_lines = content.readlines()
    content.close()
    #removes new line characters and extra end spaces
    lines = process_lines(file_lines)
    sections = []
    section_count = -1
    #next expected section to parse is a title
    curr_section = CurrentSection.title
    for i in range(len(lines)):
        #determines number of leading spaces in the line
        line_spacing, line = spacing(lines[i])
        #if it was a new line update what we expect to parse next
        if line == "":
            curr_section = update_section(curr_section, section_count)
        #if the line had no leading spaces, it is the title of a new section
        elif line_spacing == 0:
            section_count += 1
            sections.append([line, []])
        #if 4 leading spaces, it is the title of an entry within the section or an image
        elif(line_spacing == 4):
            section_body = sections[section_count][1]
            if curr_section.value == 1:
                #if it's an image, update expected section to image and process it
                if is_image(line):
                    curr_section = update_section(curr_section, section_count, is_img=True)
                    section_body.append(process_image(line))
                #it is a entry title so a new entry with the title is added
                else:
                    section_body.append(Entry(line, [Content([])], []))
        #If 8 leading spaces, it is part of an entry's body
        elif line_spacing == 8:
            #If parsing through details section, add to the details
            if curr_section.value == 2:
                section_body[-1].details.append(process_detail(line))
            #If parsing through the body section, add to the description or add image
            elif curr_section.value == 3:
                if is_image(line):
                    #adds new image to the body
                    section_body[-1].body.append(process_image(line))
                    #adds a new content block to set up further lines of description that follow
                    section_body[-1].body.append(Content([]))
                else:
                    #adds description line to the content block
                    section_body[-1].body[-1].desc.append(process_desc_line(line))
    #generates the HTML file given all of the sections' content
    generate(sections)

def process_lines(lines):
    """Removes newline character and extra spacing from the end of the lines"""
    return [line.rstrip() for line in lines]

def spacing(line):
    """Removes spacing from the front of the line and returns 
    the new length and the number of spaces removed"""
    spaces = len(line) - len(line.lstrip())
    return spaces, line.lstrip()

def process_detail(line):
    """Processes a line of details and treats it as text or a Zoom/Discord Link"""
    colon_index = line.find(":")
    if line[colon_index - 4 : colon_index] == "Link":
        return Link(line[0:colon_index], line[colon_index + 2:])
    return Text(line)

def process_desc_line(line):
    """Processes a line of a description and treats it as text or a link"""
    if line[0:2] == "L:":
        hyphen_index = line.find("-")
        return Link(line[3: hyphen_index - 1], line[hyphen_index + 2:])
    return Text(line)
    
def update_section(curr_section, section_count, is_img = False):
    """Updates the enum of what section type we will be parsing through next"""
    if is_img:
        return CurrentSection.image
    #If an image or entry body has been parsed, parsing an entry title is next
    elif curr_section.value == 3 or curr_section.value == 4:
        return CurrentSection.title
    #If an entry title has been parsed and it is the left-line body, parsing details is next
    elif curr_section.value == 1 and section_count == 0:
        return CurrentSection.details
    #In other cases entry description is next to be parsed
    return CurrentSection.description

def is_image(line):
    """Returns whether or not the line represents an image"""
    return line[0:2] == "I:"

def process_image(line):
    """Returns an Image object made up of a line that represents an image"""
    return Image(line[3:], "failed to render")

parser()