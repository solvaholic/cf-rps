# cf-rps
Rock, Paper, Scissors game to demonstrate Cloud Foundry development concepts and service integrations

# Before you 'cf push' to the cloud...
## Remove the /kill/ route
cf-rps.py defines a route '/kill/' that's handy while you're testing locally but unduly reckless on hosted Cloud Foundry.  Remove it or comment it out or something before you 'cf push'.

# v0.0
20170118: Python Flask app with route (stubs) to retrieve, create, and play RPS games
