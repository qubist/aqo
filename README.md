# aqo

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat)](https://github.com/RichardLitt/standard-readme)

> Air Quality Object which beautifully and passively displays the level of CO2 in the air

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

Changes color depending on air CO2 content.

![values](/images/values.png)

## Install

Install on an [Adafruit Feather M0 Express](https://www.adafruit.com/product/3403) by dragging the contents of the [code](/code) folder (`lib`, `main.py` and `helpers.py`) onto the Feather's CIRCUITPY drive.

### Dependencies
* [CircuitPython](https://github.com/adafruit/circuitpython)
* Selected packages from [Adafruit's CircuitPython Library Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle), included in [lib](/code/lib)

## Usage

The aqo will start displaying the color based on what CO2 readings it's getting. At first, this won't be accurate. Bring it outside for like 10 minutes so that the sensor can get a baseline reading of clean air. Then after a while it should display the colors accurately to the CO2 levels in the air.*

Touch the touchwire on the back of the aqo to change which brightness mode you're in. The brightest one is good for daytime, middle is good for nighttime, and lowest is good for sleeping.

The aqo should stay plugged in, but it has a battery and can be unplugged for periods of time. This is useful so you can transport it or take it outside without it rebooting and losing its calibration.

To remove the bottom cover for maintenance, twist it and the magnets will disengage. Then it should pop free. You can also lever it free using the power cable or maybe even shake it free.

\* I'm not 100% sure about all this stuff. I'll try and figure it out later.

## Maintainers

[@qubist](https://github.com/qubist)

## Contributing

PRs accepted.

Note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2019 Will
