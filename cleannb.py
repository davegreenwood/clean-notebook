"""
Strip the output from a jupyter notebook.
A utility to shrink the deltas when versioning.
"""
import json
import shutil
import argparse


def readnb(fname):
    """ Return a dictionary read from a notebook. """
    with open(fname) as fid:
        data = json.load(fid)
    return data


def strip(d, fname):
    """Strip the output and set execution count to zero."""
    for cell in d.get("cells", []):
        cell["outputs"] = []
        cell["execution_count"] = 0
    with open(fname, "w") as fid:
        json.dump(d, fid, indent=1)


def main():
    """ Strip notebook for git."""
    parser = argparse.ArgumentParser(
        description="Strip the output of a Jupyter Notebook")
    parser.add_argument("fname",
                        type=str,
                        help="filename of jupyter notebook")
    parser.add_argument("-n", "--no-backup",
                        action="store_false",
                        dest="backup",
                        help=(
                            "Disable backup of the original file. "
                            "Default is make a backup. "
                            "If the flag is set, NO backup is made.")
                        )
    args = parser.parse_args()
    fname = args.fname
    d = readnb(fname)
    if args.backup:
        orig = fname.split(".")
        orig.insert(-1, ".bak.")
        bak = "".join(orig)
        shutil.move(fname, bak)
        print("Saved original file to:\n", bak)
    strip(d, fname)


if __name__ == "__main__":
    main()
