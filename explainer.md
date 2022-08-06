# UC Python Library Packaging


Prepare the project directory.
```bash
mkdir uc_python_example

cd uc_python_example
```

Create the new venv inside the project directory, and activate it.

```bash
python3 -m venv /venv --prompt uc_python_example

source venv/bin/activate
```

Why inside the directory? Ease of access, visibility.


Now create the src directory, and a simple setup.py, which defines the dependencies for our project in production and dev states.

```bash
mkdir src

echo -e '\nfrom setuptools import setup, find_packages\nimport pathlib\n\nhere = pathlib.Path(__file__).parent.resolve()\nsetup(\n    name="uc_python_example",\n    packages=find_packages(where="src"),  # Required\n    python_requires=">=3.7, <4",\n    install_requires=["pydantic"],\n    extras_require={  # Optional\n        "dev": ["pip-tools", "hypothesis[cli]", "mypy", "flake8", "pre-commit"]\n    },\n    package_dir={"": "src"},\n)' >> setup.py
```

This gives us canonicalization of dependencies for all environments. Les schap of manually named dependencies falling out of step with the ones pip sees.


Now we have a logical problem: pip-tools is installed inside a venv, not globally.

So before we can use pip-tools to manage the venv's dependencies, we must manually inject pip-tools into the running venv.

```bash
pip3 install pip-tools
```

Now we can compile, with hashes, the environments' respective requirements.

```bash
pip-compile --generate-hashes -o prod-requirements.txt

pip-compile --generate-hashes --extra dev -o dev-requirements.txt
```

We provide a manual name override to keep things explicit.

At this point, we can provision our 'layered' venv environment with our dependencies:

```bash
pip-sync dev-requirements.txt prod-requirements.txt
```
