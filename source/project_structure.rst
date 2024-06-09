Project Structure
=================

This document explains the structure of the project and how each module interacts.

Directory Structure
-------------------

.. code-block:: text

    .
    ├── .gitignore
    ├── app.py
    ├── configs.py
    ├── .env
    ├── migration_rollback.sh
    ├── requirements.txt
    ├── yoyo.ini
    ├── src/
    │   ├── common/
    │   │   ├── hasher.py
    │   │   └── jwt_token.py
    │   ├── controller/
    │   │   ├── core.py
    │   │   ├── __init__.py
    │   │   └── user/
    │   │       ├── router.py
    │   │       └── schema.py
    │   ├── db/
    │   │   ├── connector.py
    │   │   ├── core_orm.py
    │   │   ├── migration.py
    │   │   └── tables/
    │   │       └── user.py
    │   └── middleware/
    │       ├── jwt_middleware.py
    │       └── logging_middleware.py
    └── .vscode/
        └── launch.json

Module Descriptions
-------------------

**app.py**:
Initializes the FastAPI application, sets up middleware, and includes controllers.

**configs.py**:
Loads environment variables and configurations, including database and JWT settings.

**.env**:
Stores environment variables.

**migration_rollback.sh**:
Script to rollback migrations using Yoyo.

**requirements.txt**:
Lists project dependencies.

**yoyo.ini**:
Configuration file for Yoyo migrations.

**src/common/**:
Contains common utilities like password hashing and JWT token management.

**src/controller/**:
Defines API controllers. The `core.py` defines base controller classes, and the `user` directory contains the user-specific controller and schemas.

**src/db/**:
Handles database connections, ORM models, and migrations.

**src/middleware/**:
Implements custom middleware for JWT authentication and logging.

**.vscode/launch.json**:
Configuration for debugging in Visual Studio Code.
