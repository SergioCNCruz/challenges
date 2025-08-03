"""FastAPI application exposing scraper results."""
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .database import Base, SessionLocal, engine
from .models import ScrapeResult
from .scraper import fetch_title

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/scrape")
def scrape(url: str, db: Session = Depends(get_db)):
    """Scrape the given URL and store the result in the database."""
    title = fetch_title(url)
    result = ScrapeResult(url=url, title=title)
    db.add(result)
    db.commit()
    db.refresh(result)
    return {"url": result.url, "title": result.title}


@app.get("/results")
def list_results(db: Session = Depends(get_db)):
    """Return all stored scrape results."""
    results = db.query(ScrapeResult).all()
    return [
        {"url": r.url, "title": r.title, "created_at": r.created_at}
        for r in results
    ]
