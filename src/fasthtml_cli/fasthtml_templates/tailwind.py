def tailwind(hdr_opts: str = ""):
    return f"""from fasthtml.common import *

hdrs = (Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"),)
app,rt = fast_app(hdrs=hdrs, {hdr_opts})

@rt('/')
def get(): return Div(P("Hello, world!!", cls="m-6"))

serve()"""
