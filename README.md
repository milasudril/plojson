# Plojson

Plojson is a json based file format that store information about a plot. This repository contains
a reference implementation written in python.

## The `plojson` command

The `plojson` command can be invoked as such:

`plojson` *`-h`* *--options [options](#command-options)* *filename*

If `filename` is ommited, data will be read from `stdin`. Without any options, `plojson` will display the result in a window. `options` is expected to be a string containing json. For alternatives,see [options](#command-options).

### Command options

This section contains a summary of all options that can be specified when invokiing `plojson`.

#### The options element

* `renderer` (= `{}`) Specifies the [renderer](#renderer), and its options

#### Renderer

* `name` (= `default_ui`) Selects the renderer. Allowed values are `default_ui`, `png_writer`, and `svg_writer`.
* `options` (= `{}`) Sets options for the chosen renderer. Currently `default_ui` has no options. See [`png_writer_options`](#png_writer_options), and [`svg_writer_options`](#svg_writer_options) for more information.

#### `png_writer_options`

* `output` (= `unset`) Selects the name of the output file. If not set, data will be written to `stdout`.
* `resolution_dpi` (= 100) Sets the output resolution in pixels per inch. For a computer display, the default value should work fine. For printing, a higher value is recommended.
* `width_px` (= *auto*) Sets the width of the output image in pixels
* `height_px` (= *auto*) Sets the height of the output image in pixels

#### `svg_writer_options`

* `output` (= `unset`) Selects the name of the output file. If not set, data will be written to `stdout`.
* `resolution_dpi` (= 100) Sets the intended output resolution in pixels per inch
* `width_px` (= *auto*) Sets the intended width of the output image in pixels
* `height_px` (= *auto*) Sets the intended height of the output image in pixels

## Document structure

Below is a specification of the document format. For examples, see the examples directory.

### Document element

* `curves` is an array hoding multiple [`curve`](#curve) objects. Currently, this element is mandatory and must contain at least one element.
* `axes_config` is an [`axes_config`](#axes_config) object that discribes the appearance of the axes

### `curve`

* `label` (= `""`) Sets a label to the current curve. The label is used in the legend of the plot.
* `data_points` (mandatory) Contains `x` and `y` values for the current curve as arrays. Both arrays must have the same length and contain at least one element.

### `axes_config`

* `ratio` (= `auto`) Sets the axes ratio. Allowed values are `auto`, `equal`, and  `scaled`. These have the same meaning as in `matplotlib`.
* `x` (= `{}`) The [`axis_config`](#axis_config) for the x axis
* `y` (= `{}`) The [`axis_config`](#axis_config) for the y axis

### `axis_config`

* `scale` (= `{}`) Sets the scale for the axis. This should contain an [`axis_scale`](#axis_scale) object. If empty, or not present, a linear scale will be used.
* `grid_lines` (= `null`) A [`grid_line_descriptor`](#grid_line_descriptor) controlling the grid lines for the axis. If not present or null, no gridlines will be shown
* `label` (= `""`) Sets the label of the axis
* `limits` (= *auto*) A [`limits`](#limits) object that controls limits of the axis

### `scale`

* `type` (= `lin`) Sets the type of scale to use. Must be one of `lin` or `log`
* `options` (= `{}`) Contains options for the selected scale. This field is unused for type `lin`. For `log`, it should be a [`log_options`](#log_options) object

### `grid_line_descriptor`

An empty type that may be used to describe grid line appearance in a future release.


### `limits`
* `min` (= *auto*) Sets the lower limit
* `max` (= *auto*) Sets the upper limit

### `log_options`
* `base` (=10) Sets the base of the logarithm

