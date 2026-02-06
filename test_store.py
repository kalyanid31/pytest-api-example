from jsonschema import validate
import pytest
import api_helpers
from hamcrest import assert_that, contains_string, is_
from schemas import patch_order_response

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''


# 2) *Optional* Consider using @pytest.fixture to create unique test data for each run
@pytest.fixture
def create_order():
    payload = {"pet_id": 0}  # Ensure pet 0 exists and is available
    response = api_helpers.post_api_data("/store/order", payload)
    assert response.status_code == 201
    return response.json()["id"]


# 1.Creating a function to test the PATCH request /store/order/{order_id}
def test_patch_order_by_id(create_order):
    payload = {"status": "sold"}

    response = api_helpers.patch_api_data(
        f"/store/order/{create_order}",
        payload
    )

    # 3 & 4. Validate response code and message
    assert_that(response.status_code, is_(200))
    assert_that(response.json()["message"], is_("Order and pet status updated successfully"))

    # Validate response schema
    validate(instance=response.json(), schema=patch_order_response)
