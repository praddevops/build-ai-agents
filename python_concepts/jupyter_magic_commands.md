# Jupyter notebooks - Magic commands 

`!` means the command will be run on the underlying instance's default terminal
`%` means the command will be run in the current Jupyter kernel environment
`%%` means the command will be run as a cell magic, affecting the entire cell
`%timeit` measures the execution time of a statement or expression
`%%timeit` measures the execution time of the entire cell
`%matplotlib inline` displays plots directly below cells
`%load_ext` loads a Jupyter extension for additional functionality
`%lsmagic` shows a list of all available magic commands
`%history -n` displays the last n commands with their line numbers
`%store` saves variables to be retrieved later with `%recall` or loaded in future sessions
`%recall` retrieves and displays previously stored variables from the `%store` command
`%load` and `%run` load and execute external Python scripts, respectively
`%who` displays all variables in the current namespace
`%pinfo` shows detailed information about an object
`%precision` sets the number of digits displayed for floating-point output
`%%time` measures the execution time of a code block
`%quickref` provides a quick reference of common magic commands and their descriptions
`%env` displays a list of all environment variables
`%debug` activates the interactive debugger for error analysis
`%%writefile filename` writes the contents of the cell to the specified file (overwrites by default); use `-a` to append instead of overwriting. Example: `%%writefile script.py` followed by the cell body saves it to script.py. 
