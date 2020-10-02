from user_manager.repos import user_repo

get_user = user_repo.get
filter_users = user_repo.filter_
update_user = user_repo.update
create_user = user_repo.get_or_create
