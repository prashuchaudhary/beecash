from invoke import task, run


@task(aliases=["s"])
def shell(ctx):
    """
    Runs Pipenv Shell
    :return:
    """
    run("pipenv shell", pty=True)


@task(aliases=["i"])
def install(ctx):
    """
    Runs Pipenv Install
    :return:
    """
    run("pipenv install -d", pty=True)


@task(aliases=["l"])
def lock(ctx):
    """
    Generate Pipenv Lock File
    :return:
    """
    run("pipenv lock", pty=True)


@task(aliases=["req"])
def requirements(ctx):
    """
    Generate requirements.txt
    :return:
    """
    run("touch requirements.txt && pipenv run pip freeze > requirements.txt", pty=True)
