Controller Module in Details
============

This document explains the controller work and interation with other components provided by `fa-cli`.


core
--------------

.. code-block:: python

    
    def Controller(cls):
        cls.controller = True
        return cls

This function defines if a class is considered as a Controller or not.
When creating the controller you will find something similar to the following :

.. code-block:: python

    
    @Controller
    class UserController(GenericController):
        pass

if you remove it all the routes that you will define later won't be considered


.. code-block:: python

    
    class GenericController():

        def __init__(self, app: APIRouter) -> None:
            self.app: APIRouter = app
            self.router: APIRouter = APIRouter()

        def add_api_route(self, path, endpoint, methods, dependencies: list = None):
            self.router.add_api_route(
                path, endpoint, methods=methods, dependencies=dependencies)

This class is the core of the application, every router later will inherit from it
