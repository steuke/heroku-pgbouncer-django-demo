from typing import List, Dict

import psycopg2
from psycopg2 import extras


def pgbouncer_stats() -> List[Dict]:
    """
    Retrieves the pgbouncer stats from the local pgbouncer via a Unix socket.

    Expects the pgbouncer-instance to be running on the same machine as Django, and listening
    on a Unix socket named `/tmp` (which is the default for pgbouncer.

    The Heroku build-pack's default behavior is exactly that.

    For more information, see the pgbouncer docs: https://www.pgbouncer.org/usage.html

    :returns: a list of dictionaries with the pgbouncer stats, one per database. In case of an error it returns a list
    containing a single dict with the error description.
    """
    try:
        connection = psycopg2.connect(host="/tmp/", port=6000, dbname="pgbouncer", user="pgbouncer",
                                      cursor_factory=extras.DictCursor)
        connection.autocommit = True  # must enable autocommit when querying pgbouncer stats
        cursor = connection.cursor()
        cursor.execute('SHOW STATS')
        pgbouncer_stats = [dict(row) for row in cursor]
        return pgbouncer_stats
    except Exception as e:
        return [{'error': True, 'description': 'Could not query pgbouncer stats.', 'reason': f'{e}'}]
