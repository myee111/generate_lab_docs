# Introduction

I got [instructlab](https://github.com/instructlab/instructlab/blob/main/README.md) to write most of this program for me. `generate_lab_docs` will create a single markdown file containing all the instructions in an `Instruqt` lab.

# Installation

## Clone this repo.
```
git clone https://github.com/myee111/generate_lab_docs.git
```

## Create a venv in fish.
```
. venv/bin/activate.fish
```

## Install requirements.
```
pip install -r requirements.txt
```

# Usage

To run the program, enter the following command.

```
python main.py --work-dir '/Users/myee/repos/instruqt/satellite-advanced-topics'
```
