"""
Test Settings File
"""

ES_HOST = "http://localhost:9200"
ES_ENV = "development"
ES_INDICES = {
    "User": {
        "name": "users",
        "doc_type": "user",
        "data_functions": {
            "single": "tests.data:get_user",
            "multi": "tests.data:list_users"
        },
        "mapping_path": "tests/user_mapping.json"
    }
}
