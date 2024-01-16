import os

import click
import requests


def send_data(text, api_key):
    url = "https://jrvs-n73oe.ondigitalocean.app/oping"
    headers = {"Authorization": api_key}
    resp = requests.post(url, data=text, headers=headers)
    return resp


@click.command()
def main():
    """A simple connectivity check with the OpenAI API"""

    # Read API key from environment variable
    api_key = os.environ.get("API_SECRET")
    if not api_key:
        click.echo("API_SECRET environment variable is not set.")
        return
    input_text = click.get_text_stream("stdin").read()
    if not input_text:
        click.echo("No input received!")
        click.echo("Usage: echo world | oping")
        return
    resp = send_data(input_text, api_key)
    print(resp.text)


if __name__ == "__main__":
    main()
