# v0.0
20170120: Instant gameplay available on PUT route

# To run locally, with debugging
    $ export FLASK_DEBUG=1
    $ python cf-rps.py

# To demonstrate the APIs
## [GET] Show the homepage
Browse to [http://localhost:8088/](http://localhost:8088/)

## [PUT] Instant gameplay
    $ curl -X PUT http://localhost:8088/games/rock
    {
    "game_id": null,
    "match_id": null,
    "plays": {
        "computer": "rock",
        "person": "rock"
    },
    "status": "Tie game!",
    "validPlays": [
        "rock",
        "paper",
        "scissors"
    ]
    }

# Some references
* [PCF Dev](http://pivotal.io/pcf-dev)
* [Flask documentation](http://flask.pocoo.org/docs/latest/)
* [Jinja2 Documentation](http://jinja.pocoo.org/docs)
* [RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
