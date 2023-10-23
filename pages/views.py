from django.views.generic import TemplateView
from django.http import HttpResponse
import json
import replicate
from django.shortcuts import render
from .forms import PromptForm
from django.views.decorators.http import require_POST


@require_POST
def test(request):

    data = json.loads(request.body)
    prompt = data.get("prompt")

    output = replicate.run(
        "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
        input={"prompt": prompt}
    )
    img_url = output[0]
    json_data = json.dumps(
        {"status": True, "prompt_image": img_url})

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

    return render(request, 'pages/landing.html', {'form': form})


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
