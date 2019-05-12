# aqo

![Banner image of an aqo showing blue next to a large monitor and keyboard](/images/banner2.png)

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat)](https://github.com/RichardLitt/standard-readme)

> Air Quality Object which beautifully and passively displays the level of CO2 in the air

## Table of Contents

- [Background](#background)
- [Install/Assembly](#installassembly)
- [Parts](#parts)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

[Too much CO2 in the air affects how well brains function.](https://ehp.niehs.nih.gov/doi/pdf/10.1289/ehp.1510037#page=6&zoom=auto,-131,530) The Air Quality Object changes color depending on air CO2 content. It's meant to be a beautiful object which also passively displays information about the surroundings. It makes a normally invisible flow visible, so you can open a window when your air is getting stale.

![Chart displaying 5 levels of air quality. Each level has three data points: CO2 (ppm), Color, and Color on wheel. Ideal: 400–450 ppm, blue, 210; Acceptable: 450–600 ppm, green, 0; Intermediate: 600–1300 ppm, yellow/orange, 55–74; Bad: 1300–2500, red, 85; Dangerous: 2500–5000, maroon/purple, 95–120](/images/values.png)

![Image showing an aqo showing blue alongside the parts that are required to build another aqo](/images/partsAndFinal.jpg)

<img src="https://github.com/qubist/aqo/blob/master/images/deskAnimation.gif" alt="Gif showing an aqo displaying various colors being touched by a hand wearing a watch" width="400"/>

## Install/Assembly

Install the code on an [Adafruit Feather M0 Express](https://www.adafruit.com/product/3403) by dragging the contents of the [code](/code) folder (`lib`, `main.py` and `helpers.py`) onto the Feather's CIRCUITPY drive.

![Image showing an aqo showing blue next to a laptop showing code](/images/coding.jpg)

### Parts
* [Adafruit SGP30 Air Quality Sensor Breakout](https://www.adafruit.com/product/3709) for measuring CO2
* [Adafruit NeoPixel Stick 8x RGB LED](https://www.adafruit.com/product/1426) for displaying the color
* [3.7v 1200mAh LiPo Battery](https://www.adafruit.com/product/258) for backup power
* [Adafruit Feather M0 Express](https://www.adafruit.com/product/3403) to control everything

![The parts that are used to create the aqo](/images/justParts.png)

<img src="https://github.com/qubist/aqo/blob/master/wiring/aqo_circuit.png" alt="Circuit diagram for the aqo, showing how to connect the Feather M0, SPG30, NeoPixel Bar, and battery together" width="250"/>

## Usage

The aqo will start displaying the color based on what CO2 readings it's getting. At first, this won't be accurate. Bring it outside for like 10 minutes so that the sensor can get a baseline reading of clean air. Then after a while it should display the colors accurately to the CO2 levels in the air.*

Touch the touchwire on the back of the aqo to change which brightness mode you're in. The brightest one is good for daytime, middle is good for nighttime, and lowest is good for sleeping.

The aqo should stay plugged in, but it has a battery and can be unplugged for periods of time. This is useful so you can transport it or take it outside without it rebooting and losing its calibration.

To remove the bottom cover for maintenance, twist it and the magnets will disengage. Then it should pop free. You can also lever it free using the power cable or maybe even shake it free.

\* I'm not 100% sure about all this stuff. I'll try and figure it out later.

<img src="https://github.com/qubist/aqo/blob/master/images/TableAnimation.gif" alt="Gif showing an aqo displaying various colors sitting on a table" width="300"/>

## Maintainers

[@qubist](https://github.com/qubist)

## Contributing

PRs accepted.

Note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2019 Will

![Banner image of an aqo showing orange next to a Prusa i3 Mk2 3D printer](/images/banner1.png)
