import re
from django.http import JsonResponse
from django.views import View

class AddView(View):
    def post(self, request):
        data = request.POST.get('numbers', '')
        if not data:
            return JsonResponse({'result': 0})

        delimiter = ",|\n"
        if data.startswith("//"):
            delimiter = re.escape(data[2:data.index('\n')])
            data = data[data.index('\n') + 1:]

        parts = re.split(delimiter, data)
        negatives = [int(num) for num in parts if num.strip() and int(num) < 0]

        if negatives:
            return JsonResponse({'error': f"Negative numbers not allowed: {', '.join(map(str, negatives))}"}, status=400)

        result = sum(int(num) for num in parts if num.strip())
        return JsonResponse({'result': result})
