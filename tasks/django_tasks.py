from invoke import task, run


@task(aliases=["sh"])
def shell(ctx):
    """
    Runs django's interactive shell
    :return:
    """
    run("./manage.py shell_plus", pty=True)


@task(aliases=["mg"])
def migrate(ctx):
    """
    Runs the migrations
    :return:
    """
    run("./manage.py migrate", pty=True)


@task(aliases=["mm"])
def make_migrations(ctx, app_name):
    """
    Runs the make migrations
    :return:
    """
    run("./manage.py makemigrations {}".format(app_name), pty=True)


@task(pre=[migrate], aliases=["rs"])
def runserver(ctx):
    """
    Runs the local server
    :return:
    """
    run("./manage.py runserver", pty=True)


@task(aliases=["cs"])
def collect_static(ctx):
    run("./manage.py collectstatic --noinput")
