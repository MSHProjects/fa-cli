Important remarks
============

I hightly recommand that in the migrations you use this command: 


.. code-block:: bash
    
    fa g m MyMigration


Why?

The code actually reads the ./src/db/migrations folder see the last index and increment it by one
so when running the migrations there is no conflict happens and they are unique



I hightly recommand that each migration file, in your step you write the action that you want to make and its rollback so in production you can handle the issues in a faster way

To execute the rollback


.. code-block:: bash

    bash migration_rollback.sh




General remarks:
----

1. Don't forget to change the env values
2. Try before running the migration to validate the sql query and ofcourse before running the project create the database at least!!
3. Be carefull with the namings for the controller and the migration
4. If you got any question feel free to send a mail at `hammamimedsoulaimen@gmail.com`