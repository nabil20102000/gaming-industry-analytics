"""Beginner-friendly Steam market snapshot analysis.

Downloads open CSV files from the Crawlora Steam Catalog Dataset (CC BY 4.0),
cleans them, saves clean copies, and creates simple charts.

Run from VS Code terminal:
    python market_analysis.py

Internet is needed for the first run. The raw files are kept in data/raw.
"""
from pathlib import Path
import sys
import requests
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
CLEAN = ROOT / "data" / "cleaned"
CHARTS = ROOT / "outputs" / "charts"
for folder in (RAW, CLEAN, CHARTS):
    folder.mkdir(parents=True, exist_ok=True)

BASE = "https://raw.githubusercontent.com/Crawlora-org/steam-catalog-data/main/data/"
FILES = {
    "pricing-by-year.csv": "pricing_by_year.csv",
    "review-by-genre.csv": "review_by_genre.csv",
    "genres.csv": "genres.csv",
    "price-tiers.csv": "price_tiers.csv",
    "ownership-concentration.csv": "ownership_concentration.csv",
}


def download_file(url: str, destination: Path) -> None:
    """Download a file only when it is not already on your computer."""
    if destination.exists() and destination.stat().st_size > 0:
        print(f"Already downloaded: {destination.name}")
        return
    print(f"Downloading {destination.name} ...")
    try:
        response = requests.get(url, timeout=45)
        response.raise_for_status()
        destination.write_bytes(response.content)
    except requests.RequestException as exc:
        raise RuntimeError(
            f"Could not download {destination.name}. Check your internet connection, "
            "or download it manually from the source links in the guide."
        ) from exc


def clean_csv(filename: str, output_name: str) -> pd.DataFrame:
    """Read a CSV, tidy column names/text, remove duplicates, and type numbers."""
    path = RAW / filename
    df = pd.read_csv(path)
    df.columns = [str(column).strip().lower() for column in df.columns]
    df = df.dropna(how="all").drop_duplicates().copy()
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].astype("string").str.strip()
    for column in df.columns:
        if column not in {"genre", "price_tier", "top_slice"}:
            converted = pd.to_numeric(df[column], errors="coerce")
            if converted.notna().any():
                df[column] = converted
    df.to_csv(CLEAN / output_name, index=False)
    print(f"Saved cleaned file: {output_name} ({len(df):,} rows)")
    return df


def save_chart(filename: str) -> None:
    plt.tight_layout()
    plt.savefig(CHARTS / filename, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"Saved chart: {filename}")


def main() -> int:
    try:
        for filename, _ in FILES.items():
            download_file(BASE + filename, RAW / filename)

        pricing = clean_csv("pricing-by-year.csv", "pricing_by_year_clean.csv")
        reviews = clean_csv("review-by-genre.csv", "review_by_genre_clean.csv")
        genres = clean_csv("genres.csv", "genres_clean.csv")
        tiers = clean_csv("price-tiers.csv", "price_tiers_clean.csv")
        ownership = clean_csv("ownership-concentration.csv", "ownership_concentration_clean.csv")

        # The dataset notes that 2025-2026 have smaller samples.
        # Keep those years in the clean data, but use 2006-2024 for the main trend chart.
        trend = pricing.loc[pricing["release_year"] <= 2024].copy()
        plt.figure(figsize=(10, 5))
        plt.plot(trend["release_year"], trend["median_price_usd"], marker="o")
        plt.title("Median listed price by release year (USD)")
        plt.xlabel("Release year")
        plt.ylabel("Median listed price (USD)")
        plt.grid(True, alpha=0.25)
        save_chart("median_price_by_year.png")

        plt.figure(figsize=(10, 5))
        plt.plot(trend["release_year"], trend["free_share"] * 100, marker="o")
        plt.title("Free-to-play share by release year")
        plt.xlabel("Release year")
        plt.ylabel("Free-to-play titles (%)")
        plt.grid(True, alpha=0.25)
        save_chart("free_to_play_share_by_year.png")

        top_genres = genres.sort_values("games", ascending=False).head(10).sort_values("games")
        plt.figure(figsize=(9, 6))
        plt.barh(top_genres["genre"], top_genres["games"])
        plt.title("Most common Steam genre tags in the dataset")
        plt.xlabel("Number of games carrying the tag")
        save_chart("top_genres.png")

        top_review_genres = reviews.sort_values("titles", ascending=False).head(10).sort_values("median_review_score")
        plt.figure(figsize=(9, 6))
        plt.barh(top_review_genres["genre"], top_review_genres["median_review_score"])
        plt.title("Median Steam review score by genre tag")
        plt.xlabel("Median review score (0 to 1)")
        save_chart("review_score_by_genre.png")

        plt.figure(figsize=(8, 5))
        plt.bar(tiers["price_tier"], tiers["games"])
        plt.title("Games by listed price tier")
        plt.xlabel("Price tier")
        plt.ylabel("Number of games")
        plt.xticks(rotation=25, ha="right")
        save_chart("games_by_price_tier.png")

        plt.figure(figsize=(8, 5))
        plt.bar(ownership["top_slice"], ownership["owner_share"] * 100)
        plt.title("Share of estimated owners held by top-ranked games")
        plt.xlabel("Share of games, ranked by owner estimate")
        plt.ylabel("Share of estimated owners (%)")
        plt.xticks(rotation=20, ha="right")
        save_chart("ownership_concentration.png")

        summary = [
            "STEAM CATALOG SNAPSHOT - AUTOMATED OUTPUT",
            "Dataset: Crawlora Steam Catalog Dataset, version 2; snapshot 2026-09-07.",
            "Universe: top 10,000 Steam games by SteamSpy owner estimate, not every Steam listing.",
            "Owner estimates are ranges, not exact sales or unique active users.",
            "2025-2026 release-year samples are smaller; interpret cautiously.",
            "Genre tags overlap; a game can appear in more than one genre.",
            "",
            f"Games in price-tier table: {int(tiers['games'].sum()):,}",
            f"Games carrying genre tags (sum; tags overlap): {int(genres['games'].sum()):,}",
        ]
        (ROOT / "outputs").mkdir(exist_ok=True)
        (ROOT / "outputs" / "read_me_first.txt").write_text("\n".join(summary), encoding="utf-8")
        print("\nFinished. Open the outputs/charts folder to see your charts.")
        print("Read outputs/read_me_first.txt before writing conclusions.")
        return 0
    except (FileNotFoundError, KeyError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print("Check that the CSV downloads completed and that the dataset columns match the guide.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
