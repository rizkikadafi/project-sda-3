from utils.app import *
from data_structure.linked_list import SLinkedList


def success_panel(value, operation: str) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""

    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(
                Text(
                    f"\n[{value}] telah masuk dalam tumpukan!.\n",
                    justify="center",
                    style="text_success",
                ),
                title="[title_success]INFO",
                style="success",
            )
        case "deletion":
            panel = Panel(
                Text(
                    f"\n[{value}] telah dihapus dari tumpukan!\n",
                    justify="center",
                    style="text_success",
                ),
                title="[text_success]INFO",
                style="success",
            )

    return panel


def empty_data_panel(operation: str) -> Panel:
    """Panel untuk menampilkan info ketika data kosong."""

    panel = Panel("None")
    match operation:
        case "deletion":
            panel = Panel(
                Text(
                    "\nTumpukan Kosong! Tidak ada data yang bisa dihapus!\n",
                    justify="center",
                    style="text_warning",
                ),
                title="[title_warning]INFO",
                style="warning",
            )
        case "display_data":
            panel = Panel(
                Text(
                    "\nTumpukan Kosong! Tidak ada data yang bisa ditampilkan!\n",
                    justify="center",
                    style="text_warning",
                ),
                title="[title_warning]INFO",
                style="warning",
            )

    return panel


def not_found_data_panel(data) -> Panel:
    """Panel untuk menampilkan infor ketika data yang dicari tidak ditemukan."""

    panel = Panel(
        Padding(
            Text(
                f"Data [{data}] tidak ada dalam tumpukan!",
                justify="center",
                style="text_warning",
            ),
            pad=(1, 0, 1, 0),
        ),
        title="[title_warning]INFO",
        style="warning",
    )

    return panel


def table_data(data: SLinkedList, opt: str, search_data=None) -> Table | Panel:
    """Tabel untuk menampilkan data."""

    table = Table(style="default")
    table.add_column("[text_title]No.", style="text_default", justify="center")
    table.add_column("[text_title]Data", style="text_default", min_width=20)

    list_data = [d for d in data.traverse()]

    match opt:
        case "top_data":
            table.title = "[text_title]Data Teratas"
            table.add_row("1", data.getLast())
        case "all_data":
            table.title = "[text_title]Data Pada Tumpukan"

            for i in range(data.size):
                table.add_row(f"{i+1}", list_data.pop())

    return table


def main():
    menu = {
        1: "Tambah Data",
        2: "Tampilkan Data",
        3: "Hapus Data Teratas",
        4: "Keluar Program",
    }

    menu_str = "\n[text_default]"
    for k, v in menu.items():
        menu_str += f"{k}. {v}\n"

    display_data_opt = {
        1: "Tampilkan Data Teratas",
        2: "Tampilkan Seluruh Data",
    }

    display_data_opt_str = "\n[text_default]"
    for k, v in display_data_opt.items():
        display_data_opt_str += f"{k}. {v}\n"

    panel_description = Panel(
        program2.description,
        title="[text_title]Deskripsi Program",
        title_align="left",
        style="default",
    )
    panel_menu = Panel(
        menu_str, title="[text_title]Menu", title_align="left", style="default"
    )
    panel_display_data_opt = Panel(
        display_data_opt_str,
        title="[text_title]Opsi Tampilan Data",
        title_align="left",
        style="default",
    )

    data = SLinkedList()

    while True:
        console.clear()
        console.rule(program2.title, style="default")
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)))

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))
        pilihan = IntPrompt.ask(
            "\n[bold]Silahkan masukkan pilihan anda",
            choices=[str(i) for i in menu.keys()],
        )

        import getpass

        match pilihan:
            case 1:
                obj = Prompt.ask("[bold]\nMasukkan data")
                data.append(obj)

                console.print(success_panel(obj, operation="addition"))
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                if data.empty():
                    console.print(empty_data_panel(operation="display_data"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.clear()
                console.rule(program2.title, style="default")

                console.print(Padding(panel_display_data_opt, pad=(1, 0, 0, 0)))
                opt = IntPrompt.ask(
                    "\n[bold]Pilih Opsi Tampilan Data",
                    choices=[str(i) for i in display_data_opt.keys()],
                )

                match opt:
                    case 1:
                        console.print(
                            table_data(data, opt="top_data"), justify="center"
                        )
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    case 2:
                        console.print(
                            table_data(data, opt="all_data"), justify="center"
                        )
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if data.empty():
                    console.print(empty_data_panel(operation="deletion"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.print(table_data(data, opt="top_data"), justify="center")
                if Confirm.ask(
                    "\n[bold]Apakah anda yakin ingin menghapus data tersebut?"
                ):
                    console.print(success_panel(data.pop(), operation="deletion"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                return program2.stop()


title = "[text_title]Program 2: Implementasi Tumpukan dengan Linked List"  # untuk di tampilkan sebagai judul
name = "Tumpukan dengan Linked List"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 2 merupakan program implementasi struktur data Tumpukan (stack) dengan linked list.
🔷 Prgram ini memiliki fitur untuk menambahkan, menampilkan dan menghapus data.
🔷 Pada program ini ukuran data yang dapat dimasukkan tidak dibatasi.\n"""  # deskripsi program

program2 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program2.start()
