# Clean Notebook

A simple utility to strip the outputs from a Jupyter Notebook, to minimise the
deltas when using GIT.

## Installation

From the project directory:

    pip install -e .

This creates an entry point on the command line.


## Usage

In the console type:

    cnb path/to/notebook.ipynb

By default, a backup is also created:  `original_name.bak.ipynb`.

This is just a rename of the original file, so everything is retained. The
clean notebook uses the original filename.

The backup can be disabled with the `-n` flag.

    cnb -n path/to/notebook.ipynb

Type `cnb -h` to get help.

