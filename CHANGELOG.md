# Changelog

All notable changes to this package are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the package uses
[Semantic Versioning](https://semver.org/). While the version is 0.0.x, a
release may break the API.

## [Unreleased]

## [0.0.5] - 2026-11-22

### Added

- Operations from the API as of 2026-11-22, second release (728 in all):
  - `storage.create_read()` (`POST /home/brief/read`) marks today's brief read. The brief now carries up to three `items` with targets.
  - Watch progress: `storage.get_position_files()` and `storage.update_position_files()`, plus position routes for board card files, table files and chat attachments.
  - Workspaces: `pinned` and `has_unread` on rows, `workspaces.update_pin_workspaces()` and `workspaces.update_pin()` for the personal space, and opt-in `search`, `limit` and `offset`.

## [0.0.4] - 2026-11-22

### Added

- Operations from the API as of 2026-11-22 (718 in all), among them `booking.duplicate_booking_pages(page_id)`, which copies a booking page (paused, new link, no bookings), the Collab support chat, channel pictures, and stickers.

### Changed

- Several answers carry new fields (file cards' `duration_seconds` and `thumbnail_url`, public channels' `members_preview`, receipts' `read_message_id`). No existing method changed.

### Fixed

- The missing-key error and the quickstart now point to Settings > Developer, where the app keeps API keys.

## [0.0.3] - 2026-11-15

### Added

- Operations from the API as of 2026-11-15 (683 in all): the camera backup destination, a signed note export link, public coupon codes, and the `semantic` search mode (`meaning` is a deprecated alias on the server).

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
