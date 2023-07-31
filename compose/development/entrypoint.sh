#!/bin/bash

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

postgres_ready() {
python3 - << END
import asyncio
import asyncpg

async def check_connection():
    try:
        # Create a connection pool asynchronously
        connection_pool = await asyncpg.create_pool(
            database="${POSTGRES_DATABASE}",
            user="${POSTGRES_USER}",
            password="${POSTGRES_PASSWORD}",
            host="${POSTGRES_HOST}",
            port="${POSTGRES_PORT}",
        )
        # Get a connection from the pool
        async with connection_pool.acquire() as connection:
            pass  # You can perform any asynchronous database operation here

    except asyncpg.exceptions.PostgresError:
        exit_code = 1
    else:
        exit_code = 0
    return exit_code

# Run the asynchronous function in an asyncio event loop
exit_code = asyncio.run(check_connection())
exit(exit_code)
END
}

until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'

exec "$@"
