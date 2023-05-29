from utils.app import *
from data_structure.linked_list import SLinkedList


def reverse_string(value: str):
    linked_list_str = SLinkedList()
    for char in value:
        linked_list_str.append(char)

    reversed_str = []
    while not linked_list_str.empty():
        reversed_str.append(linked_list_str.pop())

    return "".join(reversed_str)


def main():
    menu = {1: "1 paragraf", 2: "Lebih dari 1 paragraf", 3: "Keluar program"}

    menu_str = "\n[text_default]"
    for k, v in menu.items():
        menu_str += f"{k}. {v}\n"

    panel_description = Panel(
        program1.description,
        title="[text_title]Deskripsi Program",
        title_align="left",
        style="default",
    )
    panel_menu = Panel(
        menu_str,
        title="[text_title]Opsi Masukan String",
        title_align="left",
        style="default",
    )

    import getpass

    while True:
        console.clear()
        console.rule(program1.title, style="default")
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)))

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))
        opt = IntPrompt.ask("\n[bold]Pilih Opsi", choices=[str(i) for i in menu.keys()])

        match opt:
            case 1:
                kal = input("\nMasukkan teks:\n")
                original_string = Panel(
                    f"\n[text_default]{kal}\n",
                    title="[text_title]Original String",
                    style="default",
                )
                reversed_string = Panel(
                    f"\n[text_default]{reverse_string(kal)}\n",
                    title="[text_title]Reversed String",
                    style="default",
                )

                console.clear()
                console.rule(program1.title, style="default")

                console.print(Padding(original_string, pad=(1, 0, 0, 0)))
                console.print(Padding(reversed_string, pad=(1, 0, 0, 0)))

                getpass.getpass("\nKlik 'enter' untuk melanjutkan")
            case 2:
                list_par = SLinkedList()
                list_reverse_par = SLinkedList()

                original_par = ""
                reverse_par = ""

                print("\nMasukkan teks:")
                while True:
                    par = input()

                    if par == "end":
                        break
                    elif par == "\n":
                        continue
                    list_par.append(par)
                    list_reverse_par.append(reverse_string(par))

                for par in list_par.traverse():
                    original_par += par + "\n"

                for par in list_reverse_par.traverse():
                    reverse_par += par + "\n"

                console.clear()
                console.rule(program1.title, style="default")

                original_string = Panel(
                    f"\n[text_default]{original_par[:len(original_par)-1]}\n",
                    title="[text_title]Original String",
                    style="default",
                )
                reversed_string = Panel(
                    f"\n[text_default]{reverse_par[:len(reverse_par)-1]}\n",
                    title="[text_title]Reversed String",
                    style="default",
                )
                console.print(Padding(original_string, pad=(1, 0, 0, 0)))
                console.print(Padding(reversed_string, pad=(1, 0, 0, 0)))

                getpass.getpass("\nKlik 'enter' untuk melanjutkan")

            case 3:
                return program1.stop()


title = "[text_title]Program 1: Reverse String"  # untuk di tampilkan sebagai judul
name = "Reverse String dengan Linked List"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 1 merupakan program untuk membalik string (reverse string). 
🔷 Pada program ini pembalikkan string dilakukan dengan menggunakan struktur data linked list. 
🔷 Program ini memiliki opsi untuk membalikkan string secara keseluruhan atau per kata.\n"""  # deskripsi program

program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()
