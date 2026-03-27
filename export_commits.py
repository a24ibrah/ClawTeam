import subprocess

# Path to your local clone of the repo
repo_path = "./jaraco_path_repo"

# Export to CSV
def export_commits_csv():
    csv_cmd = [
        "git", "log", "main",
        '--pretty=format:%H,%an,%ae,%ad,%s'
    ]
    with open("commits.csv", "w") as f:
        subprocess.run(csv_cmd, cwd=repo_path, stdout=f, check=True)

# Export to TXT
def export_commits_txt():
    txt_cmd = [
        "git", "log", "main",
        '--pretty=format:%H%n%an%n%ad%n%s%n%b%n---'
    ]
    with open("commits.txt", "w") as f:
        subprocess.run(txt_cmd, cwd=repo_path, stdout=f, check=True)

if __name__ == "__main__":
    export_commits_csv()
    export_commits_txt()
    print("Export complete: commits.csv and commits.txt generated.")
