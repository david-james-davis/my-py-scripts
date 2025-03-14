# Getting started

Install dependencies:

`poetry install`

## Task Runners

### Lint your code
`poetry run poe lint`

### Fix linting issues
`poetry run poe lintfix`

### Format your code
`poetry run poe format`

### Check everything before commiting
`poetry run poe check`

(See poe tool setup in pyproject.toml)


## Running scripts

ADSB Exchange aircraft flights over tcp: `poetry run python scripts/ADSBexchange.py`