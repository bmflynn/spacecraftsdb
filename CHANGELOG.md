# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Added provisional Metop-SG A1, A2, A3, B1, B2, B3 support

### Changed
- Use pre-commit
  * JSON schema checking input
  * JSON formatting input
- Use compressed format for release db
- Remove `pseudoNoise` and `reedSolomon` from required framing config list
- Remove bad `pseudoNoies` and `reedSolomon` from GOES-16/17
- Use separate JSON files for build input


## [v0.2.1] - 2025-03-03

### Fixed
- GCOM-W1 frame size


## [v0.2.0] - 2025-01-22

### Added

- Added MetOp-C and MetOp-B
- Timecode schema support

### Modified

- Added aliases for snpp, noaa20, and noaa21
- `href` now required for `link`s
- remove `timecodeFormat` from `virtualChannel`
