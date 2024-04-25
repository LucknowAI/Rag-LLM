from FastAPI.wrapper import FastAPIChatClient

ob = FastAPIChatClient("https://0ac6-49-36-210-150.ngrok-free.app/")
print(ob.chat("1", "hello"))
