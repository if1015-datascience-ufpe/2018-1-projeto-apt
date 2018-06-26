from nbformat import v3, v4

script_name = 'dengue'

with open(f'{script_name}.py') as script_file:
    script = script_file.read()

notebook = v4.writes(v4.upgrade(v3.reads_py(script))) + '\n'

with open(f'{script_name}.ipynb', 'w') as notebook_file:
    notebook_file.write(notebook)