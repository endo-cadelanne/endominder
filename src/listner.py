from aiohttp import web

async def handle_post(request):
    data = await request.json()

    return data

app = web.Application()
app.router.add_post("/submit", handle_post)

if __name__ == "__main__":
    web.run_app(app, port=8080)