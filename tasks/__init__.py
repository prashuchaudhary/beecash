from invoke import Collection
from tasks import pipenv_tasks
from tasks import django_tasks

ns = Collection()

ns.add_collection(pipenv_tasks, name="pip")

ns.add_task(django_tasks.shell)
ns.add_task(django_tasks.runserver)
ns.add_task(django_tasks.migrate)
ns.add_task(django_tasks.make_migrations)
ns.add_task(django_tasks.collect_static)
