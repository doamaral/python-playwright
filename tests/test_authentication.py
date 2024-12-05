"""Authentication Scenarios"""
import os
from dotenv import load_dotenv

load_dotenv()


def test_authentication(before_each):
    """Test multiple possibilities of input for test authentication scenarios"""
    page = before_each
    page.goto(os.getenv("BASE_URL"))
    username_field = page.locator("username")
    password_field = page.get_by_role("input", name="password")

    username_field.fill("whatever")
    password_field.fill("whatever")
