# Database of spacecraft static metadata

*Spacecrafts database schema*

## Properties

- **`version`** *(string)*: Database version.
- **`gitSha`** *(string)*
- **`generated`** *(string, format: date-time)*: Timestamp the database was generated.
- **`spacecrafts`** *(array)*: Supported known spacecrafts.
  - **Items**: Refer to *[#/$defs/spacecraft](#%24defs/spacecraft)*.
## Definitions

- <a id="%24defs/spacecraft"></a>**`spacecraft`** *(object)*: Spacecraft data.
  - **`scid`** *(integer, required)*: Spacecraft identifier; see https://sanaregistry.org/r/spacecraftid.
  - **`name`** *(string)*: Spacecraft non-canonical name. May not be unique.
  - **`aliases`** *(array)*: Spacecraft alias names.
    - **Items** *(string)*
  - **`catalogNumber`** *(integer)*: NORAD catalog number.
  - **`framingConfig`**: Refer to *[#/$defs/framingConfig](#%24defs/framingConfig)*.
  - **`vcids`** *(array, required)*: List of available virtual channels.
    - **Items**: Refer to *[#/$defs/virtualChannel](#%24defs/virtualChannel)*.
- <a id="%24defs/framingConfig"></a>**`framingConfig`** *(object)*: Spacecraft downlink framing parameters necessary to decode.
  - **`length`** *(integer, required)*: Length of the frame, i.e. no ASM or RS parity bytes. Minimum: `0`.
  - **`insertZoneLength`** *(integer, required)*: Number of bytes in the insert zone. Minimum: `0`.
  - **`trailerLength`** *(integer, required)*: Number of bytes in the frame trailer. Minimum: `0`.
  - **`pseudoNoise`** *(object, required)*: Pseudo noise configuration.
  - **`reedSolomon`** *(object, required)*: Reed-solomon forward-error correction config.
    - **`interleave`** *(integer)*: Minimum: `0`. Maximum: `5`.
    - **`virtualFillLength`** *(integer)*: Number of bytes of virtual fill used. Minimum: `0`.
    - **`numCorrectable`** *(integer)*: Minimum: `0`.
- <a id="%24defs/virtualChannel"></a>**`virtualChannel`** *(object)*: Spacecraft virtual channel.
  - **`vcid`** *(integer, required)*: Virtual channel id.
  - **`description`** *(string)*
  - **`apids`** *(array, required)*: Application identifiers.
    - **Items** *(object)*
      - **`apid`** *(integer, required)*: Minimum: `0`. Maximum: `2048`.
      - **`sensor`** *(string)*: Sensor this APID is for, if any.
      - **`description`** *(string)*
