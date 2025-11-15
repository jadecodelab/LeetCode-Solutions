# You are given an absolute path for a Unix-style file system,
# transform this absolute path into its simplified canonical path.
# - The path must start with a single slash '/'.
# - Directories within the path must be separated by exactly one slash '/'.
# - The path must not end with a slash '/', unless it is the root directory.
# - The path must not have any single or double periods ('.' and '..')
    # used to denote current or parent directories.


def simplifyPath(path:str)->str:
    stack = []  # Initialize a stack

    # Split the path on "/" as the delimiter
    for portion in path.split("/"):
        # If the portion is a ".." and the stack is not empty,
        # remove it from the stack
        if portion == "..":
            if stack:
                stack.pop()
        # If portion is a "." or an empty string, just ignore it
        elif portion == "." or portion == "":
            continue
        # else add the portion to the stack
        else:
            stack.append(portion)

    # connect all the portion with the "/" to get the simplify path
    simplify_path = "/" + "/".join(stack)
    return simplify_path


print(simplifyPath( "/.../a/../b/c/../d/./"))
    
                
