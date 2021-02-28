from generator.user import username


def test_signup_new_account(app):
    user = username
    password = "test"
    app.james.ensure_user_exists(user, password)
