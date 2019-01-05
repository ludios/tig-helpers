#!/usr/bin/env python3

from distutils.core import setup

setup(
	name="tig-helpers",
	version="2.0.0",
	description="tig helper to open links and issues in a commit message",
	scripts=["open-commit", "open-issues-for-repo", "open-links-in-commit-message"],
	py_modules=["tig_helpers"],
)
