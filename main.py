import sys
sys.path.append("apps")

from apps.utils.load import Load
from apps import program1, program2, program3, program4, program5, program6

title = "[text_title]Nama Project[/]"
description = """[text_default]
Deskripsi Project.
"""

programs = Load(title=title, description=description)
programs.add([program1, program2, program3, program4, program5, program6])

if __name__ == "__main__":
    programs.start()
