# tig-open-links-in-commit-message

[![Build status][travis-image]][travis-url]

[tig](https://github.com/jonas/tig) is a great interface for reading git commits, but too often
there are [GitHub issues or URLs mentioned in a commit message](http://i.imgur.com/69V9KwQ.png)
that are tedious to open in a browser.  The `open-links-in-commit-message` script here takes a
commit ID and opens in your browser all of the GitHub issues and URLs mentioned in that commit.
This is easy to integrate with tig, which can bind a key to run an executable.


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
