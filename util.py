import subprocess

def get_site(origin_url):
	if origin_url.startswith(b"https://github.com/"):
		return "github.com"
	elif origin_url.startswith(b"git@github.com:"):
		return "github.com"
	elif origin_url.startswith(b"git://kernel.ubuntu.com/"):
		return "kernel.ubuntu.com"
	elif origin_url.startswith(b"https://anonscm.debian.org/git/"):
		return "anonscm.debian.org"

def get_github_user_and_repo(origin_url):
	if origin_url.startswith(b"https://github.com/"):
		_, _, _, user, repo = origin_url.split(b"/")
	elif origin_url.startswith(b"git@github.com:"):
		_, user_repo = origin_url.split(b":", 1)
		user, repo   = user_repo.split(b"/", 1)
	else:
		raise ValueError("remote.origin.url did not start with https://github.com/ or git@github.com:")
	if repo.endswith(b".git"):
		repo = repo[:-4]
	return user, repo

assert get_github_user_and_repo(b"https://github.com/user/repo")     == (b"user", b"repo")
assert get_github_user_and_repo(b"https://github.com/user/repo.git") == (b"user", b"repo")
assert get_github_user_and_repo(b"git@github.com:user/repo")         == (b"user", b"repo")
assert get_github_user_and_repo(b"git@github.com:user/repo.git")     == (b"user", b"repo")

def get_origin_url():
	"""
	Returns remote.origin.url for the git repo in the current directory.
	"""
	# Why not git ls-remote?  Because it won't work in a detached HEAD state.
	# See https://goo.gl/yc3QOe
	return subprocess.check_output([b"git", b"config", b"--get", b"remote.origin.url"]).rstrip()
