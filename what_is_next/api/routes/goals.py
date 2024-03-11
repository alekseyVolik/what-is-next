from flask import (
    Blueprint,
    request
)

from what_is_next import db
from what_is_next.goals.models import Goal
from what_is_next.api.schemas.goals import (
    GoalSchema,
    GoalsListSchema,
    CreateGoalSchema
)

bp = Blueprint('goals', __name__, url_prefix='/goals')


@bp.route('/get/all', methods=['GET', ])
def get_goals():
    """Return list all goals"""

    goals_schema = GoalsListSchema(
        goals=[GoalSchema.model_validate(goal) for goal in db.session.query(Goal)]
    )
    return goals_schema.model_dump()


@bp.route('/get/<int:ident>', methods=['GET', ])
def get_goal(ident):
    """Return goal by ident"""

    goal = db.session.get(Goal, ident)
    goal_schema = GoalSchema.model_validate(goal)
    return goal_schema.model_dump()


@bp.route('/create', methods=['POST', ])
def create_goal():
    """Create a new goal"""

    body = request.get_json()
    goal_schema = CreateGoalSchema(**body)
    goal = Goal.create_from_schema(schema=goal_schema)
    db.session.add(goal)
    db.session.commit()
    goal_schema = GoalSchema.model_validate(goal)
    return goal_schema.model_dump()
