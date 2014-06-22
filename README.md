cseu
====

CryptSetup Encryption Utility

WARNING: This project is in pre-alpha stages. It should be considered highly unstable and is not suitable for use.

Purpose: CSEU will mimic Truecypt style functionality using cryptsetup as the underlying encryption engine.

Goals:
- Complete python wrapper for cryptsetup and necessary system tools, allowing for easy inclusion
  into other software.
- Command line front end for cryptsetup.
- Graphical front end for cryptsetup.
- Native container format with the following features:
	- Plausible deniability via Truecrypt style hidden containers
	- Encrypted headers
	- Minimal information contained in headers
	- Maximum modularity, all available options made available to end users
		- Header and data sections may use seperate encryption schemes
		and hash functions.
	- Brute force resilience
- Compatibility with LUKS and dm-crypt containers
- Compatibility with Truecrypt containers (via cryptsetup)
- To be continued.....

Status:
-This project is not functional at the moment and should be used only for developmental purposes.

-The CSEU container format is not complete and may undergo significant changes prohibiting
backwards compatibility. 

-There are no instructions available for utilization of this software at the moment.

Contributers:
Contributers wanted! Those with experience with python, cryptsetup, and linux are especially
needed at this stage of development. If you are interested, please email asralabs@openmailbox.org
for further information.

Requirements:
This software is designed for use on linux systems only, due to heavy integration with the linux
crypto API. This may change in the future, but windows development is not planned until the
software is usable underneath the linux operating system.

