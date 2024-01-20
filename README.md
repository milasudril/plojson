# Pyjlot (Python json plot script)

This is a simple script that creates a plot from data stored in a json file.

## Plot document structure

### Document element

* `curves` is an array hoding multiple [`curve`](#curve) objects. Currently, this element is mandatory and must contain at least one element.
* `axes_config` is an [`axes_config`](#axes_config) object that discribes the appearance of the axes

### `curve`

* `label` (= "") Sets a label to the current curve. The label is used in the legend of the plot.
* `data_points` (mandatory) Contains `x` and `y` values for the current curve as arrays. Both arrays must have the same length and contain at least one element.

### `axes_config`

* `ratio` (= `auto`) Sets the axes ratio. Allowed values are `auto`, `equal`, and  `scaled`. These have the same meaning as in `matplotlib`.
* `x` (= `{}`) The [`axis_config`](#axis_config) for the x axis
* `y` (= `{}`) The [`axis_config`](#axis_config) for the y axis

### `axis_config`

* `scale` (= `{}`) Sets the scale for the axis. This should contain an [`axis_scale`](#axis_scale) object. If empty, or not present, a linear scale will be used.
* `grid_lines` (= `null`) A [`grid_line_descriptor`](#grid_line_descriptor) controlling the grid lines for the axis. If not present or null, no gridlines will be shown
* `label` (= "") Sets the label of the axis
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

