# Dependency explorer

Select a package to see its direct consumers and dependencies. Arrows point from **consumer to dependency**. The table provides relationship type and source evidence; use [all diagrams and evidence](dependencies.md) for the complete snapshot.

<div id="dependency-explorer">
  <label for="package-select">Package</label>
  <select id="package-select" aria-label="Select a package"></select>
  <label><input type="checkbox" id="include-extra"> Include build-tool, test, and release-manifest relationships</label>
  <p id="dependency-summary" role="status" aria-live="polite">Loading local dependency data…</p>
  <p>On narrow screens, scroll within the graph to see consumers and dependencies.</p>
  <div id="dependency-graph" tabindex="0" aria-label="Scrollable dependency graph"></div>
  <div id="dependency-table"></div>
</div>

This explorer uses the locally generated JSON and SVG; it does not contact GitHub or the detector. In a plain Markdown viewer, use the linked static diagrams and package pages instead.
