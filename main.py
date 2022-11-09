import traceback
import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from common.r import MyException404
from routers.project_router import router as project
from routers.environment_router import router as environment
from routers.group_router import router as group
from routers.api_router import router as api
from routers.test_log_router import router as test_log
from routers.test_report_router import router as test_report
from routers.testcase_router import router as testcase
from routers.test_user_router import router as test_user

app = FastAPI()
app.include_router(project)
app.include_router(environment)
app.include_router(group)
app.include_router(api)
app.include_router(test_log)
app.include_router(test_report)
app.include_router(testcase)
app.include_router(test_user)


@app.exception_handler(MyException404)
def my_exception_404_handler(request: Request, exc: MyException404):
    # logging.Logger.error(
    #     f'url:{request.url}, method:{request.method}, headers:{request.headers}\n{traceback.format_exc()}')
    return JSONResponse(
        status_code=exc.code,
        content={"code": exc.code, "message": f"{exc.message}, 信息跟踪：{traceback.format_exc()}"}
    )


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
