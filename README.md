Discord bots
============

A collection of helpful bots for use in a Discord server.
So far the family consists of

* GitlabUpdater
*

## GitlabUpdater

A bot designed to copy qualifying comments from a Discord channel to an
issue in a particular Gitlab repository.

Unlike Github, Gitlab is not free for everyone. Gitlab is a better place
to record discussions than Discord but giving everyone who wants to
participate a Gitlab userid in your project repo may not be practical.
This bot allows everyone with a userid in your Discord server to add 
comments to issues in your project. It's not perfect but it encourages
greater participation.

### Usage

* Install the bot in your server and enroll the bot user in the channel
you want to copy comments from.
* Prefix comments you want to copy to Gitlab with the magic string
(default is '##') and the issue number, eg:
```
## 219 This is a good idea but we need to be careful with licensing 
restrictions. The original is CC-SA but blah blah blah. More blah. Even
a great big text wall. Once upon a time in a land far far away lived a
little goblin called Fred. Fred had a pet wombat. The wombat was very
vicious and the subject of multiple restraining orders. All of which he
ignored because he was a wombat and therefore had no concept of legal
niceties like restraining orders. Blah blah blah.
```
* The bot will see the message and attempt to update the specified issue
and report the result in a person-friendly way.
* The bot does not see edited messages so you can't edit a comment to
include the issue number after it's been posted. You would need to copy
and paste the message again, remembering to prefix it with the magic
string and the issue number.

#### Installation
Discord: TODO

Gitlab: TODO

#### Configuration

Copy Bots.ini.sample to Bots.ini and customise for your installation.
There are 4 records in the GitlabUpdater section.
| key | value |
| ------------- | ----- |
| private_token | the private token you created in your Gitlab account |
| base_url | the base URL for the issues in your repository/project |
| bot_id | the bot ID you got from Discord |
| magic_string | the prefix the bot responds to |

#### Operation

Start the bot by
```
python3 GitlabUpdater.py
```
It will tell you once it has logged in to Discord and then sit there 
silently watching
for the activation magic string and copying comments to Gitlab. Any feedback
will appear in the Discord channel.

### Donate

    BTC: 3C1VgNZK1M9evqMQaDBUGVCk1EBZU5ND8Q
    CRW: CRWKcbKuYkT35s4MJMwo8zjTjVe76aCsKUjG

### MIT License

Copyright (c) 2019, Mark Brooker

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
