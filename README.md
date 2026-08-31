# BallsDex CF-Commands Package

A package for **BallsDex** that adds commands from CarFigures.

## Commands

| Command | Description |
|---|---|
| `/balls inspect` | View the info of a countryball without owning the countryball |

## Installation

### 1 — Configure extra.toml

**If the file doesn't exist:** Create a new file `extra.toml` in your `config` folder under the BallsDex directory.

**If you already have other packages installed:** Simply add the following configuration to your existing `extra.toml` file. Each package is defined by a `[[ballsdex.packages]]` section, so you can have multiple packages installed.

Add the following configuration:

```toml
[[ballsdex.packages]]
location = "git+https://github.com/hiboman/BallsDex-CFCommands-Pack.git@0.0.1#master"
path = "cfcommands"
enabled = true
```

**Example of multiple packages:**

```toml
# First package
[[ballsdex.packages]]
location = "git+https://github.com/example/other-package.git"
path = "other"
enabled = true

# CFCommands Package
[[ballsdex.packages]]
location = "git+https://github.com/hiboman/BallsDex-CFCommands-Pack.git@0.0.1#master"
path = "cfcommands"
enabled = true
```

### 2 — Rebuild and start the bot

`docker compose up -d --build`

This will install the package and start the bot.
