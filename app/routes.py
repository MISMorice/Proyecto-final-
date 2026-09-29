from flask import Blueprint, render_template, redirect, url_for

from app.database import get_items
from app.services.scraping_service import run_scraper

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    items = get_items()

    return render_template(
        "dashboard.html",
        items=items
    )

@main.route("/scrape", methods=["POST"])
def scrape():
    run_scraper()

    return redirect(url_for("main.dashboard"))