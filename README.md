# SolidPy Domain submodule template
Base structure for SolidPy.Domain submodule

# Basic Setup
- Configure Poetry Auth to use GCP Artifact Registry:
- `$ poetry config http-basic.pypi-gcp oauth2accesstoken $(gcloud auth print-access-token)`
- Edit `pyproject.toml` and replace all __\*placeholders\*__ with actual values
- Add additional dependencies to `pyproject.toml` as needed:
  - `$ poetry add <dependency>`
- Create a virtual environment and install dependencies:
  - `$ poetry update`
- Run tests:
  - `$ poetry run pytest`
- Run linters:
  - `poetry run black <project>_<submodule> -l 79`
  - `poetry run flake8 <project>_<submodule> --ignore=E203,W503,W504`
- Update CHANGELOG.md with changes
- Sync version in `pyproject.toml` with `CHANGELOG.md`
  - `$ poetry run python scripts/py/update_version.py` 
- Publish to GCP Artifact Registry:
  - `$ poetry publish --build --repository pypi-gcp`
