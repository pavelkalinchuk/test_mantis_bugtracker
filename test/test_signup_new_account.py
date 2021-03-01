from generator.user import name


def test_signup_new_account(app):
    username = name
    password = "test"
    email = username + "@localhost.domain"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()
