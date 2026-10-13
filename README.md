# Policy-as-Code Platform

## Overview

A small policy-as-code service that checks container deployment settings before they ship. The `/check` endpoint fails a deployment that uses an image tagged `latest` or runs a privileged container, and a versioned ops API adds workspaces, tenant isolation, job approval and audit records.

- **Built with:** Python, pytest, GitHub Actions
- **Scope:** Local lab with tests; it refuses production changes and does not call a hosted model.

<!-- project-guide:start -->
## Project guide

[Project architecture](PROJECT_ARCHITECTURE.md) · [Interview questions and answers](INTERVIEW_QA.md)

Use the architecture document for the component diagram, implementation boundaries, and verification entry points. The interview guide includes source-backed answers and project walkthroughs.

### Implementation map

| Component | Responsibility |
| --- | --- |
| [`src/policy/main.py`](src/policy/main.py) | HTTP handlers: `GET /healthz`, `POST /check` |
| [`src/policy/gate.py`](src/policy/gate.py) | Functions: `check` |
| [`requirements.txt`](requirements.txt) | Implementation or supporting configuration |
| [`src/policy/__init__.py`](src/policy/__init__.py) | Implementation or supporting configuration |
| [`tests/test_gate.py`](tests/test_gate.py) | Executable checks and regression examples |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | GitHub Actions job definitions |
| [`README.md`](README.md) | Project explanations or operating notes |

### Local setup and verification

From the repository root (the commands follow the checked-in manifests):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

To serve the FastAPI application locally, install the server separately if it is not already available:

```bash
python -m pip install uvicorn
PYTHONPATH=src python -m uvicorn policy.main:app --reload
```

<!-- project-guide:end -->

Level: 14 — Cloud, DevOps & Platform Engineering

Skills: Python, latest and privileged

Fail latest images and privileged true.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.

## Ops plane

Workspaces, tenant isolation, job approval, and audit live under `/v1`. Production apply is refused. See `docs/ARCHITECTURE.md`.

## Documentation checks

Project architecture, interview guides, and local source links are checked automatically on pushes and pull requests. Run the same check locally:

```bash
python3 .github/scripts/validate_project_docs.py
```

See [service improvements and local run instructions](docs/UPGRADES.md).
