# pet schemas
# --------

pet = {
    "type": "object",
    "required": ["name", "type"],
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "integer"
        },
        "type": {
            "type": "string",
            "enum": ["cat", "dog", "fish"]
        },
        "status": {
            "type": "string",
            "enum": ["available", "sold", "pending"]
        },
    }
}

# 2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
# Order schemas
# -------------------
order = {
    "type": "object",
    "required": ["id", "pet_id", "status"],
    "properties": {
        "id": {"type": "string"},        # UUID
        "pet_id": {"type": "integer"},
        "status": {"type": "string", "enum": ["available", "pending", "sold"]}
    }
}

patch_order_response = {
    "type": "object",
    "required": ["message"],
    "properties": {
        "message": {"type": "string"}
    }
}
