def base(hdr_opts: str = ""):
    return f"""from fasthtml.common import *

app,rt = fast_app({hdr_opts})

@rt('/')
def get(): return Div(P("Hello, world!!"))

serve()"""