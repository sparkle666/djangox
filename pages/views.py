from django.views.generic import TemplateView
from django.http import HttpResponse
import json
import replicate
from django.shortcuts import render
from .forms import PromptForm
from django.views.decorators.http import require_POST


@require_POST
def test(request):

    req = request.POST
    print("prompt", request.body)

    data = json.loads(request.body)
    print("The prompt:",  data.get("prompt"))
    # output = replicate.run(
    #     "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
    #     input={"prompt": "a vision of paradise. unreal engine"}
    # )
    # print(output)
    json_data = json.dumps(
        {"data": True, "prompt": data.get("prompt")})

    response = HttpResponse(json_data, content_type='application/json')

    return response


def generate_image(request, prompt: str):

    pass


def index(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            # Process the form data here
            prompt_text = form.cleaned_data['prompt']
            # Perform actions with the prompt_text
    else:
        form = PromptForm()

    return render(request, 'pages/home.html', {'form': form})


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
