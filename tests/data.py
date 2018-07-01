"""
Test data will fetched from here.
"""
USERS = [
    {
        "id": 1,
        "name": "Tony Stark",
        "email": "tony.stark@starkenterprises.org"
    },
    {
        "id": 2,
        "name": "Steve Rogers",
        "email": "steve.rogers@shield.com"
    }
]


def get_user(user_id: int):
    """Retrieves user data with the id requested.
    Arguments:
        user_id {int} -- The User ID
    Returns:
        [dict] -- The User data
    """

    for user in USERS:
        if user["id"] == user_id:
            return user
    return None


def list_users(limit: int = 10, offset: int = 0):
    """Returns list of users
    Keyword Arguments:
        limit {int} -- Total number sample size (default: {10})
        offset {int} -- Offset in list (default: {0})
    """
    return USERS[offset:offset+limit]
