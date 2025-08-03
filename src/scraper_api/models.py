"""Database models."""
from sqlalchemy import Column, DateTime, Integer, String, func

from .database import Base


class ScrapeResult(Base):
    """Stores the scraped page title for a given URL."""

    __tablename__ = "scrape_results"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
