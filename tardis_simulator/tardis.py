from tardis import run_tardis

def run_default():
	model = run_tardis(
		'tardis_simulator/static/tardis_example/tardis_example.yml')
	return zip(mdl.spectrum.luminosity_density_lambda.value,
		mdl.spectrum.wavelength.value)