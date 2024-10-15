import flet as ft

def main(page: ft.Page):
    
    def sair_aplicacao(e):
        page.window_close()



    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.CODE),
        bgcolor = "#003377", color=ft.colors.WHITE,
        title = ft.Text("Meu APP", color=ft.colors.WHITE),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem("Menu"),
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.LOGIN, color=ft.colors.BLACK),
                                ft.Text("Login"),
                            ],
                        ),
                        on_click=lambda _: print("Botão Login Clicado"),
                    ),
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.SHOPPING_CART, color=ft.colors.BLACK),
                                ft.Text("Shop"),
                            ],
                        ),
                        on_click=lambda _: print("Botão Shop Clicado"),
                    ),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text= 'Sair',
                        on_click=sair_aplicacao

                    )

                ]
            )
        ]

    )






    page.add(
        ft.Text("Corpo"),
    )

ft.app(target=main)