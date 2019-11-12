from django.shortcuts import render
from .models import PaginationModel
from django.core.paginator import Paginator


def showPagination(request):
    page_no = request.GET.get("page_no")
    qs=PaginationModel.objects.all()
    per_page=Paginator(qs,3,1) #(object_list, per_page, orphans=0)

    if page_no:
       pge= per_page.page(page_no)
    else:
        pge=per_page.page(1)
    return render(request,"index.html",{"page":pge})