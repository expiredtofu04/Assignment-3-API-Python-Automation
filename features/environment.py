import logging

from framework.config_reader import get_config
from framework.api_client import APIClient
from framework.test_data import load_user_data


def before_all(context):

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    config = get_config()

    context.client = APIClient(
        config["base_url"]
    )

    context.user_data = load_user_data()


def after_all(context):
    pass