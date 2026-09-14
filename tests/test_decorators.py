from utils.decorators import require_auth, require_admin

def test_decorators_existence():
    assert callable(require_auth)
    assert callable(require_admin)