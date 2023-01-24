from __future__ import print_function

import os.path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://mail.google.com/"]


def credential():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


# def main():
#     """Shows basic usage of the Gmail API.
#     Lists the user's Gmail labels.
#     """
#     # creds = None
#     # # The file token.json stores the user's access and refresh tokens, and is
#     # # created automatically when the authorization flow completes for the first
#     # # time.
#     # if os.path.exists("token.json"):
#     #     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#     # # If there are no (valid) credentials available, let the user log in.
#     # if not creds or not creds.valid:
#     #     if creds and creds.expired and creds.refresh_token:
#     #         creds.refresh(Request())
#     #     else:
#     #         flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
#     #         creds = flow.run_local_server(port=0)
#     #     # Save the credentials for the next run
#     #     with open("token.json", "w") as token:
#     #         token.write(creds.to_json())
#     creds = credential()

#     try:
#         # Call the Gmail API
#         service = build("gmail", "v1", credentials=creds)
#         results = service.users().labels().list(userId="me").execute()
#         labels = results.get("labels", [])

#         if not labels:
#             print("No labels found.")
#             return
#         print("Labels:")
#         for label in labels:
#             print(label["name"])

#     except HttpError as error:
#         # TODO(developer) - Handle errors from gmail API.
#         print(f"An error occurred: {error}")


# if __name__ == "__main__":
#     main()


def gmail_send_message():
    email_to = "tsg03232@naver.com"
    email_from = "alex.jiuk.kim@gmail.com"
    email_subject = "Automated draft"
    email_content = "This is automated draft mail"
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # creds, _ = google.auth.default()
    creds = credential()

    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(email_content)

        message["To"] = email_to
        message["From"] = email_from
        message["Subject"] = email_subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
    return send_message


if __name__ == "__main__":
    gmail_send_message()
