import os, configparser
import uvicorn, fastapi

class Common:
  def __init__(self) -> None:
    self._config_path: str = f"{os.path.dirname(__file__)}/config.ini"
    self._config: configparser.ConfigParser = configparser.ConfigParser()
    self._config.read(self._config_path)

class App:
  def __init__(self) -> None:
    self.app: fastapi.FastAPI = fastapi.FastAPI()
    self.setup_routes()

  def setup_routes(self) -> None:
    @self.app.get("/")
    async def main() -> dict[str, str]:
      return {"message": "Hello World"}

  def run(self) -> None:
    uvicorn.run(self.app, host='0.0.0.0', port=8000, log_level='info')

if __name__ == "__main__":
  app: App = App()
  app.run()
