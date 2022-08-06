
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
setup(
    name="uc_python_example",
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    install_requires=["pydantic"],
    extras_require={  # Optional
        "dev": ["pip-tools", "hypothesis[cli]", "mypy", "flake8", "pre-commit"]
    },
    package_dir={"": "src"},
)
