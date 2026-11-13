# Changelog

All notable changes to this package are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the package uses
[Semantic Versioning](https://semver.org/). While the version is 0.0.x, a
release may break the API.

## [0.0.2] - 2026-11-13

### Changed

- README: what the SDK can do, what you need first, and what an API key can reach.
- Package author is Invrsys.

## [0.0.1] - 2026-11-13

### Added

- First public release of the `flowpydisk` package.
- `FlowpyDisk` client with API key auth, retries for safe verbs, and
  `paginate()` for paged listings.
- 677 generated operations across 34 namespaces (storage, calendar, collab,
  graph, knowledge, rag, tables, tasks, mail, webhooks and more).
- `client.files.upload()` for single or resumable uploads, and `client.index`.
- Typed errors: `AuthError`, `NotFound`, `InvalidRequest`, `LimitExceeded`,
  `Throttled`, all subclasses of `FlowpyDiskError`.
- `verify_webhook()` and `sign_inbound_webhook()` helpers.
