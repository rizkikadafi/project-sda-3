from utils.app import *


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next and curr_node.next.data < data:
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node

    def delete_first(self):
        if self.head is None:
            console.print(
                Panel(
                    Text(
                        "\nLinked List Kosong!\n",
                        justify="center",
                        style="text_warning",
                    ),
                    title="[title_warning]INFO",
                    style="warning",
                )
            )
        else:
            self.head = self.head.next
            console.print(
                Panel(
                    Text(
                        f"\nData awal berhasil dihapus.\n",
                        justify="center",
                        style="text_success",
                    ),
                    title="[title_success]INFO",
                    style="success",
                )
            )

    def delete_last(self):
        if self.head is None:
            console.print(
                Panel(
                    Text(
                        "\nLinked List Kosong!\n",
                        justify="center",
                        style="text_warning",
                    ),
                    title="[title_warning]INFO",
                    style="warning",
                )
            )
        elif self.head.next is None:
            self.head = None
            console.print(
                Panel(
                    Text(
                        f"\nData terakhir berhasil dihapus.\n",
                        justify="center",
                        style="text_success",
                    ),
                    title="[title_success]INFO",
                    style="success",
                )
            )
        else:
            curr_node = self.head
            while curr_node.next.next:
                curr_node = curr_node.next
            curr_node.next = None
            console.print(
                Panel(
                    Text(
                        f"\nData terakhir berhasil dihapus.\n",
                        justify="center",
                        style="text_success",
                    ),
                    title="[title_success]INFO",
                    style="success",
                )
            )

    def delete_by_name(self, name):
        if self.head is None:
            console.print(
                Panel(
                    Text(
                        "\nLinked List Kosong!\n",
                        justify="center",
                        style="text_warning",
                    ),
                    title="[title_warning]INFO",
                    style="warning",
                )
            )
        elif self.head.data == name:
            self.head = self.head.next
            console.print(
                Panel(
                    Text(
                        f"\nData dengan nama {name} berhasil dihapus.\n",
                        justify="center",
                        style="text_success",
                    ),
                    title="[title_success]INFO",
                    style="success",
                )
            )
        else:
            curr_node = self.head
            while curr_node.next and curr_node.next.data != name:
                curr_node = curr_node.next
            if curr_node.next:
                curr_node.next = curr_node.next.next
            else:
                console.print(
                    Panel(
                        Text(
                            "\nData tidak ditemukan!\n",
                            justify="center",
                            style="text_warning",
                        ),
                        title="[title_warning]INFO",
                        style="warning",
                    )
                )

    def delete_all(self):
        self.head = None
        console.print(
            Panel(
                Text(
                    f"\nSemua data telah terhapus.\n",
                    justify="center",
                    style="text_success",
                ),
                title="[title_success]INFO",
                style="success",
            )
        )

    def display(self):
        if self.head is None:
            console.print(
                Panel(
                    Text(
                        "\nLinked List Kosong!\n",
                        justify="center",
                        style="text_warning",
                    ),
                    title="[title_warning]INFO",
                    style="warning",
                )
            )
        else:
            curr_node = self.head
            table = Table(
                style="default", title="[text_title]Data dalam Linked List (Ascending)"
            )
            table.add_column("[text_title]No.", style="text_default", justify="center")
            table.add_column("[text_title]Data", style="text_default", min_width=20)

            count = 1
            while curr_node:
                table.add_row(f"{count}", curr_node.data)
                curr_node = curr_node.next

            console.print(table, justify="center")


def success_panel(value, operation: str) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""

    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(
                Text(
                    f"\n[{value}] berhasil dimasukkan.\n",
                    justify="center",
                    style="text_success",
                ),
                title="[title_success]INFO",
                style="success",
            )
        case "deletion":
            panel = Panel(
                Text(
                    f"\n[{value}] berhasil dihapus!\n",
                    justify="center",
                    style="text_success",
                ),
                title="[text_success]INFO",
                style="success",
            )

    return panel


def main():
    menu = {1: "Tambah data", 2: "Hapus data", 3: "Tampilkan data", 4: "Keluar program"}

    menu_str = "\n[text_default]"
    for k, v in menu.items():
        menu_str += f"{k}. {v}\n"

    delete_opt = {
        1: "Hapus data awal",
        2: "Hapus data terakhir",
        3: "Hapus data dengan nama",
        4: "Hapus seluruh data",
    }
    delete_opt_str = "\n[text_default]"
    for k, v in delete_opt.items():
        delete_opt_str += f"{k}. {v}\n"

    panel_menu = Panel(
        menu_str, title="[text_title]Menu", title_align="left", style="default"
    )
    panel_delete_opt = Panel(
        delete_opt_str,
        title="[text_title]Opsi Penghapusan data",
        title_align="left",
        style="default",
    )
    panel_description = Panel(
        program4.description,
        title="[text_title]Deskripsi Program",
        title_align="left",
        style="default",
    )

    linked_list = LinkedList()

    while True:
        console.clear()
        console.rule(program4.title, style="default")
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)))

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))
        choice = IntPrompt.ask(
            "\n[bold]Masukkan pilihan menu", choices=[str(i) for i in menu.keys()]
        )

        import getpass

        match choice:
            case 1:
                data = Prompt.ask("\n[bold]Masukkan data")
                linked_list.insert(data)

                console.print(success_panel(data, operation="addition"))
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                console.clear()
                console.rule(program4.title, style="default")

                console.print(Padding(panel_delete_opt, pad=(1, 0, 0, 0)))

                delete_choice = IntPrompt.ask(
                    "\n[bold]Masukkan pilihan hapus data",
                    choices=[str(i) for i in delete_opt.keys()],
                )

                match delete_choice:
                    case 1:
                        linked_list.delete_first()
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    case 2:
                        linked_list.delete_last()
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    case 3:
                        name = Prompt.ask(
                            "\n[bold]Masukkan nama data yang akan dihapus"
                        )
                        linked_list.delete_by_name(name)
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    case 4:
                        linked_list.delete_all()
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

            case 3:
                linked_list.display()
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                return program4.stop()


title = "[text_title]Program 4: Implementasi Linked List"  # untuk di tampilkan sebagai judul
name = "Linked List (Pengurutan Data)"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 4 merupakan program implementasi struktur data Linked List untuk mengurutkan data.
🔷 Data yang dimasukkan akan otomatis diurutkan secara menaik (ascending). 
🔷 Pada program ini ukuran data yang dapat dimasukkan tidak dibatasi.\n"""  # deskripsi program

program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
