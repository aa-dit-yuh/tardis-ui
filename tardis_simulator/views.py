from django.shortcuts import render

from graphos.renderers import gchart
from graphos.sources.simple import SimpleDataSource
from tardis import run_tardis


def home(request):
	return render(request, 'tardis_simulator/home.html')

def default_chart(request):
	g_chart = gchart.LineChart(SimpleDataSource(data=run_default()))		
	return render(request,'tardis_simulator/demo.html',{
			'chart': gchart
		})

def run_default():
	model = run_tardis(
		'tardis_simulator/static/tardis_example/tardis_example.yml')
	return zip(mdl.spectrum.luminosity_density_lambda.value,
		mdl.spectrum.wavelength.value)