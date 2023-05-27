from utils.app import *

from data_structure.linked_list import DLinkedList


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


def empty_data_panel(operation: str) -> Panel:
    """Panel untuk menampilkan info ketika data kosong."""

    panel = Panel("None")
    match operation:
        case "deletion":
            panel = Panel(
                Text(
                    "\nLinked List Kosong! Tidak ada data yang bisa dihapus!\n",
                    justify="center",
                    style="text_warning",
                ),
                title="[title_warning]INFO",
                style="warning",
            )
        case "display_data":
            panel = Panel(
                Text(
                    "\nLinked List Kosong! Tidak ada data yang bisa ditampilkan!\n",
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
                f"Data [{data}] tidak ada dalam Linked List!",
                justify="center",
                style="text_warning",
            ),
            pad=(1, 0, 1, 0),
        ),
        title="[title_warning]INFO",
        style="warning",
    )

    return panel


def table_data(data: DLinkedList, opt: str, search_data=None) -> Table:
    """Tabel untuk menampilkan data."""

    table = Table(style="default")
    table.add_column("[text_title]No.", style="text_default", justify="center")
    table.add_column("[text_title]Data", style="text_default", min_width=20)

    match opt:
        case "all_data_forward":
            table.title = "[text_title]Data Pada Linked List (Forward)"

            for i, d in enumerate(data.traverse()):
                table.add_row(f"{i+1}", str(d))
        case "all_data_backward":
            table.title = "[text_title]Data Pada Linked List (Backward)"

            for i, d in enumerate(data.traverse(reverse=True)):
                table.add_row(f"{i+1}", str(d))
        case "search_data":
            table.title = "[text_title]Data Pada Linked List"
            list_data = [d for d in data.traverse()]
            table.add_row(f"{list_data.index(search_data)+1}", str(search_data))

    return table


def main():
    menu = {1: "Tambah data", 2: "Tampilkan data", 3: "Hapus data", 4: "Keluar program"}

    menu_str = "\n[text_default]"
    for k, v in menu.items():
        menu_str += f"{k}. {v}\n"

    insert_data_opt = {
        1: "Tambah data diawal",
        2: "Tambah data diakhir",
        3: "Tambah data sebelum data tertentu",
        4: "Tambah data setelah data tertentu",
    }

    insert_data_opt_str = "\n[text_default]"
    for k, v in insert_data_opt.items():
        insert_data_opt_str += f"{k}. {v}\n"

    display_data_opt = {1: "Forward", 2: "Backward"}

    display_data_opt_str = "\n[text_default]"
    for k, v in display_data_opt.items():
        display_data_opt_str += f"{k}. {v}\n"

    delete_data_opt = {
        1: "Hapus data terdepan",
        2: "Hapus data terbelakang",
        3: "Hapus data berdasarkan nama",
    }

    delete_data_opt_str = "\n[text_default]"
    for k, v in delete_data_opt.items():
        delete_data_opt_str += f"{k}. {v}\n"

    panel_menu = Panel(
        menu_str, title="[text_title]Menu", title_align="left", style="default"
    )
    panel_description = Panel(
        program5.description,
        title="[text_title]Deskripsi Program",
        title_align="left",
        style="default",
    )
    panel_insert_data_opt = Panel(
        insert_data_opt_str,
        title="[text_title]Opsi Tampilan Data",
        title_align="left",
        style="default",
    )
    panel_display_data_opt = Panel(
        display_data_opt_str,
        title="[text_title]Opsi Tampilan Data",
        title_align="left",
        style="default",
    )
    panel_delete_data_opt = Panel(
        delete_data_opt_str,
        title="[text_title]Opsi Penghapusan Data",
        title_align="left",
        style="default",
    )

    double_linked_list = DLinkedList()

    while True:
        console.clear()
        console.rule(program5.title, style="default")
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)))

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))
        opt = IntPrompt.ask("\n[bold]Pilih Menu", choices=[str(i) for i in menu.keys()])

        import getpass

        match opt:
            case 1:
                console.clear()
                console.rule(program5.title, style="default")

                console.print(Padding(panel_insert_data_opt, pad=(1, 0, 0, 0)))
                opt = IntPrompt.ask(
                    "\n[bold]Pilih Opsi Penambahan Data",
                    choices=[str(i) for i in insert_data_opt.keys()],
                )

                while True:
                    data = Prompt.ask("[bold]\nMasukkan data")
                    if data == "":
                        console.print(
                            "[prompt.invalid]Input yang dimasukkan tidak boleh kosong!"
                        )
                    else:
                        break

                match opt:
                    case 1:
                        double_linked_list.prepend(data)
                        console.print(success_panel(data, operation="addition"))
                    case 2:
                        double_linked_list.append(data)
                        console.print(success_panel(data, operation="addition"))
                    case 3:
                        reference_data = Prompt.ask("[bold]\nMasukkan acuan data")
                        feedback = double_linked_list.add_before(data, reference_data)
                        if feedback == -1:
                            console.print(not_found_data_panel(reference_data))
                        else:
                            console.print(success_panel(data, operation="addition"))
                    case 4:
                        reference_data = Prompt.ask("[bold]\nMasukkan acuan data")
                        feedback = double_linked_list.add_after(data, reference_data)
                        if feedback == -1:
                            console.print(not_found_data_panel(reference_data))
                        else:
                            console.print(success_panel(data, operation="addition"))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                if double_linked_list.empty():
                    console.print(empty_data_panel(operation="display_data"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.clear()
                console.rule(program5.title, style="default")

                console.print(Padding(panel_display_data_opt, pad=(1, 0, 0, 0)))
                opt = IntPrompt.ask(
                    "\n[bold]Pilih Opsi Tampilan Data",
                    choices=[str(i) for i in display_data_opt.keys()],
                )

                match opt:
                    case 1:
                        console.print(
                            table_data(double_linked_list, opt="all_data_forward"),
                            justify="center",
                        )

                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    case 2:
                        console.print(
                            table_data(double_linked_list, opt="all_data_backward"),
                            justify="center",
                        )

                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if double_linked_list.empty():
                    console.print(empty_data_panel(operation="deletion"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.clear()
                console.rule(program5.title, style="default")

                console.print(Padding(panel_delete_data_opt, pad=(1, 0, 0, 0)))
                opt = IntPrompt.ask(
                    "\n[bold]Pilih Opsi Penghapusan Data",
                    choices=[str(i) for i in delete_data_opt.keys()],
                )

                match opt:
                    case 1:
                        first_data = double_linked_list.getFirst()
                        console.print(
                            table_data(
                                double_linked_list,
                                opt="search_data",
                                search_data=first_data,
                            ),
                            justify="center",
                        )

                        if Confirm.ask(
                            "[bold]\nApakah anda yakin ingin menghapus data tersebut?"
                        ):
                            console.print(
                                success_panel(
                                    double_linked_list.popLeft(), operation="deletion"
                                )
                            )
                            getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    case 2:
                        last_data = double_linked_list.getLast()
                        console.print(
                            table_data(
                                double_linked_list,
                                opt="search_data",
                                search_data=last_data,
                            ),
                            justify="center",
                        )

                        if Confirm.ask(
                            "[bold]\nApakah anda yakin ingin menghapus data tersebut?"
                        ):
                            console.print(
                                success_panel(
                                    double_linked_list.pop(), operation="deletion"
                                )
                            )
                            getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    case 3:
                        while True:
                            delete_data = Prompt.ask(
                                "[bold]\nMasukkan data yang ingin dihapus"
                            )
                            if delete_data == "":
                                console.print(
                                    "[prompt.invalid]Input yang dimasukkan tidak boleh kosong!"
                                )
                            else:
                                break

                        if not double_linked_list.contain(delete_data):
                            console.print(not_found_data_panel(delete_data))
                            getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                        else:
                            console.print(
                                table_data(
                                    double_linked_list,
                                    opt="search_data",
                                    search_data=delete_data,
                                ),
                                justify="center",
                            )
                            if Confirm.ask(
                                "[bold]\nApakah anda yakin ingin menghapus data tersebut?"
                            ):
                                double_linked_list.remove(delete_data)
                                console.print(
                                    success_panel(delete_data, operation="deletion")
                                )
                                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                return program5.stop()


title = "[text_title]Program 5: Implementasi Linked List Ganda"  # untuk di tampilkan sebagai judul
name = "Linked List Ganda"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 5 merupakan program implementasi struktur data Linked List Ganda yakni linked list yang setiap Node memiliki 3 bagian, yakni data dan reference yang merujuk pada data sebelum dan setelahnya (prev dan next). 
🔷 Dengan Linked List Ganda memungkinkan pembacaan data dari depan (forward) ataupun dari belakang (backward).
🔷 Program ini memiliki fitur untuk menambah, menghapus, dan menampilkan data.
🔷 Pada menu tampilkan data, user diberi opsi untuk menampilkan data dari depan (forward) atau dari belakang (backward)
🔷 Pada program ini ukuran data yang dapat dimasukkan tidak dibatasi.\n"""  # deskripsi program

program5 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program5.start()
