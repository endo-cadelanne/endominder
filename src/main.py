import aiohttp
import asyncio
import os

import logger

async def send_notification(content: str, meta_info: dict[str, str]):
    # Open a session and name it
    async with aiohttp.ClientSession() as session:
        # send our request
        async with session.request(
            "post", ntfy_server, data=content, headers=meta_info
            ) as response:
            response_data = await response.text()
            if response.status == 200:
                status = "Success"
            else:
                status = f"Failed with {response.status}"

        logger.log_write(status)

    return status
    

