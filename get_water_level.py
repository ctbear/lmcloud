from lmcloud.lmcloud import LMCloud
import json
import asyncio
import logging

async def main():
    with open("config.json") as f:
        data = json.load(f)

    creds = {
        "client_id": data["client_id"],
        "client_secret": data["client_secret"],
        "username": data["username"],
        "password": data["password"]
    }
    logging.basicConfig(filename="/var/log/lmcloud.log",
                        filemode="a",
                        format="%(asctime)s %(message)s",
                        level=logging.CRITICAL)
    lmcloud = await LMCloud.create(creds)
    await lmcloud.update_local_machine_status()
    if not lmcloud.current_status['water_reservoir_contact']:
        print('Water reservoir level is low')

asyncio.run(main())
