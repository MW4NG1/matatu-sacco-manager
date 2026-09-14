from utils.auth import login_user, logout_user, get_current_user

def and_clear_auth():
    logout_user()

def test_login_and_current_user():
    logout_user()
    assert get_current_user() is None
    
    user = login_user("0712345678")
    if user:
        assert get_current_user() == user
    logout_user()
    assert get_current_user() is None