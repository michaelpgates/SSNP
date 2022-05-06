Slackbot Social Networking Project
PROSPECTUS:
Our cybersecurity cohort can greatly benefit by networking with one another but exchanging information and be cumbersome and time consuming.
The Slackbot Social Networking Project (SSNP) posits that individuals can submit their linkedin profile in the form of a command to slackbot.
Slackbot then will remit the profile to a readonly channel. This format will allow users to easily navigate the profiles of their fellow peers.
Connection requests can be easily sent out by users on their own volition.

Methodology:
A test channel will be formed where the slackbot API can be tinkered with.
proposed langauge - python
once the bot is functional the development team will reach out to the instructors with said proposal.
If the project is reviewed and accepted the project will be deployed.

Development notes:
Processes:
5/6/2022 slack workspace created, VScode installed, pip installed, python-dotenv installed, Python 3.10 in use
5/6/2022 - bot permissions created. if permissions are changed the app must be reinstalled. 
[source - https://youtu.be/KJ5bFv-IRFM?t=319]
5/6/2022 slackbot is hosted on a localserver using ngrok migration will be necessary
5/6/2022 slackbot permission changed to handle channel messages and direct messages. currently it is not sure if the messages
are localed to just the bot or all direct messages. app reinstalled via api.slack.com due to permission change

Errors:
5/6/2022 client = slack.WebClient(token=os.environ['SLACK_TOKEN']) should import the environmental variable but it doesn't.
preliminary solution - hardcode the token until the solution is found.
5/6/2022 posting this file to github with the token in plain text caused a security event. the slack auth token was destroyed.
preliminary solution - create a new token and find a way to import the token from a noncomitted environmental variable file.

Hurdles:
5/6/2022 in order to support event handling slackbot needs to be hosted. Soft research suggests using AWS LAMBDA (zappa flask lambda combo). resource material
provides a temporary solution of using local hosting. At this time local hosting will be used to keep project momentum.

Meta Notes:
slack freemium only allows posting permissions to be restricted on the #general channel. This may be a problem as the channel
created and controlled by the SSNP needs to be heavily moderated. preliminary solution - program the bot to delete all messages
not created by self.

//future lambda revision
if the server is moved to AWS lambda then marked tools and processes will be affected [removed]

Current resources:
https://www.youtube.com/watch?v=KJ5bFv-IRFM&list=PLzMcBGfZo4-kqyzTzJWCV6lyK-ZMYECDc

Tools:
slack api [api.slack.com]
windows terminal
Python 3.10
VScode
pip [using windows but on linux command is pip3]
slackclient [installed via terminal using command: pip install slackclient]
python-dotenv [installed via terminal using command: pip install python-dotenv]
flask [installed via terminal using command: pip install flask] //future lambda revision
slack events api [installed via terminal using command: pip install slackeventsapi] //future lambda revision
ngrok [installed via https://ngrok.com/download] //future lambda revision

