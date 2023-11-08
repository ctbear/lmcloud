from lmcloud.lmcloud import LMCloud
import json
import asyncio

async def main():
    with open("config.json") as f:
        data = json.load(f)

    creds = {
        "client_id": data["client_id"],
        "client_secret": data["client_secret"],
        "username": data["username"],
        "password": data["password"]
    }
    lmcloud = await LMCloud.create(creds)
    await lmcloud.update_local_machine_status()
    target_coffee_boiler_status = not lmcloud.current_status['coffee_boiler_on']
    await lmcloud.set_power(target_coffee_boiler_status)
    print("Setting coffee boiler to " + ("ON" if target_coffee_boiler_status else "OFF"))

asyncio.run(main())
