class Database:
    """The Database Implementation."""
    def __init__(self, connection: str | None = None) -> None:
        """Create a connection to a database."""
        pass

# database = Database("file:/path/to/database")

def get_database(connection: str | None = None) -> Database:
    global db
    if not db:
        db = Database(connection)
    return db
