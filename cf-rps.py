"""Cloud Foundry Rock, Paper, Scissors"""
from flask import Flask, render_template, jsonify
import cf_deployment_tracker
import os

# Emit deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

# Get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8088
port = int(os.getenv('PORT', 8088))

# Check out the Flask and Jinja2 documentation :
#   http://flask.pocoo.org/docs/0.12/quickstart
#   http://jinja.pocoo.org/docs
# Also this is very instructive :
#   https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

'''
    GET    '/[index/]'           Show the homepage
    GET    '/matches/[<string>]' Retrieve a match, or all matches
    GET    '/games/[<string>]'   Retrieve a game, or all games
    POST   '/matches/'           Create a new match
    POST   '/games/[<string>]'   Create a new game
    PUT    '/games/[<string>]'   Submit a play to a new or existing game
'''

@app.route('/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def show_index():
    """Show the cf-RPS homepage."""
    # Provide info, link to different gameplay modes
    # fyi, fwiw, here's an example of passing values to render_template() :
    #   return render_template('index.html', name='<someone>')
    return render_template('index.html')

@app.route('/matches/', methods=['GET'])
@app.route('/matches/<string:match_id>', methods=['GET'])
@app.route('/matches/game_id/<string:game_id>', methods=['GET'])
def get_matches(match_id="GET",game_id="GET"):
    """Retrieve a match or all matches. Return match details and status."""
    # If no match_id or game_id then return info for all matches
    # If match_id then return info for that match
    # If game_id then return info for the match that game is part of
    result = '{"game_id":"'+str(game_id)+'","match_id":"'+str(match_id)+'"}'
    return result

@app.route('/matches/', methods=['POST'])
def post_matches():
    """Create a match. Return match details and status."""
    # If match_id or game_id then something is wrong
    # If no match_id or game_id then create a match
    result = '{"match_id":"POST"}'
    return result

@app.route('/games/', methods=['GET'])
@app.route('/games/<string:game_id>', methods=['GET'])
@app.route('/games/match_id/<string:match_id>', methods=['GET'])
def get_games(game_id='GET',match_id='GET'):
    """Retrieve a game or all games. Return game details and status."""
    # If no match_id or game_id then return info for all games
    # If game_id then return info for that game
    # If match_id then return info for all games in that match
    result = '{"game_id":"'+str(game_id)+'", "match_id":"'+str(match_id)+'"}'
    return result

@app.route('/games/', methods=['POST'])
@app.route('/games/match_id/<string:match_id>', methods=['POST'])
def post_games(match_id='POST'):
    """Create a game. Return game details and status."""
    # If game_id then something is wrong
    # If match_id then create a new game in that match
    # If no match_id then create a new game with no match
    result = '{"game_id":"POST", "match_id":"'+str(match_id)+'"}'
    return result

@app.route('/games/', methods=['PUT'])
@app.route('/games/<string:my_play>', methods=['PUT'])
@app.route('/games/game_id/<string:game_id>/<string:my_play>', methods=['PUT'])
def play_game(my_play='PUT',game_id='PUT'):
    """Submit a play to a game. Return results of the game."""
    # If no my_play then something is wrong
    # If no game_id and no match_id then create a new game and play it
    # If game_id then play that game
    # If match_id and no game_id then .. idk .. tea?
    result = getfromreq()
    return result

def getfromreq(myreq=None):
    """Get useful fields from request data."""
    result = jsonify({"game_id":"---",
               "match_id":"---",
               "yourplay":"---",
               "npc_play":"---",
               "result":"---"})
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
