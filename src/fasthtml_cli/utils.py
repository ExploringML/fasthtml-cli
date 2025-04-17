import fasthtml_cli.fasthtml_templates.base as base
import fasthtml_cli.fasthtml_templates.tailwind as tw
import fasthtml_cli.fasthtml_templates.toml as toml

available_templates = ["base", "tailwind", "toml"]

def create_main_py(name:str, tpl:str, tailwind:bool, reload:bool, pico:bool):
    "Create the main.py file with selected config options."
    
    # Whitelist template.
    if tpl not in available_templates:
        tpl = available_templates[0]

    if tailwind:
        tpl = "tailwind"

    opts = []
    if reload: opts.append("live=True")
    if tailwind: opts.append("pico=False")
    args = ', '.join(opts)
    hdr_opts = f"{args}"

	# @todo: Dynamically get the function from the module.
    if tpl == "base":
        tpl_func = getattr(base, tpl)
        return tpl_func(hdr_opts)
    elif tpl == "tailwind":
        tpl_func = getattr(tw, tpl)
        return tpl_func(hdr_opts)

	# Return the base template as a fallback.
    return tpl_func(hdr_opts)

def create_pyproject_toml(name:str):
    "Create the pyproject.toml file with selected config options."
    
    return toml.config(name)