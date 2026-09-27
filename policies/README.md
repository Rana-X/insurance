# Downloaded policy documents

`scripts/download_policies.py` saves files here as `<region>/<carrier>/<id>__<name>.<ext>`.
The `<id>` matches the `id` column in `catalog/cyber_policies.csv`, and `catalog/download_manifest.json`
records the source URL, HTTP status, size and SHA-256 for every file.
