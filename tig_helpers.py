import subprocess

def get_site(origin_url):
	if origin_url.startswith("https://github.com/"):
		return "github.com"
	elif origin_url.startswith("git@github.com:"):
		return "github.com"
	elif origin_url.startswith("git://kernel.ubuntu.com/"):
		return "kernel.ubuntu.com"
	elif origin_url.startswith("https://anonscm.debian.org/git/"):
		return "anonscm.debian.org"
	elif origin_url.startswith("https://chromium.googlesource.com/"):
		return "chromium.googlesource.com"

def get_github_user_and_repo(origin_url):
	if origin_url.startswith("https://github.com/"):
		_, _, _, user, repo = origin_url.split("/")
	elif origin_url.startswith("git@github.com:"):
		_, user_repo = origin_url.split(":", 1)
		user, repo   = user_repo.split("/", 1)
	else:
		raise ValueError("remote.origin.url did not start with https://github.com/ or git@github.com:")
	if repo.endswith(".git"):
		repo = repo[:-4]
	return user, repo

assert get_github_user_and_repo("https://github.com/user/repo")     == ("user", "repo")
assert get_github_user_and_repo("https://github.com/user/repo.git") == ("user", "repo")
assert get_github_user_and_repo("git@github.com:user/repo")         == ("user", "repo")
assert get_github_user_and_repo("git@github.com:user/repo.git")     == ("user", "repo")

def get_origin_url():
	"""
	Returns remote.origin.url for the git repo in the current directory.
	"""
	# Why not git ls-remote?  Because it won't work in a detached HEAD state.
	# See https://goo.gl/yc3QOe
	return subprocess.check_output(["git", "config", "--get", "remote.origin.url"]).decode("utf-8").rstrip()
