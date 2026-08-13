[![CI](https://github.com/DiamondLightSource/pssAutoDial/actions/workflows/ci.yml/badge.svg)](https://github.com/DiamondLightSource/pssAutoDial/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/DiamondLightSource/pssAutoDial/branch/main/graph/badge.svg)](https://codecov.io/gh/DiamondLightSource/pssAutoDial)
[![PyPI](https://img.shields.io/pypi/v/pssAutoDial.svg)](https://pypi.org/project/pssAutoDial)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

# pssAutoDial

Module to trigger a phone call when certain alarms are raised. 

Requirement: To place a phone call with an automated message when a gas alarm is raised by the PSS logic solver. This will be used for Flagship beamlines, to notify EHCs of an incident.

The tool makes use of the Twilio API to place the phone call. The message is customisable within the python file. 

Athorisation credentials, and phone numbers are stored separately. To run locally, use an .env file with the format of the .env_template file in the repository.

What            | Where
:---:           | :---:
Source          | <https://github.com/DiamondLightSource/pssAutoDial>
PyPI            | `pip install pssAutoDial`
Docker          | `docker run ghcr.io/diamondlightsource/pssAutoDial:latest`
Releases        | <https://github.com/DiamondLightSource/pssAutoDial/releases>
