from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from nextjs_fastapi_crud_backend_api.core import config,todo
from nextjs_fastapi_crud_backend_api.routers.todo import router as api_router

def get_application():
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION) # 変更

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", todo.create_start_app_handler(app)) # 追加
    app.add_event_handler("shutdown", todo.create_stop_app_handler(app)) # 追加

    app.include_router(api_router)

    return app

app = get_application()