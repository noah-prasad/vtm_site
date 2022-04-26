def test_index_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    print(" -- / GET test")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Vertical Tank Maintenance" in res.data
        assert b"Welcome to VTM!" in res.data 
        assert b"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Erat velit scelerisque in dictum non consectetur a erat. Leo urna molestie at elementum eu facilisis. Fermentum dui faucibus in ornare quam viverra orci sagittis eu. Felis donec et odio pellentesque diam volutpat. Egestas pretium aenean pharetra magna ac placerat vestibulum. Faucibus vitae aliquet nec ullamcorper sit amet risus. Curabitur gravida arcu ac tortor dignissim convallis aenean et tortor. Neque volutpat ac tincidunt vitae semper quis lectus nulla. Nec feugiat in fermentum posuere urna nec tincidunt praesent semper. Diam sit amet nisl suscipit adipiscing bibendum. Etiam erat velit scelerisque in dictum non. Neque laoreet suspendisse interdum consectetur libero id. Elementum integer enim neque volutpat. A iaculis at erat pellentesque. Vel risus commodo viverra maecenas. Sed felis eget velit aliquet. Fames ac turpis egestas integer eget. Morbi blandit cursus risus at ultrices. Sit amet nisl suscipit adipiscing bibendum est. Phasellus faucibus scelerisque eleifend donec pretium. Quis risus sed vulputate odio ut. Morbi blandit cursus risus at ultrices mi tempus imperdiet. Sapien faucibus et molestie ac feugiat sed. Nec dui nunc mattis enim ut tellus elementum sagittis vitae. Mi sit amet mauris commodo quis imperdiet massa. Vulputate mi sit amet mauris commodo quis imperdiet. Nibh tellus molestie nunc non blandit massa enim. At erat pellentesque adipiscing commodo. Euismod elementum nisi quis eleifend quam adipiscing. Bibendum at varius vel pharetra vel turpis nunc." in res.data 
    
def test_about_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    print(" -- /about GET test")
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About VTM" in res.data
        assert b"About Vertical Tank Maintenance" in res.data 
        assert b"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Egestas integer eget aliquet nibh praesent tristique magna sit amet. Neque laoreet suspendisse interdum consectetur libero. A scelerisque purus semper eget duis at. Scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam malesuada. Ac tortor dignissim convallis aenean et tortor at. Donec ac odio tempor orci. Aliquet risus feugiat in ante. Egestas egestas fringilla phasellus faucibus scelerisque. Malesuada fames ac turpis egestas sed tempus urna. Commodo quis imperdiet massa tincidunt nunc pulvinar sapien. Augue neque gravida in fermentum. Turpis egestas sed tempus urna. Quis varius quam quisque id diam vel." in res.data 


def test_estimate_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    print(" -- /estimate GET test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"Price Estimator" in res.data
        assert b"Create an Estimate" in res.data 
        assert b"Enter Tank Information:" in res.data
        assert b"Your Price Estimate" in res.data

def test_estimate_functionality(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (POST)
    THEN check that the response is valid
    """
    print(" -- /estimate POST test")
    with app.test_client() as test_client:
        tank_specs = {"radius":"180", "height":"360"} 
        res = test_client.post('/estimate', data=tank_specs)
        assert res.status_code == 200
        assert b"$141300.0" in res.data