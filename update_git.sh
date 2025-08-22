#!/bin/bash
# script should be placed in with the source files
# Check for changes
if [[ -n $(git status --porcelain) ]]; then
    # Stage all changes
    git add .

    # Commit changes with a message
    read -p "Enter commit message: " commit_message
    git commit -m "$commit_message"

    # Push changes to the remote repository
    git push origin main  # Change 'main' to your branch name if necessary

    echo "Changes have been pushed to GitHub."
else
    echo "No changes to commit."
fi
