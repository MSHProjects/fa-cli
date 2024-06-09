BaseORM Module in Details
============

This document explains the BaseOrm works and his interation with the database.


First we have defined in the configs (at the root directory) the env variables PSQL.. You can change them later to whenver you want
you can use postgres, mysql.. (tested only on postgres)

when running the project you need to install the following requirements:
- sqlalchemy
- yoyo-migrations
- engine of the database, in my case psycog2-binray for synchronos call and asyncpg for async calls 


BaseORM
--------------

.. code-block:: python

    

    class BaseORM(Base):
    __abstract__ = True
    id = mapped_column(Integer, primary_key=True, autoincrement=True)

    def dump(self, relationships: List[str] = None):
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        if relationships:
            for rel in relationships:
                rel_data = getattr(self, rel)
                if isinstance(rel_data, list):
                    data[rel] = [item.dump() for item in rel_data]
                else:
                    data[rel] = rel_data.dump() if rel_data else None
        return data

    @classmethod
    async def select(cls, **kwargs) -> List[Any]:
        async with sessionmanager.session() as session:
            query = select(cls)
            relationships = []
            for name, attr in cls.__dict__.items():
                if isinstance(attr, InstrumentedAttribute) and hasattr(attr.property, 'direction'):
                    relationships.append(name)
                    query = query.options(joinedload(getattr(cls, name)))
            for attr, value in kwargs.items():
                query = query.where(getattr(cls, attr) == value)
            result = await session.execute(query)
            instances = result.unique().scalars().all()
            return [instance.dump(relationships) for instance in instances]

    @classmethod
    async def insert(cls, **kwargs) -> Dict:
        async with sessionmanager.session() as session:
            obj = cls(**kwargs)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj.dump()

    @classmethod
    async def update(cls, values: Dict[str, Any], **kwargs) -> None:
        async with sessionmanager.session() as session:
            query = sqlalchemy_update(cls).where(
                *(getattr(cls, attr) == value for attr, value in kwargs.items())
            ).values(**values)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **kwargs) -> None:
        async with sessionmanager.session() as session:
            query = sqlalchemy_delete(cls).where(
                *(getattr(cls, attr) == value for attr, value in kwargs.items())
            )
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, values: Dict[str, Any], **kwargs) -> None:
        async with sessionmanager.session() as session:
            query = sqlalchemy_update(cls).where(
                *(getattr(cls, attr) == value for attr, value in kwargs.items())
            ).values(**values)
            await session.execute(query)
            await session.commit()


This class this class will be the root for every table that we will define later in our application,
it contains the mendatory functions for a crud applications
you can use it as the following:

- ORM definition:
----

.. code-block:: python

    class Users(BaseORM):
        __tablename__ = "users"
        name = mapped_column(VARCHAR, nullable=False)
        email = mapped_column(VARCHAR)
        password = mapped_column(VARCHAR)
        active = mapped_column(BOOLEAN)
        dns = relationship("Dns", back_populates="user",
                        cascade="all, delete-orphan")

RQ: don't forget the relationships if needed since they really make difference in the response

Example of Usage:
----
.. code-block:: python

    
    from src.db.tables.user import Users

    async def create_user(self, user: UserCreate):
        exist = await Users.select(email=user.email)
        ...
        registerd = await Users.insert(**user.dict())


In case you want to do complex opeartions, call the function from sqlalchemy and use it as the following:

.. code-block:: python

    
    from src.db.tables.user import Users
    from sqlalchemy.future import select
    from src.db.connector import sessionmanager


    async def create_user(self, id):
        async with sessionmanager.session() as session:
            query = select(Users).where(Users.id = id )
            users = await session.execute(query)
            result = users.unique().scalars().all()
        
it's the same the only difference is you can instead of writing 4 line of code, you write 1 single code
It's up to you to use the method you like