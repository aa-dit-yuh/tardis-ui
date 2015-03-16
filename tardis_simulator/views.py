from django.shortcuts import render

from graphos.renderers import gchart
from graphos.sources.simple import SimpleDataSource
from tardis import run_tardis

def home(request):
	return render(request, 'tardis_simulator/home.html')

def default_chart(request):
	g_chart = gchart.LineChart(SimpleDataSource(data=run_default()))
	return render(request,'tardis_simulator/demo.html',{
			'chart': g_chart,
		})

def run_default():
	model = run_tardis(
		'tardis_simulator/static/tardis_example/tardis_example.yml',
		'tardis_simulator/static/tardis_example/kurucz_cd23_chianti_H_He.h5')
	print model.spectrum.luminosity_density_lambda.value
	# print model.spectrum.wavelength.value
	data =  zip(model.spectrum.wavelength.value,
		model.spectrum.luminosity_density_lambda.value)
	data.insert(0, ('Wavelength', 'Luminosity Density'))
	return data
