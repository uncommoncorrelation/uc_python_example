# UC Example Python Project

Uses venv and piptools. Contains basic setup.py and gitignore config. CLI explainer at
explainer.md.

## Whys and Wherefores
This approach gives greater fidelity of control and visibility over virtual
environments than UC's current system.

Venv is now the Python foundation's recommended virtual environment management
tool, surpassing virtualenv. As such, we should use it now:
- to align with the Foundation's future development of the Python ecosystem;
- avoid a rush to move away from virtualenv if it becomes deprecated.

Venv has a nice API, which allows flexibility:
- venv directory is user specified; 
- venv prompt name is user specified.

This allows us to keep the venv directories within our project directories,
meaning that we have:
- filesystem canonicalization;
- avoidence of namespace clashing and the requirement for hashed directory
  names;
- easy visibility over virtual environments' state to aid assertion of
  deterministic builds.

Jazzband's pip-tools has a nice API which allows:
- hashing of dependencies;
- generation of layered, named, environments for projects;
- canonicalization of dependencies in setup.py;
- management of dependencies in the venv.


