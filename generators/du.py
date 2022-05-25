# Create a treemap json based on the file sizes within the given directory
#
# Example:
#
#   python generators/du.py ../drivers/bundle/ > examples/bundle.json

import pathlib
import json
import sys

root = pathlib.Path(sys.argv[-1])

def explore(path):
    if path.is_dir():
        children = []
        for sub in path.iterdir():
            children.append(explore(sub))
        return {
            "name": path.name,
            "children": children
        }
    else:
        return {
            "name": path.name,
            "value": path.stat(follow_symlinks=False).st_size
        }



tree = explore(root)
tree["name"] = str(root)

print(json.dumps(tree, indent=1))
