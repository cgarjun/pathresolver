name = "pathresolver"

version = "0.0.1"

authors = [
    "arjun.thekkumadathil"
]

description = "Show context based app launcher"

tools = [
    "path_resolver_qc",
]

requires = [
    "python-2.7+<3",
    "nlogger-0+<1",
]

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")
    env.PATHRESOLVER_TEMPLATE_DIR = "{root}/template"