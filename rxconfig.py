import reflex as rx

config = rx.Config(
    app_name="PyProject",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)