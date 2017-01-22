"""Define object class for rock, paper, scissors game"""
import json, random

class rpsGame( object ):
    """Provide data structure and methods for rock, paper, scissors game."""
    def __init__( self, match_id=None, game_id=None,
                  player1='PERSON', player2='COMPUTER', play1='', play2='' ):
        # Seems like we should validate the input.
        self.match_id = match_id
        self.game_id = game_id
        self.validPlays = ['rock','paper','scissors']
        if player2 == 'COMPUTER':
            play2 = random.choice(self.validPlays)
        inputPlays = [player1,play1,player2,play2]
        try:
            [player1,play1,player2,play2] = list(map(lambda x: x.strip().lower(), [player1,play1,player2,play2]))
        except:
            # There was some problem with the input
            # TODO: Re-use all the good input
            [player1,play1,player2,play2] = ('1','','2','')
        self.plays = {player1:play1, player2:play2}
        self.status = '' # Narrative about current status of this game
        try:
            self.status = self.play()
        except:
            self.status = 'Some gameplay data are missing or invalid.'
        dictGameInfo = {'match_id':self.match_id,
                        'game_id' :self.game_id}
        dictGameInfo.update(self.plays)
        self.log('Instantiated game with: '+str(dictGameInfo))
        return

    def play( self ):
        """Attempt to play game with current data; Return text for .status"""
        # Valid data looks like ...
        # * len(self.plays) == 2
        # * Each value in self.plays.values() is in self.validPlays
        result = ''
        # It should be impossible to create a rpsGame without 2 plays
        # But as it is .plays could be modified, so we should make sure
        readyToPlay = len(self.plays) == 2
        thesePlayers = []
        for thisPlayer in self.plays:
            thesePlayers.append(str(thisPlayer))
            if thisPlayer == 'computer':
                self.plays[thisPlayer] = random.choice(self.validPlays)
            if self.plays[thisPlayer] not in self.validPlays:
                self.plays[thisPlayer] = ''
                readyToPlay = False
                self.log('Reset invalid play for '+str(thisPlayer))

        if self.plays[thesePlayers[0]] == self.plays[thesePlayers[1]]:
            result = 'Tie game!'
        elif self.plays[thesePlayers[0]] == 'rock' and self.plays[thesePlayers[1]] == 'scissors' or \
             self.plays[thesePlayers[0]] == 'paper' and self.plays[thesePlayers[1]] == 'rock' or \
             self.plays[thesePlayers[0]] == 'scissors' and self.plays[thesePlayers[1]] == 'paper' :
            result = self.plays[thesePlayers[0]] + ' beats ' + self.plays[thesePlayers[1]] + ': ' + thesePlayers[0] + ' wins!'
        else:
            result = self.plays[thesePlayers[1]] + ' beats ' + self.plays[thesePlayers[0]] + ': ' + thesePlayers[1] + ' wins!'
        return result

    def log( self, logText=None ):
        """Log a message as requested."""
        # TODO: Accept more parameters, like msg, data, src, pri

        # https://www.balabit.com/documents/syslog-ng-ose-latest-guides/en/syslog-ng-ose-guide-admin/html/concepts-message-ietfsyslog.html
        if logText is not None:
            # How do we log from here out to the Flask app.logger ?
            pass

        return

    def toJSON( self ):
        """Return JSON string representing object's values."""
        # http://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
        result = json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
        return result
    def __repr__( self ):
        return self.toJSON()
    def __enter__( self ):
        return self
    def __exit__( self, exc_type, exc_value, traceback ):
        # Close files, sync to DB, whatever
        pass
