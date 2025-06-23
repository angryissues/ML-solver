from setuptools import setup, find_packages
from pathlib import Path

# читаем описание из README, если он есть
this_dir = Path(__file__).parent
long_desc = ""
if (this_dir / "README.md").exists():
    long_desc = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="my_solver_lib",           # как вы будете pip install my_solver_lib
    version="0.1.0",
    author="Ваше Имя",
    description="Библиотека задач и решений",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/angryissues/ML-solver",  # ваш репо
    # найдёт папку solver_lib как пакет
    packages=find_packages(include=["solver_lib", "solver_lib.*"]),
    include_package_data=True,      # чтоб брать файлы, указанные в MANIFEST.in
    install_requires=[
        # здесь ваши зависимости, если есть
    ],
    package_data={
        # указываем, что problems.json лежит рядом с кодом
        "solver_lib": ["data/problems.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
