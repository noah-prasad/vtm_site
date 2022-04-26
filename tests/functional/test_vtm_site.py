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
        assert b"Lorem ipsum " in res.data 
    
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
        assert b"Lorem ipsum " in res.data 


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