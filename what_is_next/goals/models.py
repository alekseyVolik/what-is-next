from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import (
    String,
    DateTime,
    func
)

from what_is_next import db
from what_is_next.api.schemas.goals import CreateGoalSchema


class Goal(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    @staticmethod
    def create_from_schema(schema: CreateGoalSchema) -> Goal:
        return Goal(title=schema.title)

    def __repr__(self):
        return f"Goal(id={self.id}, title={self.title}, create_at={self.create_at})"
