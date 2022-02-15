"""Arquivo com métodos de verificação de usuário.

"""
from werkzeug.security import check_password_hash


def verify_password(password_db, password_login):
    """Verifica se a senha que o usuário tentou fazer login é igual a senha cadastrada.

    :param password_db: senha salva no database
    :param password_login: senha que o usuário inseriu para fazer login
    :return: Boolean
    """
    return check_password_hash(password_db, password_login)


def verify_emails_equals(email_db, user):
    """Verifica se o email que o usuário tentou fazer login é igual ao email cadastrada.

    :param email_db: email salvo no database
    :param user: email que o usuário inseriu para fazer login
    :return: Boolean
    """
    if verify_user_exists(user):
        return email_db is user.email
    return False


def verify_user_exists(user):
    """Verifica se o retorno da recuperação de usuário no database é None.

    :param user: retorno de usuário do database.
    :return: Boolean
    """
    return user is None
