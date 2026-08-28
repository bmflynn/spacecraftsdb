# Changelog

## [UNRELEASED]

### Breaking

This version contains breaking changes to allow a more complete and flexible 
description. Namely to correct issues in how timecodes are described as well as 
to support the different CCSDS framing types, and also to more accurately describe
the use of OCF, FEC, and FHEC frame fields.

- Move `apids` out of VCID configuration
- Change the way timecodes are configured
- Rename
    - `framingConfig` -> `framing`
    - `catalogNumber` -> `noradCatalogID`
- Replace `trailerLength` with the more specific `ocfPresent`, `fhecPresent`, and 
  `fecPresent`.

### Added
- Separate out spacecraft schema so files can be used separately
- Added provisional Metop-SG A1, A2, A3, B1, B2, B3 support
- Allow per-vcid framing configuration

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
