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
    target_coffee_boiler_status = not lmcloud.current_status['coffee_boiler_on']
    await lmcloud.set_power(target_coffee_boiler_status)
    logging.getLogger(__name__).critical("Setting coffee boiler to " + ("ON" if target_coffee_boiler_status else "OFF"))
    print("Setting coffee boiler to " + ("ON" if target_coffee_boiler_status else "OFF"))

asyncio.run(main())
