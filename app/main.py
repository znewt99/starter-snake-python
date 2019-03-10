import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response
from math import sqrt

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#3366ff"
    headType = "pixel"
    tailType = "curled"

    return start_response(color,headType,tailType)


@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))

    directions = ['up', 'down', 'left', 'right']
    H = data['board']['height'] -1
    W = data['board']['width'] -1
    x = ['up', 'down']
    y = ['left', 'right']

    if data['turn'] == 0:
        direction = random.choice(directions)
    else:
        xh = data['you']['body'][0]['x']
        yh = data['you']['body'][0]['y']
        xb = data['you']['body'][1]['x']
        yb = data['you']['body'][1]['y']
        d = []
        for m in data['board']['food']:
            d.append(abs(m['x']-xh) + abs(m['y']-yh))
        f = data['board']['food'][d.index(min(d))]
        print f
        if abs(f['x']-xh) < abs(f['y']-yh):
            if f['x']-xh > 0:
                direction = 'right'
                if xb-xh > 0:
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    else:
                        direction = 'left'
                        if f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                elif yb-yh > 0:
                    direction = 'down'
                    if yh == H or yh == 0:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    else:
                        direction = 'up'
                        if f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                print 'x'
            elif f['x']-xh < 0:
                direction = 'left'
                if xb-xh < 0:
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    else:
                        direction = 'right'
                        if f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                elif yb-yh < 0:
                    direction = 'up'
                    if yh == 0 or yh == H:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    else:
                        direction = 'down'
                        if f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                print 'y'
            else:
                if xb-xh > 0:
                    direction = 'left'
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    elif f['y']-yh > 0:
                        direction = 'down'
                    elif f['y']-yh < 0:
                        direction = 'up'
                elif xb-xh < 0:
                    direction = 'right'
                    if xh == 0 or xh == W:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    elif f['y']-yh > 0:
                        direction = 'down'
                    elif f['y']-yh < 0:
                        direction = 'up'
                elif yb-yh > 0:
                    direction = 'up'
                    if yh == H or yh == 0:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    elif f['x']-xh > 0:
                        direction = 'right'
                    elif f['x']-xh < 0:
                        direction = 'left'
                elif yb-yh < 0:
                    direction = 'down'
                    if yh == 0 or yh == H:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    elif f['x']-xh > 0:
                        direction = 'right'
                    elif f['x']-xh < 0:
                        direction = 'left'
                print 'z'
            print 'one'
        elif abs(f['x']-xh) > abs(f['y']-yh):
            if f['y']-yh > 0:
                direction = 'down'
                if yb-yh > 0:
                    if yh == H or yh == 0:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    else:
                        direction = 'up'
                        if f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                elif xb-xh > 0:
                    direction = 'right'
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    else:
                        direction = 'left'
                        if f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                print 'x'
            elif f['y']-yh < 0:
                direction = 'up'
                if yb-yh < 0:
                    if yh == 0 or yh == H:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    else:
                        direction = 'down'
                        if f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                elif xb-xh < 0:
                    direction = 'left'
                    if xh == 0 or xh == W:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    else:
                        direction = 'right'
                        if f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                print 'y'
            else:
                if xb-xh > 0:
                    direction = 'left'
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    elif f['y']-yh > 0:
                        direction = 'down'
                    elif f['y']-yh < 0:
                        direction = 'up'
                elif xb-xh < 0:
                    direction = 'right'
                    if xh == 0 or xh == W:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    elif f['y']-yh > 0:
                        direction = 'down'
                    elif f['y']-yh < 0:
                        direction = 'up'
                elif yb-yh > 0:
                    direction = 'up'
                    if yh == H or yh == 0:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    elif f['x']-xh > 0:
                        direction = 'right'
                    elif f['x']-xh < 0:
                        direction = 'left'
                elif yb-yh < 0:
                    direction = 'down'
                    if yh == 0 or yh == H:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    elif f['x']-xh > 0:
                        direction = 'right'
                    elif f['x']-xh < 0:
                        direction = 'left'
                print 'z'
            print 'two'
        else:
            #equl distance
            if f['x']-xh > 0:
                direction = 'right'
                if xb-xh > 0:
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    else:
                        direction = 'left'
                        if f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                elif yb-yh > 0:
                    direction = 'down'
                    if yh == H or yh == 0:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    else:
                        direction = 'up'
                        if f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                print 'x'
                print 'one'
            elif f['x']-xh < 0:
                direction = 'left'
                if xb-xh < 0:
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    else:
                        direction = 'right'
                        if f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                elif yb-yh < 0:
                    direction = 'up'
                    if yh == 0 or yh == H:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    else:
                        direction = 'down'
                        if f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                print 'y'
                print 'one'
            elif f['y']-yh > 0:
                direction = 'down'
                if yb-yh > 0:
                    if yh == H or yh == 0:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    else:
                        direction = 'up'
                        if f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                elif xb-xh > 0:
                    direction = 'right'
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    else:
                        direction = 'left'
                        if f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                print 'x'
                print 'two'
            elif f['y']-yh < 0:
                direction = 'up'
                if yb-yh < 0:
                    if yh == 0 or yh == H:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        elif f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                    else:
                        direction = 'down'
                        if f['x']-xh > 0:
                            direction = 'right'
                        elif f['x']-xh < 0:
                            direction = 'left'
                elif xb-xh < 0:
                    direction = 'left'
                    if xh == 0 or xh == W:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        elif f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                    else:
                        direction = 'right'
                        if f['y']-yh > 0:
                            direction = 'down'
                        elif f['y']-yh < 0:
                            direction = 'up'
                print 'y'
                print 'two'
            else:
                if xb-xh > 0:
                    direction = 'right'
                    if xh == W or xh == 0:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        else:
                            direction = random.choice(x)
                    elif xb-xh > 0:
                        direction = 'left'
                elif xb-xh < 0:
                    direction = 'left'
                    if xh == 0 or xh == W:
                        if yh == H:
                            direction = 'up'
                        elif yh == 0:
                            direction = 'down'
                        else:
                            direction = random.choice(x)
                    elif xb-xh < 0:
                        direction = 'right'
                elif yb-yh > 0:
                    direction = 'down'
                    if yh == H or yh == 0:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        else:
                            direction = random.choice(y)
                    elif yb-yh > 0:
                        direction = 'up'
                elif yb-yh < 0:
                    direction = 'up'
                    if yh == 0 or yh == H:
                        if xh == W:
                            direction = 'left'
                        elif xh == 0:
                            direction = 'right'
                        else:
                            direction = random.choice(y)
                    elif yb-yh < 0:
                        direction = 'down'
                print 'z'
                print 'three'
            print 'hello'
        print 'goodbye'

    return move_response(direction)

@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
