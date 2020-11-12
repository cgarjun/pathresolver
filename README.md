# pathresolver

token based path building system

## API

Resolving Tokens
```python
from pathresolver import pathresolver

res = pathresolver.PathResolver()
res.list_all_tokens()

token_name = 'show_root'
res = pathresolver.PathResolver(token_name)
res.get_token()

data = {"show":"dummy"}
res.resolve_token(token_name, **data)
```

## CLI
 ```bash
path_resolver_qc -l
2020-11-12 23:17:52,221 INFO pathresolver.py list_all_tokens: show_root: /projects/{show}
2020-11-12 23:17:52,221 INFO pathresolver.py list_all_tokens: all_show_root: /projects

[arjun: dummy/csk/0034/animation]$path_resolver_qc -t show_root
/projects/{show}

[arjun: dummy/csk/0034/animation]$path_resolver_qc -t show_root -td '{"show":"dummy"}'
/projects/{show}
/projects/dummy
 ```
