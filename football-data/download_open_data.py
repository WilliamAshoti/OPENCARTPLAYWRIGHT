#!/usr/bin/env python3
"""Download the free data that StatsBomb (Hudl), IMPECT and Wyscout publish themselves.

Only the official open-data releases are used; no paid API, login or third-party
site is touched. Each dataset has its own licence (non-commercial, attribution
required, no redistribution), so the files are written to a local folder that is
git-ignored and should not be re-published.

Examples:
    python download_open_data.py statsbomb list
    python download_open_data.py statsbomb get --competition 9 --season 281
    python download_open_data.py statsbomb get --all --no-360
    python download_open_data.py impect list
    python download_open_data.py impect get --limit 5
    python download_open_data.py wyscout list
    python download_open_data.py wyscout get --competition England
    python download_open_data.py wyscout get --raw

Only the Python standard library is needed.
"""

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

STATSBOMB_BASE = "https://raw.githubusercontent.com/hudl/open-data/master/data"
IMPECT_BASE = "https://raw.githubusercontent.com/ImpectAPI/open-data/main/data"
WYSCOUT_BASE = "https://raw.githubusercontent.com/koenvo/wyscout-soccer-match-event-dataset/main"

# Wyscout competitions in the Pappalardo et al. (2019) release, keyed by the
# source file name used in the index of the GitHub mirror.
WYSCOUT_COMPETITIONS = {
    "England": "Premier League 2017/18",
    "France": "Ligue 1 2017/18",
    "Germany": "Bundesliga 2017/18",
    "Italy": "Serie A 2017/18",
    "Spain": "La Liga 2017/18",
    "World_Cup": "FIFA World Cup 2018",
    "European_Championship": "UEFA Euro 2016",
}

# Original figshare files (CC BY 4.0) for users who want the raw zips.
WYSCOUT_FIGSHARE = {
    "players.json": "https://ndownloader.figshare.com/files/15073721",
    "teams.json": "https://ndownloader.figshare.com/files/15073697",
    "matches.zip": "https://ndownloader.figshare.com/files/14464622",
    "events.zip": "https://ndownloader.figshare.com/files/14464685",
}

USER_AGENT = "football-open-data-downloader/1.0"


def fetch(url, retries=4):
    """Return the body of url, or None on 404. Retries other errors with backoff."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            if attempt == retries:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries:
                raise
        time.sleep(2 ** (attempt + 1))
    return None


def fetch_json(url):
    body = fetch(url)
    if body is None:
        raise SystemExit(f"Not found: {url}")
    return json.loads(body)


def save(url, path, overwrite=False):
    """Download url to path unless it already exists. Returns a status string."""
    if path.exists() and not overwrite:
        return "skipped"
    body = fetch(url)
    if body is None:
        return "missing"
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".part")
    tmp.write_bytes(body)
    tmp.replace(path)
    return "downloaded"


def save_many(jobs, workers, overwrite):
    """Download (url, path) pairs in parallel and print a summary."""
    counts = {"downloaded": 0, "skipped": 0, "missing": 0, "failed": 0}
    total = len(jobs)

    def run(job):
        url, path = job
        try:
            return save(url, path, overwrite)
        except Exception as error:  # keep going; report at the end
            print(f"  failed: {url} ({error})", file=sys.stderr)
            return "failed"

    with ThreadPoolExecutor(max_workers=workers) as pool:
        for done, status in enumerate(pool.map(run, jobs), start=1):
            counts[status] += 1
            if done % 25 == 0 or done == total:
                print(f"  {done}/{total} files", file=sys.stderr)
    print(", ".join(f"{name}: {count}" for name, count in counts.items()))
    return counts


# --- StatsBomb -----------------------------------------------------------------


def statsbomb_list(_args):
    competitions = fetch_json(f"{STATSBOMB_BASE}/competitions.json")
    print(f"{'comp':>5} {'season':>6}  {'gender':6}  {'360':3}  competition / season")
    for c in sorted(competitions, key=lambda c: (c["competition_name"], c["season_name"])):
        has_360 = "yes" if c.get("match_available_360") else "-"
        print(
            f"{c['competition_id']:>5} {c['season_id']:>6}  {c['competition_gender']:6}  "
            f"{has_360:3}  {c['country_name']} - {c['competition_name']} {c['season_name']}"
        )
    print(f"\n{len(competitions)} competition-seasons. Use: statsbomb get --competition ID --season ID")


def statsbomb_get(args):
    out = Path(args.out) / "statsbomb"
    competitions = fetch_json(f"{STATSBOMB_BASE}/competitions.json")
    out.mkdir(parents=True, exist_ok=True)
    (out / "competitions.json").write_text(json.dumps(competitions, indent=1), encoding="utf-8")

    if args.all:
        selected = [(c["competition_id"], c["season_id"]) for c in competitions]
    elif args.competition is not None:
        selected = [
            (c["competition_id"], c["season_id"])
            for c in competitions
            if c["competition_id"] == args.competition
            and (args.season is None or c["season_id"] == args.season)
        ]
    else:
        raise SystemExit("Pass --competition ID [--season ID] or --all (see: statsbomb list)")
    if not selected:
        raise SystemExit("No matching competition/season. Run: statsbomb list")

    jobs = []
    for competition_id, season_id in selected:
        matches_url = f"{STATSBOMB_BASE}/matches/{competition_id}/{season_id}.json"
        matches_path = out / "matches" / str(competition_id) / f"{season_id}.json"
        save(matches_url, matches_path, args.overwrite)
        matches = json.loads(matches_path.read_text(encoding="utf-8"))
        if args.limit:
            matches = matches[: args.limit]
        print(f"StatsBomb {competition_id}/{season_id}: {len(matches)} matches")
        for match in matches:
            match_id = match["match_id"]
            jobs.append((f"{STATSBOMB_BASE}/events/{match_id}.json", out / "events" / f"{match_id}.json"))
            jobs.append((f"{STATSBOMB_BASE}/lineups/{match_id}.json", out / "lineups" / f"{match_id}.json"))
            if not args.no_360 and match.get("match_status_360") == "available":
                jobs.append(
                    (f"{STATSBOMB_BASE}/three-sixty/{match_id}.json", out / "three-sixty" / f"{match_id}.json")
                )
    save_many(jobs, args.workers, args.overwrite)
    print(f"Saved to {out}")


# --- IMPECT --------------------------------------------------------------------


def impect_list(_args):
    for iteration in fetch_json(f"{IMPECT_BASE}/iterations.json"):
        matches = fetch_json(f"{IMPECT_BASE}/matches/matches_{iteration['id']}.json")
        competition = iteration["competition"]
        print(
            f"iteration {iteration['id']}: {competition['name']} {iteration['season']} "
            f"({competition['gender'].lower()}) - {len(matches)} matches"
        )


def impect_get(args):
    out = Path(args.out) / "impect"
    jobs = []
    for name in ("countries.json", "iterations.json", "kpi_definitions.json"):
        jobs.append((f"{IMPECT_BASE}/{name}", out / name))
    iterations = fetch_json(f"{IMPECT_BASE}/iterations.json")
    for iteration in iterations:
        iteration_id = iteration["id"]
        for folder in ("matches", "players", "squads"):
            jobs.append(
                (f"{IMPECT_BASE}/{folder}/{folder}_{iteration_id}.json", out / folder / f"{folder}_{iteration_id}.json")
            )
        matches = fetch_json(f"{IMPECT_BASE}/matches/matches_{iteration_id}.json")
        matches = [m for m in matches if m.get("available", True)]
        if args.limit:
            matches = matches[: args.limit]
        print(f"IMPECT iteration {iteration_id}: {len(matches)} matches")
        for match in matches:
            match_id = match["id"]
            for folder in ("events", "events_kpis", "lineups", "player_kpis"):
                jobs.append(
                    (f"{IMPECT_BASE}/{folder}/{folder}_{match_id}.json", out / folder / f"{folder}_{match_id}.json")
                )
    save_many(jobs, args.workers, args.overwrite)
    print(f"Saved to {out}")


# --- Wyscout -------------------------------------------------------------------


def wyscout_index():
    """Parse the match index of the GitHub mirror into (match_id, label, date, competition)."""
    body = fetch(f"{WYSCOUT_BASE}/processed-v2/README.md")
    if body is None:
        raise SystemExit("Wyscout index not found")
    rows = []
    for line in body.decode("utf-8").splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4 or not cells[0].startswith("["):
            continue
        match_id = cells[0][1 : cells[0].index("]")]
        competition = cells[3].removeprefix("matches_").removesuffix(".json")
        rows.append((int(match_id), cells[1], cells[2], competition))
    return rows


def wyscout_list(_args):
    counts = {}
    for _, _, _, competition in wyscout_index():
        counts[competition] = counts.get(competition, 0) + 1
    for competition, count in counts.items():
        print(f"{competition:22} {WYSCOUT_COMPETITIONS.get(competition, ''):24} {count} matches")
    print("\nUse: wyscout get --competition NAME   (or --raw for the original figshare zips)")


def wyscout_get(args):
    out = Path(args.out) / "wyscout"
    if args.raw:
        jobs = [(url, out / "raw" / name) for name, url in WYSCOUT_FIGSHARE.items()]
        save_many(jobs, args.workers, args.overwrite)
        print(f"Saved to {out / 'raw'}")
        return

    rows = wyscout_index()
    if args.competition:
        if args.competition not in WYSCOUT_COMPETITIONS:
            raise SystemExit(f"Unknown competition. Choose from: {', '.join(WYSCOUT_COMPETITIONS)}")
        rows = [row for row in rows if row[3] == args.competition]
    if args.limit:
        rows = rows[: args.limit]
    print(f"Wyscout: {len(rows)} matches")

    out.mkdir(parents=True, exist_ok=True)
    index = [{"match_id": m, "label": label, "date": date, "competition": comp} for m, label, date, comp in rows]
    (out / "index.json").write_text(json.dumps(index, indent=1), encoding="utf-8")
    jobs = [
        (f"{WYSCOUT_BASE}/raw_data/players.json", out / "players.json"),
        (f"{WYSCOUT_BASE}/raw_data/teams.json", out / "teams.json"),
    ]
    for match_id, _, _, competition in rows:
        jobs.append(
            (f"{WYSCOUT_BASE}/processed-v2/files/{match_id}.json", out / "matches" / competition / f"{match_id}.json")
        )
    save_many(jobs, args.workers, args.overwrite)
    print(f"Saved to {out}")


# --- CLI -----------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    providers = parser.add_subparsers(dest="provider", required=True)

    def add_provider(name, list_func, get_func, extra):
        provider = providers.add_parser(name, help=f"{name} open data")
        actions = provider.add_subparsers(dest="action", required=True)
        actions.add_parser("list", help="show what is available").set_defaults(func=list_func)
        get = actions.add_parser("get", help="download")
        get.add_argument("--out", default=str(Path(__file__).parent / "data"), help="output folder")
        get.add_argument("--limit", type=int, help="max matches per competition-season (for testing)")
        get.add_argument("--workers", type=int, default=8, help="parallel downloads")
        get.add_argument("--overwrite", action="store_true", help="re-download existing files")
        extra(get)
        get.set_defaults(func=get_func)

    def statsbomb_args(get):
        get.add_argument("--competition", type=int, help="competition_id (see list)")
        get.add_argument("--season", type=int, help="season_id (see list); default: all seasons")
        get.add_argument("--all", action="store_true", help="every competition-season (several GB)")
        get.add_argument("--no-360", action="store_true", help="skip StatsBomb 360 freeze frames")

    def wyscout_args(get):
        get.add_argument("--competition", help=f"one of: {', '.join(WYSCOUT_COMPETITIONS)}")
        get.add_argument("--raw", action="store_true", help="download the original figshare files instead")

    add_provider("statsbomb", statsbomb_list, statsbomb_get, statsbomb_args)
    add_provider("impect", impect_list, impect_get, lambda get: None)
    add_provider("wyscout", wyscout_list, wyscout_get, wyscout_args)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
