from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from .models import Item


# Create class-based views
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = {"meals":"Pizza"}
        return context




class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
