from github import Github, InputFileContent
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import time

"""
Script query all Github repositories of the account once a day, 
compares “uniques” (unique views) and reports if any difference 
between current and previous day views. 
"""

TOKEN = "github_access_token"
git = Github(TOKEN)
my_user = git.get_user("github user name")


def main():

    previous_day_views = {}
    current_day_views = {}
    print("Test1")

    while True:

        current_day_views = get_repo_views(my_user)
        repo = []
        if len(diff_in_views(current_day_views, previous_day_views)) != 0:
            for i in diff_in_views(current_day_views, previous_day_views):
                repo.append(i)

            text = "\n\n".join([str(i) for i in repo])
            send_email("Github Repo Report", text)

        time.sleep(86400)


def get_repo_views(user):
    views = {}
    for repo in my_user.get_repos():

        views[repo.name] = {}

        for k, v in repo.get_views_traffic(per="day").items():
            if k == "count" or k == "uniques":
                views[repo.name][k] = v
    return views


def diff_in_views(dict1, dict2):
    try:
        diff = list()
        for k, v in dict1.items():
            # if dict1[k] != dict2[k]:
            if dict1[k]["uniques"] != dict2[k]["uniques"]:
                diff.append(f"{k}: Today: {dict1[k]} Yesterday: {dict2[k]}")
        return diff
    except:
        return {}


def send_email(subject_text, report_text):
    """ Send email via email realay. Takes two string arguments:
    subject_text will pressent suject line of email
    report_text will pressent body of the email. 
    """
    fromaddr = "sender@domain.com"
    toaddr = "recipient@domain.com"
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = str(subject_text)
    body = str(report_text)
    msg.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP("relay.domain.com", 25)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr.split(","), text)


def update_previous_day_views():
    previous_day_views = current_day_views
    return previous_day_views


if __name__ == "__main__":
    print()
    main()
    print()
