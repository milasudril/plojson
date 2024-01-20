# Pyjlot (Python json plot script)

This is a simple script that creates a plot from data stored in a json file.

## Plot document structure

### Document element

* `curves` is an array hoding multiple `curve` objects. Currently, this element is mandatory and must contain at least one element.
* `axes_config` discribes the appearance of the axes

### `curve`

* `label` (= "") Sets a label to the current curve. The label is used in the legend of the plot.
* `data_points` (mandatory) Contains `x` and `y` values for the current curve as arrays. Both arrays must have the same length and contain at least one element.

### `axes_config`

* `ratio` (= `auto`) Sets the axes ratio. Allowed values are `auto`, `equal`, and  `scaled`. These have the same meaning as in `matplotlib`.
* `x` (= `{}`) `axis_config` for the x axis
* `y` (= `{}`) `axis_config` for the y axis

### `axis_config`

* `scale` (= `{}`) Sets the scale for the axis. This should contain an `axis_scale` object. If empty, or not present, a linear scale will be used.
* `grid_lines` (= `null`) A `grid_line_descriptor` controlling the grid lines for the axis. If not present or null, no gridlines will be shown
* `label` (= "") Sets the label of the axis
* `limits` (= *auto*) A `limits` object that controls limits of the axis

### `scale`

* `type` (= `lin`) Sets the type of scale to use. Must be one of `lin` or `log`
* `options` (= `{}`) Contains options for the selected scale. This field is unused for type `lin`. For `log`, it should be a `log_options` object

