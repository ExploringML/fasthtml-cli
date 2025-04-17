def tailwind(hdr_opts: str = ""):
    return f"""from fasthtml.common import *

hdrs = (Script(src="https://cdn.tailwindcss.com"),)
app,rt = fast_app(hdrs=hdrs, {hdr_opts})

@rt('/')
def get(): return Div(P("Hello, world!!", cls="m-6"))

serve()"""
