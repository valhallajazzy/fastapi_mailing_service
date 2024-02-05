from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from models.database import get_db
from controllers.execute_mailing import get_execute_mailing
from fastapi.responses import JSONResponse
from tasks.tasks import create_task

router = APIRouter()


# @router.get('/{mailing_id}', status_code=200)
# async def execute_mailing(mailing_id: int, db: AsyncSession = Depends(get_db)):
#     return await get_execute_mailing(db=db, mailing_id=mailing_id)

@router.post('/ex', status_code=200)
def run_task(data=Body()):
    amount = int(data["amount"])
    x = int(data["x"])
    y = int(data["y"])
    print(data)
    print(type(data))
    task = create_task.delay(amount, x, y)
    return JSONResponse({'Task': task})