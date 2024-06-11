from flask import jsonify
from flask_openapi3 import APIBlueprint

from .schemas import UsersResponse
from app.tasks.telegram_tasks import send_message

bp = APIBlueprint('v1',
                  __name__,
                  url_prefix='/v1')


@bp.get('/users')
async def get_users():
    response = UsersResponse().model_dump()
    await send_message(810858640, 'test')
    return jsonify({'users': response})
