# duckdb extensions in docker on Apple Silicon

## Problem

see https://github.com/duckdb/duckdb/issues/8035

## Summary
When using duckdb in a container running on an Mac with ARM processor, it fails to download extensions.

```
duckdb.duckdb.HTTPException: HTTP Error: Failed to download extension "httpfs" at URL "http://extensions.duckdb.org/v0.9.1/linux_arm64_gcc4/httpfs.duckdb_extension.gz"
> Extension "httpfs" is an existing extension.
```

## Work-around

As suggested in https://github.com/duckdb/duckdb/issues/8035#issuecomment-1736727138

Build duckdb inside the container.

## TODO

* try to use another base container
* use a multi-stage build: build duckdb in a builder container



