import os
import sys
from github import Github

# List of prohibited words
PROHIBITED_WORDS = ['badword1', 'badword2', 'example']

# Authenticate with GitHub
g = Github(os.getenv('GITHUB_TOKEN'))

# Get the pull request event data
pr_number = int(os.getenv('PR_NUMBER'))
repo_name = os.getenv('GITHUB_REPOSITORY')
repo = g.get_repo(repo_name)

# Get the pull request details
pr = repo.get_pull(pr_number)

# Get the PR description and title
pr_title = pr.title
pr_body = pr.body

# Combine the title and body for word checking
pr_content = pr_title + ' ' + pr_body

# Check if prohibited words are present
for word in PROHIBITED_WORDS:
    if word.lower() in pr_content.lower():
        print(f"Prohibited word found: {word}")
        sys.exit(1)

print("No prohibited words found.")