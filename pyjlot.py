#!/usr/bin/env python3

import json
import matplotlib.pyplot
import sys
import argparse

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

def gen_plot(plot_file):
	legend = []
	if not 'curves' in plot_file:
		eprint('Input file does not contain any `curves`')
		return None
	
	curves = plot_file['curves']

	if len(curves) == 0:
		eprint('Input file has an empty array of curves')
		return None

	curve_num = 0
	for item in plot_file['curves']:
		label = item.get('label', '')
		curve_id = label if label != '' else str(curve_num)

		if not 'data_points' in item:
			eprint('error: Curve `%s` has no `data_points`'%curve_id)
			return None

		data_points = item['data_points']

		if not 'x' in data_points:
			eprint('error: Curve `%s` has no `x` values in `data_points`'%curve_id)
			return None

		if not 'y' in data_points:
			eprint('error: Curve `%s` has no `y` values in `data_points`'%curve_id)
			return None

		x = data_points['x']
		y = data_points['y']

		if len(x) != len(y):
			eprint('error: Curve `%s` has different `x` and `y` has different lengths: %d vs %d'
				%(curve_id, len(x), len(y)))
			return None

		if len(x) == 0:
			eprint('error: Curve `%s` has a zero length'%curve_id)

		legend.append(item.get('label', ''))
		matplotlib.pyplot.plot(x, y)
		curve_num = curve_num + 1

	if all(map(lambda v: v=='', '')):
		matplotlib.pyplot.legend(legend)


	if 'axes_config' in plot_file:
		axes_config = plot_file['axes_config']

		ratio = axes_config.get('ratio', 'auto')
		if ratio == 'equal':
			matplotlib.pyplot.axis('equal')
		elif ratio == 'auto':
			matplotlib.pyplot.axis('auto')
		elif ratio == 'scaled':
			matplotlib.pyplot.axis('scaled')
		else:
			eprint('Usupported axis ratio')
			return None

		if 'x' in axes_config:
			x = axes_config['x']

			x_scale = x.get('scale', {})
			x_scale_type = x_scale.get('type', 'lin')
			if x_scale_type == 'lin':
				matplotlib.pyplot.xscale('linear')

			elif x_scale_type == 'log':
				options = x_scale.get('options', {})
				log_base = options.get('base', 10)
				matplotlib.pyplot.xscale('log', base = log_base)

			else:
				eprint('error: `x` axis has an unsupported scale')
				return None

			if 'grid_lines' in x:
				matplotlib.pyplot.grid(axis = 'x')

			if 'label' in x:
				matplotlib.pyplot.xlabel(x['label'])

			if 'limits' in x:
				limits = x['limits']

				if 'min' in limits:
					matplotlib.pyplot.xlim(left = limits['min'])

				if 'max' in limits:
					matplotlib.pyplot.xlim(right = limits['max'])

		if 'y' in axes_config:
			y = axes_config['y']
			y_scale = y.get('scale', {})
			y_scale_type = y_scale.get('type', 'lin')
			if y_scale_type == 'lin':
				matplotlib.pyplot.xscale('linear')

			elif y_scale_type == 'log':
				options = y_scale.get('options', {})
				log_base = options.get('base', 10)
				matplotlib.pyplot.yscale('log', base = log_base)

			else:
				eprint('error: `y` axis has an unsupported scale')
				return None

			if 'grid_lines' in y:
				matplotlib.pyplot.grid(axis = 'y')

			if 'label' in y:
				matplotlib.pyplot.ylabel(y['label'])

			if 'limits' in y:
				limits = y['limits']

				if 'min' in limits:
					matplotlib.pyplot.ylim(bottom = limits['min'])

				if 'max' in limits:
					matplotlib.pyplot.ylim(top = limits['max'])

	return matplotlib.pyplot.gcf()

def render_plot(plot, opts):
	renderer = opts.get('renderer',{})
	renderer_name = renderer.get('name', 'default_ui')
	if renderer_name == 'default_ui':
		matplotlib.pyplot.show()
	elif renderer_name == 'png_writer':
		renderer_opts = renderer.get('options', {})
		output = renderer_opts.get('output', sys.stdout.buffer)
		resolution = renderer_opts.get('resolution_dpi', 100)
		if 'width_px' in renderer_opts:
			plot.set_figwidth(renderer_opts['width_px']/resolution)
		if 'height_px' in renderer_opts:
			plot.set_figheight(renderer_opts['height_px']/resolution)
		plot.tight_layout()
		plot.savefig(output, format = 'png', dpi = resolution)
	elif renderer_name == 'svg_writer':
		renderer_opts = renderer.get('options', {})
		output = renderer_opts.get('output', sys.stdout.buffer)
		resolution = renderer_opts.get('resolution_dpi', 100)
		if 'width_px' in renderer_opts:
			plot.set_figwidth(renderer_opts['width_px']/resolution)
		if 'height_px' in renderer_opts:
			plot.set_figheight(renderer_opts['height_px']/resolution)
		plot.tight_layout()
		plot.savefig(output, format = 'svg', dpi = resolution)
	else:
		eprint('Unsupported renderer')

def fetch_args(argv):
	parser = argparse.ArgumentParser(
		prog = 'pyjlot',
		description = 'Renders a pyjlot file'
	)

	parser.add_argument('--options', type=json.loads, nargs='?')
	parser.add_argument('filename', nargs='?')
	args = parser.parse_args()
	ret = {'options':{}}
	if args.filename != None:
		ret['input'] = args.filename
	if args.options != None:
		ret['options'] = args.options
	
	return ret

def load_file(args):
	if 'input' in args:
		with open(args['input'], 'r') as input:
			return json.load(input)
	else:
		return json.load(sys.stdin)

if __name__ == '__main__':
	try:
		args = fetch_args(sys.argv)
		plot_file = load_file(args)
		res = gen_plot(plot_file)
		if res != None:
			render_plot(res, args['options'])

	except Exception as e:
		e = sys.exc_info()
		eprint('error: %s %s %s'%(type(e), e[0], e[1]))
		exit(1)
