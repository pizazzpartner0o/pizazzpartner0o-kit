# pizazzpartner0o-kit

Validate JSON files and print a normalized form.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m pizazzpartner0o_kit.cli --help
```

```python
from pizazzpartner0o_kit.core import Pizazzpartner0oTool

tool = Pizazzpartner0oTool()
print(tool)
```

## Layout

```
pizazzpartner0o_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 pizazzpartner0o
