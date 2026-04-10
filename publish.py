import subprocess

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        raise SystemExit(1)
    if result.stdout.strip():
        print(result.stdout.strip())

run(["git", "add", "."])
run(["git", "commit", "-m", "Add Flask app, CSV analysis, and publish script"])
run(["git", "push", "origin", "main"])

print("Published to https://github.com/zdmoor7/python_course")
