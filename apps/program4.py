from utils.app import *

def main():
    if Confirm.ask("[bold]Keluar Program?"):
        return program4.stop()

title = "[text_title]Program 1: Title Program\n" # untuk di tampilkan sebagai judul
name = "Nama Program" # untuk di tampilkan di list menu
description = """[text_default]
🔷 list 1. 
🔷 list 2. 
🔷 list 3.\n""" # deskripsi program

program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
