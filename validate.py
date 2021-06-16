#!/usr/bin/env python
import snowflake.connector
from credentials import SnowflakeConfigs

# Gets the version
ctx = snowflake.connector.connect(
    authenticator='externalbrowser',
    user=SnowflakeConfigs.USER,
    # password=SnowflakeConfigs.password,
    account=SnowflakeConfigs.ACCOUNT,
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()
