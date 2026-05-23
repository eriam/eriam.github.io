# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a GitHub Pages personal site hosted at `eriam.github.io`. The repository is currently empty — no framework or static site generator has been chosen yet.

## GitHub Pages Deployment

GitHub Pages serves the `main` branch automatically. The default branch for publishing should be `main` (not `master`). Pages are live at `https://eriam.github.io` after pushing to the publishing branch.

If Jekyll is used, GitHub Pages builds it automatically. For other frameworks (Hugo, Eleventy, Astro, plain HTML), a GitHub Actions workflow is needed to build and deploy to the `gh-pages` branch or the `main` branch root/`docs/` folder.
