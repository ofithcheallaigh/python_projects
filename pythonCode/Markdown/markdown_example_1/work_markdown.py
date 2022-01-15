from mdutils.mdutils import MdUtils
from mdutils import Html
from datetime import datetime
import calendar

week_day = datetime.today().strftime('%A')
today = datetime.today().strftime('%Y-%m-%d')
title = 'Work ' + today



# file_name is the name we will see in a folder
# title is the title of the doc, inside the file
mdFile = MdUtils(file_name=title, title='Work Notes '+week_day+' '+today)
mdFile.new_paragraph("Current project: BLE")

mdFile.new_header(level=1,title="Boot Time")
mdFile.new_paragraph("Boot up time today was: ")

# Add in a to do list
mdFile.new_header(level=1,title="To Do List")
mdFile.new_paragraph("[ ]")


mdFile.new_table_of_contents(table_title='Contents', depth=2)
# Needed to actually generate the markdown file
mdFile.create_md_file()
