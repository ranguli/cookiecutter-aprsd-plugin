from nox_poetry import session


@session(python=["3.7", "3.8", "3.9"])
def test(session):
    session.run(
        "pytest",
        "-vvv",
        external=True,
    )

@session(python=["3.9"])
def lint(session):
    session.run("black", ".", external=True)
    session.run("flake8", "./" + {{cookiecutter.module_name}}, "./test", external=True)
    session.run("bandit", "-r", "./" + {{cookiecutter.module_name}}, external=True)
    session.run("mypy", "--warn-unreachable", "./" + {cookiecutter.module_name}}, external=True)
    session.run("pylint", "./" + {{cookiecutter.module_name}}, external=True)
    session.run("isort", ".", external=True)
