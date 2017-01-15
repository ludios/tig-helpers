# tig-open-links-in-commit-message

[![Build status][travis-image]][travis-url]

[tig](https://github.com/jonas/tig) is a great interface for reading git commits,
but too often there are GitHub issues or URLs mentioned in a commit message that
are tedious to open in a browser.  `tig-open-links-in-commit-message` provides
an easy way to open all GitHub issues and URLs mentioned in a commit.


## Installation

```
git clone https://github.com/ludios/tig-open-links-in-commit-message
```

Add to `~/.config/tig/config` or `~/.tigrc`:

```
bind generic   x   @/PATH/TO/tig-open-links-in-commit-message/open-links-in-commit-message %(commit)
```


## Usage

Move to whichever commit you're interested in and press the `x` key (or whichever key was set in the tig config).

If it doesn't seem to be working, replace `@` with `!` in the tig config to see output from the script.


[travis-image]: https://img.shields.io/travis/ludios/tig-open-links-in-commit-message.svg
[travis-url]: https://travis-ci.org/ludios/tig-open-links-in-commit-message
