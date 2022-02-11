from werkzeug.security import check_password_hash


def verify_password(password_db, password_login):
    return check_password_hash(password_db, password_login)
