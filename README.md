# Md. Basim Al Zabir Shammo — portfolio

This archive contains the complete published static site, including its home page,
research, projects, publications, courses, skills, education, experience,
achievements, image assets, document previews, and downloadable documents.
The pages work under a GitHub Pages repository URL as well as a custom domain.

## Publish on GitHub Pages

1. Create a GitHub repository and upload **the contents of this ZIP** into the
   repository's top level. `index.html`, `style.css`, `app.js`, `assets/`, and
   `.nojekyll` belong at the top level; do not upload the ZIP as a single file.
2. In the repository, open Settings → Pages. Under Build and deployment, choose
   **Deploy from a branch**. Set the branch to **main** and folder to **/(root)**,
   then save.
3. After GitHub publishes it, use the URL shown in the Pages settings. A usual
   project URL is `https://YOUR_USERNAME.github.io/YOUR_REPOSITORY/`.

GitHub's official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Files and edits

- `index.html`, each section's `index.html`, `style.css`, `app.js`, and
  `search-index.json` are the ready-to-publish site.
- `assets/` holds the images, certificates, publication screenshots, and PDFs.
- `source/build.py` and `source/asset-map.json` are the editable Python site
  generator and its asset mapping. The original exported assets are already in
  `assets/`. If you edit the generator, install `pymupdf` and `pillow`, then run
  `python source/build.py` from the repository root to regenerate the pages.
  `source/prepare_github_pages.py` handles repository-safe relative URLs.

Links to publishers, papers, social profiles, and the OpenModelica logo still
point to their external public websites, just as on the existing site.
