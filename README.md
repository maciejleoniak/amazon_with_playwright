

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip install -r requirements.txt`

before commit:

`pre-commit run --all-files`


`pytest . -s -v --html=reports/report.html --self-contained-html`