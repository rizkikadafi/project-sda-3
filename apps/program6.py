from typing import Tuple
from utils.app import *


def priority(simbol):
    precedence = None
    match simbol:
        case "(":
            precedence = 1
        case ")":
            precedence = 2
        case "+" | "-":
            precedence = 3
        case "*" | "/" | "%":
            precedence = 4
        case "^":
            precedence = 5
        case _:
            precedence = 0

    return precedence


class InfixPrompt(PromptBase):
    response_type = str
    validate_error_massage = "[prompt.invalid]Ekspresi yang anda masukkan tidak valid!"
    error_empty_value = "[prompt.invalid]Input tidak boleh kosong!"

    def process_response(self, value: str):
        operator = ["+", "-", "*", "/", "^", "%"]
        parenthesis_stack = []

        if value == "":
            raise InvalidResponse(self.error_empty_value)

        list_token = value.split()

        if len(list_token) == 1 and (
            not priority(list_token[0]) == 0 or not list_token[0].isalnum()
        ):
            raise InvalidResponse(self.validate_error_massage)

        even = True
        for token in list_token:
            if len(token) == 1:
                if (
                    (even and not priority(token) == 0)
                    or (not even and token not in operator)
                    or (even and priority(token) == 0 and not token.isalnum())
                ):
                    raise InvalidResponse(self.validate_error_massage)
            else:
                list_char = [char for char in token]
                for char in list_char:
                    if priority(char) == 2 and len(parenthesis_stack) == 0:
                        raise InvalidResponse(self.validate_error_massage)

                    if priority(char) == 1:
                        parenthesis_stack.append(char)
                    elif priority(char) == 2:
                        parenthesis_stack.pop()
                    elif priority(char) == 0:
                        continue
                    else:
                        raise InvalidResponse(self.validate_error_massage)
            even = not even
        if len(parenthesis_stack) != 0:
            raise InvalidResponse(self.validate_error_massage)

        return value


class PostfixPrompt(PromptBase):
    response_type = str
    validate_error_massage = "[prompt.invalid]Ekspresi yang anda masukkan tidak valid!"
    error_empty_value = "[prompt.invalid]Input tidak boleh kosong!"
    error_value_type = "[prompt.invalid]Operand harus berupa angka!"

    def process_response(self, value: str):
        operand_stack = []
        operator = ["+", "-", "*", "/", "^", "%"]

        if value == "":
            raise InvalidResponse(self.error_empty_value)

        list_token = value.split()

        for token in list_token:
            if token[0] in operator:
                if len(operand_stack) < 2 or len(token) > 1:
                    raise InvalidResponse(self.validate_error_massage)
                else:
                    operand_stack.pop()
            elif priority(token) == 0:
                if not token.replace(".", "").isdecimal():
                    raise InvalidResponse(self.error_value_type)
                else:
                    operand_stack.append(token)
            else:
                raise InvalidResponse(self.validate_error_massage)

        return value


class PrefixPrompt(PromptBase):
    response_type = str
    validate_error_massage = "[prompt.invalid]Ekspresi yang anda masukkan tidak valid!"
    error_empty_value = "[prompt.invalid]Input tidak boleh kosong!"
    error_value_type = "[prompt.invalid]Operand harus berupa angka!"

    def process_response(self, value: str):
        operand_stack = []
        operator = ["+", "-", "*", "/", "^", "%"]

        if value == "":
            raise InvalidResponse(self.error_empty_value)

        list_token = value.split()
        list_token.reverse()

        for token in list_token:
            if token[0] in operator:
                if len(operand_stack) < 2 or len(token) > 1:
                    raise InvalidResponse(self.validate_error_massage)
                else:
                    operand_stack.pop()
            elif priority(token) == 0:
                if not token.replace(".", "").isdecimal():
                    raise InvalidResponse(self.error_value_type)
                else:
                    operand_stack.append(token)
            else:
                raise InvalidResponse(self.validate_error_massage)

        return value


def reverse_infix(infix_str: str):
    list_infix = [char for char in infix_str]
    reversed_infix = ""
    while len(list_infix) != 0:
        char = list_infix.pop()
        if char == "(":
            reversed_infix += ")"
        elif char == ")":
            reversed_infix += "("
        else:
            reversed_infix += char

    return reversed_infix


def evalPostfix(postfix_str: str):
    list_postfix = postfix_str.split()

    stack = []
    eval_stack = []

    table_eval_postfix = Table(title="[text_title]Tabel Eval Postfix", style="default")

    table_eval_postfix.add_column("[text_title]Simbol", style="text_default")
    table_eval_postfix.add_column("[text_title]Stack", style="text_default")
    table_eval_postfix.add_column("[text_title]Eval Stack", style="text_default")

    for token in list_postfix:
        if priority(token) == 0:
            stack.append(token)
            eval_stack.append(str(eval(token)))
            table_eval_postfix.add_row(
                f"{token}", f"{' '.join(stack)}", f"{' '.join(eval_stack)}"
            )
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            infix_string = f"({operand1} {token} {operand2})"
            stack.append(infix_string)
            eval_stack.pop()
            eval_stack.pop()
            eval_stack.append(str(eval(infix_string.replace("^", "**"))))
            table_eval_postfix.add_row(
                f"{token}", f"{' '.join(stack)}", f"{' '.join(eval_stack)}"
            )

    infix_expression = stack.pop()
    return (
        infix_expression,
        eval(infix_expression.replace("^", "**")),
        table_eval_postfix,
    )


def evalPrefix(prefix_str: str):
    list_reverse_prefix = prefix_str.split()
    list_reverse_prefix.reverse()

    stack = []
    eval_stack = []

    table_eval_prefix = Table(title="[text_title]Tabel Eval Prefix", style="default")

    table_eval_prefix.add_column("[text_title]Simbol", style="text_default")
    table_eval_prefix.add_column("[text_title]Stack", style="text_default")
    table_eval_prefix.add_column("[text_title]Eval Stack", style="text_default")

    for token in list_reverse_prefix:
        if priority(token) == 0:
            stack.append(token)
            eval_stack.append(str(eval(token)))
            table_eval_prefix.add_row(
                f"{token}", f"{' '.join(stack)}", f"{' '.join(eval_stack)}"
            )
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_string = f"({operand1} {token} {operand2})"
            stack.append(infix_string)
            eval_stack.pop()
            eval_stack.pop()
            eval_stack.append(str(eval(infix_string.replace("^", "**"))))
            table_eval_prefix.add_row(
                f"{token}", f"{' '.join(stack)}", f"{' '.join(eval_stack)}"
            )

    infix_expression = stack.pop()
    return (
        infix_expression,
        eval(infix_expression.replace("^", "**")),
        table_eval_prefix,
    )


def infixToPostfix(expression: str) -> Tuple:
    stack = []
    infix_str = expression + ")"
    postfix_str = ""

    table_postfix = Table(title="[text_title]Tabel Postfix", style="default")

    table_postfix.add_column("[text_title]Simbol", style="text_default")
    table_postfix.add_column("[text_title]Prioritas", style="text_default")
    table_postfix.add_column("[text_title]Stack", style="text_default")
    table_postfix.add_column("[text_title]Pop Karakter", style="text_default")
    table_postfix.add_column("[text_title]String Postfix", style="text_default")

    stack.append("(")

    char = ""
    only_once = False
    for token in infix_str:
        if token == " ":
            continue
        precedence = priority(token)
        match precedence:
            case 0:
                postfix_str += token
            case 1:
                stack.append(token)
            case 2:
                char = stack.pop()
                count = 0
                while char != "(":
                    postfix_str += char
                    table_postfix.add_row(
                        f"{token if count == 0 else ''}",
                        f"{priority(token) if count == 0 else ''}",
                        f"{''.join(stack)}",
                        f"{char}",
                        f"{postfix_str}",
                    )
                    char = stack.pop()
                    count = 1
                only_once = True if count == 1 else False
            case 3 | 4 | 5:
                char = stack.pop()
                count = 0
                while priority(char) >= precedence:
                    postfix_str += char
                    table_postfix.add_row(
                        f"{token if count == 0 else ''}",
                        f"{priority(token) if count == 0 else ''}",
                        f"{''.join(stack)}",
                        f"{char}",
                        f"{postfix_str}",
                    )
                    char = stack.pop()
                    count = 1

                stack.append(char)
                stack.append(token)
                only_once = True if count == 1 else False
        table_postfix.add_row(
            f"{token if not only_once else ''}",
            f"{priority(token) if not only_once else ''}",
            f"{''.join(stack)}",
            f"{char if priority(token) == 2 else ''}",
            f"{postfix_str}",
        )
        only_once = False

    return (postfix_str, infix_str, table_postfix)


def infixToPrefix(expression: str) -> Tuple:
    stack = []
    infix_str = reverse_infix(expression) + ")"
    postfix_str = ""

    table_prefix = Table(title="[text_title]Tabel Prefix", style="default")

    table_prefix.add_column("[text_title]Simbol", style="text_default")
    table_prefix.add_column("[text_title]Prioritas", style="text_default")
    table_prefix.add_column("[text_title]Stack", style="text_default")
    table_prefix.add_column("[text_title]Pop Karakter", style="text_default")
    table_prefix.add_column("[text_title]Reverse String Prefix", style="text_default")

    stack.append("(")

    char = ""
    only_once = False
    for token in infix_str:
        if token == " ":
            continue
        precedence = priority(token)
        match precedence:
            case 0:
                postfix_str += token
            case 1:
                stack.append(token)
            case 2:
                char = stack.pop()
                count = 0
                while char != "(":
                    postfix_str += char
                    table_prefix.add_row(
                        f"{token if count == 0 else ''}",
                        f"{priority(token) if count == 0 else ''}",
                        f"{''.join(stack)}",
                        f"{char}",
                        f"{postfix_str}",
                    )
                    char = stack.pop()
                    count = 1
                only_once = True if count == 1 else False
            case 3 | 4 | 5:
                char = stack.pop()
                count = 0
                while priority(char) >= precedence:
                    postfix_str += char
                    table_prefix.add_row(
                        f"{token if count == 0 else ''}",
                        f"{priority(token) if count == 0 else ''}",
                        f"{''.join(stack)}",
                        f"{char}",
                        f"{postfix_str}",
                    )
                    char = stack.pop()
                    count = 1

                stack.append(char)
                stack.append(token)
                only_once = True if count == 1 else False
        table_prefix.add_row(
            f"{token if not only_once else ''}",
            f"{priority(token) if not only_once else ''}",
            f"{''.join(stack)}",
            f"{char if priority(token) == 2 else ''}",
            f"{postfix_str}",
        )
        only_once = False

    prefix_str = postfix_str[::-1]

    return (prefix_str, infix_str, table_prefix)


def main():
    menu = {
        1: "Konversi",
        2: "Evaluasi",
        3: "Keluar program",
    }

    menu_str = "\n[text_default]"
    for k, v in menu.items():
        menu_str += f"{k}. {v}\n"

    eval_menu = {
        1: "Eval Postfix",
        2: "Eval Prefix",
    }

    eval_menu_str = "\n[text_default]"
    for k, v in eval_menu.items():
        eval_menu_str += f"{k}. {v}\n"

    docs_conversion = """
Masukkan ekspresi Infix dengan spasi antar operand dan operator.
Tidak ada spasi antar kurung dan operand.

contoh 1: 2 + 4 / 5 * (5 - 3) ^ 5 ^ 4
contoh 2: A + B / C * (D - A) ^ F ^ H
"""
    docs_eval_postfix = """
Masukkan ekspresi Postfix dengan spasi antar operand dan operator.
Operand harus berupa angka.

contoh: 4 55 + 62 23 - *
"""
    docs_eval_prefix = """
Masukkan ekspresi prefix dengan spasi antar operand dan operator.
Operand harus berupa angka.

contoh: + - 2 7 * 8 / 4 12
"""

    panel_menu = Panel(
        menu_str, title="[text_title]Menu", title_align="left", style="default"
    )
    panel_description = Panel(
        program6.description,
        title="[text_title]Deskripsi Program",
        title_align="left",
        style="default",
    )
    panel_docs_conversion = Panel(
        Text(docs_conversion, style="text_default", justify="center"),
        title="[text_title]INFO",
        title_align="center",
        style="default",
    )
    panel_docs_eval_postfix = Panel(
        Text(docs_eval_postfix, style="text_default", justify="center"),
        title="[text_title]INFO",
        title_align="center",
        style="default",
    )
    panel_docs_eval_prefix = Panel(
        Text(docs_eval_prefix, style="text_default", justify="center"),
        title="[text_title]INFO",
        title_align="center",
        style="default",
    )
    panel_eval_menu = Panel(
        eval_menu_str,
        title="[text_title]Opsi Evaluasi",
        title_align="left",
        style="default",
    )

    while True:
        console.clear()
        console.rule(program6.title, style="default")
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)))

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))
        opt = IntPrompt.ask("\n[bold]Pilih Menu", choices=[str(i) for i in menu.keys()])

        import getpass

        match opt:
            case 1:
                console.clear()
                console.rule(program6.title, style="default")
                console.print(Padding(panel_docs_conversion, pad=(1, 0, 0, 0)))

                infix_expression = InfixPrompt.ask("\n[bold]Masukkan ekspresi Infix")
                result_postfix = infixToPostfix(infix_expression)
                result_prefix = infixToPrefix(infix_expression)

                layout_result = Layout(name="result")

                layout_result.split_row(
                    Layout(name="result_postfix", ratio=5),
                    Layout(name="result_prefix", ratio=5),
                )
                layout_result["result_postfix"].update(
                    Panel(
                        Text(
                            f"\n{result_postfix[0]}\n",
                            justify="center",
                            style="text_default",
                        ),
                        title=f"[text_title]Postfix",
                        style="default",
                    )
                )
                layout_result["result_prefix"].update(
                    Panel(
                        Text(
                            f"\n{result_prefix[0]}\n",
                            justify="center",
                            style="text_default",
                        ),
                        title=f"[text_title]Prefix",
                        style="default",
                    )
                )

                layout_initial_infix = Layout(name="initial_infix")

                layout_initial_infix["initial_infix"].split_row(
                    Layout(name="for_postfix"),
                    Layout(name="for_prefix"),
                )

                text_infix_postfix = Group(
                    Align(
                        Text("\nString Infix Awal", style="bold underline"),
                        align="center",
                    ),
                    Align(Text(f"{result_postfix[1]}", style="bold"), align="center"),
                )
                text_infix_prefix = Group(
                    Align(
                        Text("\nString Infix Awal (Reverse)", style="bold underline"),
                        align="center",
                    ),
                    Align(Text(f"{result_prefix[1]}", style="bold"), align="center"),
                )

                layout_initial_infix["for_postfix"].update(text_infix_postfix)
                layout_initial_infix["for_prefix"].update(text_infix_prefix)

                layout_table = Layout(name="table")

                layout_table["table"].split_row(
                    Layout(name="table_postfix"),
                    Layout(
                        name="table_prefix",
                    ),
                )
                layout_table["table_postfix"].update(
                    Align(result_postfix[2], align="center")
                )
                layout_table["table_prefix"].update(
                    Align(result_prefix[2], align="center")
                )

                if Confirm.ask(
                    "\n[bold]Apakah anda ingin menampilkan proses koneversi"
                ):
                    console.clear()
                    console.rule(program6.title, style="default")
                    console.print(layout_result, height=5)
                    console.print(layout_initial_infix, height=4)
                    console.print(layout_table, height=28)
                else:
                    console.clear()
                    console.rule(program6.title, style="default")
                    console.print(Padding(layout_result, pad=(1, 0, 0, 1)), height=6)
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                console.clear()
                console.rule(program6.title, style="default")
                console.print(Padding(panel_eval_menu, pad=(1, 0, 0, 0)))

                opt = IntPrompt.ask("\n[bold]Pilih opsi untuk evaluasi")

                layout_eval = Layout(name="layout_eval")
                layout_eval["layout_eval"].split_row(
                    Layout(name="initial", ratio=5),
                    Align.center(Text("➔", justify="center"), vertical="middle"),
                    Layout(name="infix", ratio=5),
                    Align.center(Text("➔", justify="center"), vertical="middle"),
                    Layout(name="eval", ratio=5),
                )

                match opt:
                    case 1:
                        console.clear()
                        console.rule(program6.title, style="default")
                        console.print(
                            Padding(panel_docs_eval_postfix, pad=(1, 0, 0, 0))
                        )

                        postfix_expression = PostfixPrompt.ask(
                            "\n[bold]Masukkan ekspresi Postfix"
                        )

                        result_eval = evalPostfix(postfix_expression)

                        layout_eval["initial"].update(
                            Panel(
                                Text(
                                    f"\n{postfix_expression}\n",
                                    justify="center",
                                    style="text_default",
                                ),
                                title=f"[text_title]Postfix",
                                style="default",
                            )
                        )
                        layout_eval["infix"].update(
                            Panel(
                                Text(
                                    f"\n{result_eval[0]}\n",
                                    justify="center",
                                    style="text_default",
                                ),
                                title=f"[text_title]Infix",
                                style="default",
                            )
                        )
                        layout_eval["eval"].update(
                            Panel(
                                Text(
                                    f"\n{result_eval[1]}\n",
                                    justify="center",
                                    style="text_default",
                                ),
                                title=f"[text_title]Hasil Evaluasi",
                                style="default",
                            )
                        )

                        if Confirm.ask(
                            "\n[bold]Apakah anda ingin menampilkan proses evaluasi"
                        ):
                            console.clear()
                            console.rule(program6.title, style="default")
                            console.print(
                                Padding(layout_eval, pad=(1, 0, 1, 0)), height=7
                            )
                            console.print(result_eval[2], justify="center")
                        else:
                            console.clear()
                            console.rule(program6.title, style="default")
                            console.print(
                                Padding(layout_eval, pad=(1, 0, 1, 0)), height=7
                            )
                    case 2:
                        console.clear()
                        console.rule(program6.title, style="default")
                        console.print(Padding(panel_docs_eval_prefix, pad=(1, 0, 0, 0)))

                        prefix_expression = PrefixPrompt.ask(
                            "\n[bold]Masukkan ekspresi Prefix"
                        )

                        result_eval = evalPrefix(prefix_expression)

                        layout_eval["initial"].update(
                            Panel(
                                Text(
                                    f"\n{prefix_expression}\n",
                                    justify="center",
                                    style="text_default",
                                ),
                                title=f"[text_title]Prefix",
                                style="default",
                            )
                        )
                        layout_eval["infix"].update(
                            Panel(
                                Text(
                                    f"\n{result_eval[0]}\n",
                                    justify="center",
                                    style="text_default",
                                ),
                                title=f"[text_title]Infix",
                                style="default",
                            )
                        )
                        layout_eval["eval"].update(
                            Panel(
                                Text(
                                    f"\n{result_eval[1]}\n",
                                    justify="center",
                                    style="text_default",
                                ),
                                title=f"[text_title]Hasil Evaluasi",
                                style="default",
                            )
                        )

                        if Confirm.ask(
                            "\n[bold]Apakah anda ingin menampilkan proses evaluasi"
                        ):
                            console.clear()
                            console.rule(program6.title, style="default")
                            console.print(
                                Padding(layout_eval, pad=(1, 0, 1, 0)), height=7
                            )
                            console.print(result_eval[2], justify="center")
                        else:
                            console.clear()
                            console.rule(program6.title, style="default")
                            console.print(
                                Padding(layout_eval, pad=(1, 0, 1, 0)), height=7
                            )

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                return program6.stop()


# untuk di tampilkan sebagai judul
title = "[text_title]Program 6: Konversi Infix"
name = "Konversi infix"  # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 6 merupakan program untuk menkonversi ekspresi infix ke postfix dan juga prefix.
🔷 Program ini juga dapat mengevaluasi ekspresi postfix dan juga prefix.\n"""  # deskripsi program

program6 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program6.start()
