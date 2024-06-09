CLI Commands
============

This document explains the CLI commands provided by `fa-cli`.

Commands
--------

**fa new project <name of the project>**:
Creates a new project with the specified name.

**fa generate controller <name of controller>**:
Generates a new controller with the specified name.

**fa rm controller <name of the controller>**:
Removes the controller with the specified name.

**fa generate migration <name of the migration>**:
Generates a new migration with the specified name.

Usage Examples
--------------

.. code-block:: bash

    # Create a new project
    fa new project MyNewProject
    # or 
    fa n p MyNewProject

    # Generate a new controller
    fa generate controller UserController

    # or 
    fa g c UserController

    # Remove a controller
    fa rm controller UserController

    # or
    fa r c UserController

    # Generate a new migration
    fa generate migration AddUserTable

    # or

    fa g m AddUserTable
