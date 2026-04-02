from datetime import date
from sqlalchemy import Date, Float, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)        # negative = expense, positive = income
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    is_recurring: Mapped[bool] = mapped_column(Boolean, default=False)  # True for detected subscriptions
