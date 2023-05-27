import sys

sys.path.append("apps")

from apps.utils.load import Load
from apps import program1, program2, program3, program4, program5, program6

title = "[text_title]Project SDA 3[/]"
description = """[text_default]
Project SDA 3 merupakan project mata kuliah Struktur Data dan Algoritma yang berisi program-program implementasi struktur data Senarai Berantai (Linked List).
"""

programs = Load(title=title, description=description)
programs.add([program1, program2, program3, program4, program5, program6])

if __name__ == "__main__":
    programs.start()
