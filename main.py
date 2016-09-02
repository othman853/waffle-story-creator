import os
import requests


def main():
    endpoint = (
        'https://api.github.com/repos/othman853/casa-planner-android/issues'
    )
    oauth_token = os.environ['GITHUB_OAUTH_TOKEN']

    title = input("Story title: ")
    as_clause = input("As: ")
    i_want_clause = input("I Want: ")
    so_that_clause = input("So that: ")

    story_body_template = (
        "**As** {} \n"
        "**I want** {}\n"
        "**So that** {}"
    ).format(
        as_clause,
        i_want_clause,
        so_that_clause
    )

    print("Preparing headers...")

    request_headers = {
        "Authorization": "token {}".format(oauth_token)
    }

    print("Preparing request data...")
    request_body = {
        "title": title,
        "body": story_body_template
    }

    print("Sending...")
    response = requests.post(
        endpoint,
        headers=request_headers,
        json=request_body
    )
    print("Sent!")

    if response.status_code == 201:
        print('Story/Issue created')
    else:
        print(
            'There was an error when attempting to create the story/issue.'
            'See the response body below:'
        )
        print(response.text)


if __name__ == '__main__':
    main()
