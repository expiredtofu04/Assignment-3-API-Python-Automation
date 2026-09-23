import requests

from framework.logger import get_logger


logger = get_logger(__name__)


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint

        try:
            logger.info("GET Request: %s", url)

            response = requests.get(
                url,
                params=params,
                timeout=30
            )

            logger.info("GET Response Status: %s", response.status_code)

            return response

        except requests.exceptions.RequestException as e:
            logger.error("GET request failed: %s", e)
            raise

    def post(self, endpoint, data=None):
        url = self.base_url + endpoint

        try:
            logger.info("POST Request: %s", url)

            response = requests.post(
                url,
                data=data,
                timeout=30
            )

            logger.info("POST Response Status: %s", response.status_code)

            return response

        except requests.exceptions.RequestException as e:
            logger.error("POST request failed: %s", e)
            raise

    def put(self, endpoint, data=None):
        url = self.base_url + endpoint

        try:
            logger.info("PUT Request: %s", url)

            response = requests.put(
                url,
                data=data,
                timeout=30
            )

            logger.info("PUT Response Status: %s", response.status_code)

            return response

        except requests.exceptions.RequestException as e:
            logger.error("PUT request failed: %s", e)
            raise

    def delete(self, endpoint, data=None):
        url = self.base_url + endpoint

        try:
            logger.info("DELETE Request: %s", url)

            response = requests.delete(
                url,
                data=data,
                timeout=30
            )

            logger.info("DELETE Response Status: %s", response.status_code)

            return response

        except requests.exceptions.RequestException as e:
            logger.error("DELETE request failed: %s", e)
            raise