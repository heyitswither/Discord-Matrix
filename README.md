# Discord-Matrix
A bridge for Discord and Matrix

## Installation

```
git clone https://github.com/heyitswither/Discord-Matrix
cd Discord-Matrix
pip install -r requirements.txt
```

## Usage

Edit the `config.yml` file with your settings

Run normally

Example output:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Matrix client ready!
@unix-like-discord:matrix.org
Watching Unix-Like in matrix.org
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Discord client ready!
matrix is cool#2672
Watching #matrix-test in Wither Server
```

## Config

The following is an example confgiuration.

```
matrix:
    room_id: "!FOaRwvHYvwfEYKhuRX:matrix.org"
    username: discord-link
    password: just a password
    homeserver: https://matrix.org
discord:
    channel_id: 376493893736202240
    token: MzY5MTgwNDQyMzAzMzk3OTAx.DMUxsQ.SWa1yg_pum3J5pFiIOc1a2XmPm4
```

The room\_id must be the internal id (can be found in a room's settings menu, under advanced) and be in quotes.
