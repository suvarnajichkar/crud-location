from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseNotFound
from .models import *

# Create your views here.
class indexView(View):
	def get(self,request):
		return render(request,'index.html')
	
class CountryView(View):
	def get(self,request):
		countryobj = Country.objects.all()
		return render(request,'country.html',{'countryobj':countryobj})
	
	def post(self,request,id=None):
		if id:
			countryobj = Country.objects.get(id=id)
			countryobj.delete()
			return redirect('/country/')
		else:
			country_name = request.POST.get('country_name')
			slug = request.POST.get('slug')
			code = request.POST.get('code')
			flag = request.FILES.get('flag')
			state_available = request.POST.get('state_available')

			if state_available:
				is_state_available= True
			else:
				is_state_available= False

			Country.objects.create(name=country_name,
							slug=slug,
							code=code,
							flag=flag,
							is_state_available = is_state_available
							)
			return redirect('/country/')
class CountryUpdate(View):
	def get(self,request,id=None):
		countryobj = Country.objects.get(id=id)
		return render(request,'update.html',{'countryobj':countryobj})
	
	def post(self,request,id=None):
		country_name = request.POST.get('country_name')
		slug = request.POST.get('slug')
		code = request.POST.get('code')
		flag = request.FILES.get('flag')
		state_available = request.POST.get('state_available')

		countryobj= Country.objects.get(id=id)
		if country_name:
			countryobj.name=country_name
		if slug:
			countryobj.slug=slug
		if code:
			countryobj.code=code
		if flag:
			countryobj.flag=flag
		if state_available:
			countryobj.is_state_available = True
		else:
			countryobj.is_state_available=False
		countryobj.save()
		return redirect('/country/')


class StateView(View):
	def get(self,request):
		countryobj = Country.objects.filter(is_state_available =True)
		stateobj = State.objects.all()
		return render(request,'state.html',{'countryobj':countryobj,'stateobj':stateobj})
	
	def post(self,request):
		country_id = request.POST.get('country_id')
		state_name = request.POST.get('state')
		state_slug = request.POST.get('state_slug')
		population = request.POST.get('population')
		language = request.POST.get('language')

		countryobj = Country.objects.get(id= country_id)

		State.objects.create(Country=countryobj,
							statename=state_name,
							stateslug =state_slug,
							population=population,
							language =language
					   )
		return redirect('/state/')

class Statedelete(View):
    def get(self, request, id=None):
        stateobj = State.objects.get( id=id)
        return render(request, 'statedelete.html', {'stateobj': stateobj})

    def post(self, request, id=None):
        stateobj = State.objects.get(id=id)
        stateobj.delete()
        return redirect('/state/')

class StateUpdate(View):
	def get(self, request, id=None):
			stateobj =State.objects.get(id=id)
			countryobj = State.Country 
			return render(request,'updatestate.html',{'stateobj': stateobj,'countryobj':countryobj})
	
	def post(self,request,id=None):
		statename =request.POST.get('statename')
		stateslug =request.POST.get('stateslug')
		language =request.POST.get('language')
		population = request.POST.get('population')

		stateobj = State.objects.get(id=id)
		stateobj.statename = statename
		stateobj.stateslug = stateslug
		stateobj.language = language
		stateobj.population =population
		stateobj.save()
		return redirect('/state/')

	
class CityView(View):
    def get(self, request):
        countries = Country.objects.all()
        cityobj = City.objects.all()
        return render(request, 'city.html', {'countries': countries, 'cityobj': cityobj})
    
class CityView(View):
		def get(self, request):
			countries = Country.objects.all()
			cityobj = City.objects.all()
			return render(request, 'city.html', {'countries': countries, 'cityobj': cityobj})
		
		def post(self, request):
				cityname = request.POST.get('cityname')
				state_id = request.POST.get('state')
				cityslug = request.POST.get('cityslug')
				country_id = request.POST.get('country')  # Get the country_id from the form data
				

				country = Country.objects.get(id=country_id)  # Get the country object
				stateobj = State.objects.get(id = state_id)
				City.objects.create(cityname=cityname,state=stateobj, slug=cityslug, country=country)
				print("hiiiii")
				print(cityname)
				print(cityslug)
				return redirect('/city/')
					

class StateListView(View):
    def get(self, request, *args, **kwargs):
        country_id = request.GET.get('country_id')
        try:
            if country_id:
                # Use 'statename' and 'Country_id' as per the model fields
                states = list(State.objects.filter(Country_id=country_id).values('id', 'statename'))
                return JsonResponse(states, safe=False)
            else:
                return JsonResponse([], safe=False)
        except Exception as e:
            import traceback
            error_message = traceback.format_exc()
            print(f"Error occurred: {error_message}")  # Print detailed error message for debugging
            return JsonResponse({'error': str(e)}, status=500)

class CityUpdateView(View):
		def get(self, request, id=None):
			countries = Country.objects.all()
			states = State.objects.all()
			cityobj = City.objects.get(id=id)
			return render(request, 'cityupdate.html', {
				'cityobj': cityobj,
				'countries': countries,
				'states': states,
			})

		def post(self, request, id=None):
			city_name = request.POST.get('cityname')
			slug = request.POST.get('cityslug')
			
			cityobj = City.objects.get(id=id)
			if city_name:
				cityobj.cityname = city_name
			if slug:
				cityobj.slug = slug
			
			cityobj.save()
			return redirect('/city/')
		
class CityDeleteView(View):
    def get(self, request, id=None):
        cityobj = City.objects.get(id=id)
        return render(request, 'citydelete.html', {'cityobj': cityobj})

    def post(self, request, id=None):
        cityobj = City.objects.get( id=id)
        cityobj.delete()
        return redirect('/city/')
