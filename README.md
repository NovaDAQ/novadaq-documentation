# novadaq-documentation

Documentation and a severity-ranked code review for all 120 NOvA DAQ package repositories.

- [Published documentation](https://novadaq.github.io/novadaq-documentation/)
- [Remediation priorities and GitHub issues](docs/review/index.md)
- [Package catalog](docs/packages/index.md)
- [System architecture](docs/architecture/index.md) and [dependency diagrams](docs/architecture/dependencies.md)
- [Operations](docs/operations/index.md), [build/release](docs/operations/build.md), and [recovery](docs/operations/recovery.md)
- [Review scope and limits](docs/review/methodology.md)
- [Executed validation](docs/review/validation.md)
- [Build, update, and maintain](docs/contributing.md)

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/mkdocs build --strict
.venv/bin/mkdocs serve -a 127.0.0.1:8000
```

The review snapshot is dated 2026-09-30. This is an independent documentation package; it does not modify or build the DAQ software. See the coverage ledger for the review depth, tool inputs, preserved local changes, and unperformed runtime/hardware validation.
