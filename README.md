# mergify
An easy way for non-technical stakeholders to join two tables via a selected column

## Setting up a dev environment

1. Make sure you have TK support in your python. On mac, you could run `brew install python-tk`.
2. Initiate a venv with `python3 -m venv venv`, activate it (`source venv/bin/activate`) and install dependencies (`pip install -r requirements.txt`).
3. Run the app with `python app.py`.


## Building

1. Create or update setup file: `py2applet --make-setup MyApplication.py`
2. Clear temporary dirs: `rm -rf build dist`
3. Build: `python setup.py py2app`


## Tech stack

- pandas for handling the data
- Tkinter for the gui
- py2app for packaging
