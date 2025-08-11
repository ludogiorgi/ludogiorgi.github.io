# Personal Website

This repository contains the static files for my personal website. The list of publications on the site is automatically fetched from my Google Scholar profile using the script `update_publications.py` and the accompanying GitHub Action defined in `.github/workflows/update-publications.yml`.

The workflow runs daily and updates `publications.html` whenever new entries appear on Google Scholar. Set the `SERPAPI_API_KEY` secret in the repository settings so the action can query the [SerpAPI](https://serpapi.com/) Google Scholar endpoint. The `index.html` page loads the generated file dynamically when the site is viewed.
