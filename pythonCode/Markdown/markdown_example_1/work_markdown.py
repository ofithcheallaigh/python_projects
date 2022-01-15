from mdutils.mdutils import MdUtils
from mdutils import Html
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
title = 'Work ' + today
# print(title)

# file_name is the name we will see in a folder
# title is the title of the doc, inside the file
mdFile = MdUtils(file_name=title, title='Work Notes')



# Needed to actually generate the markdown file
mdFile.create_md_file()
