import asyncio, uvicorn

async def app():
    config = uvicorn.Config("main:app", port=8000, host="lostvayne", log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(app())