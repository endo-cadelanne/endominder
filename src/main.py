import aiohttp
import asyncio
import os

import logger

# Send a post request to a ntfy server or other receiver
async def send_post(target_url: str, content: str, meta_info: dict[str, str]):
    try:
        # Open a session and name it
        async with aiohttp.ClientSession() as session:
            # send our request
            async with session.request(
                "post", target_url, data=content, headers=meta_info
                ) as response:
                response_data = await response.text()
                if response.status == 200:
                    status = "Success"
                else:
                    status = f"Failed with {response.status}"

            logger.log_write(status)

        return status

    except Exception as e:
        print(e)
        logger.log_write(e)


    
# Select target url for reminders
def url_selector(target):
    if target.lower() == "home":
        return os.getenv("home_url")
    elif target.lower() == "work":
        return os.getenv("work_url")
    elif target.lower() == "after work":
        return os.getenv("geofence_url")
    else:
        return Exception("No such target")