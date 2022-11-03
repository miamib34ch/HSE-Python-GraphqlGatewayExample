from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TimeStampMixin(BaseModel):
    """
    Миксин для добавления атрибутов с датой и временем создания и обновления записи.
    """

    created_at: Optional[datetime] = Field(title="Дата и время создания записи")
    updated_at: Optional[datetime] = Field(title="Дата и время обновления записи")
