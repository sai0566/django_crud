# from django.shortcuts import render,redirect

# # Create your views here.
# from crudoperations.app.models import employee

# from django.views import View


# # Class based CRUD operations

# # Read

# class employee_details(View):
#     def get(self,request):
#         data=employee.objects.all()
#         context={
#             'data':data
#         }
#         return render(request,'details.html',context)
    
# #Create
# from crudoperations.app.form import employee_form
# class employee_create(View):
#     def get(self,request):
#         form=employee_form()
#         return render(request,'create.html',{'form':form})
#     def post(self,request):
#         form=employee_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('details')
#         return redirect(request,'create.html',{'form':form})
    
# # Update
# class employee_update(View):
#     def get(self, request, emp_id):
#         data = employee.objects.get(emp_id=emp_id)
#         form = employee_form(instance=data) 
#         return render(request, 'create.html', {'form': form})

#     def post(self, request, emp_id):
#         data = employee.objects.get(emp_id=emp_id)
#         form = employee_form(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect('details')
#         return render(request, 'create.html', {'form': form})

# # Delete
# class employee_delete(View):
#     def get(self,request,id):
#         data=employee.objects.get(id=id)
#         data.delete()
#         return redirect('details')

from django.shortcuts import render
from crudoperations.app.models import employee
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from crudoperations.app.form import employee_form

from django.db.models import Q

class employee_details(ListView):
    model=employee
    template_name='details.html'
    context_object_name='data'
    paginate_by=5

    def get_queryset(self):
        data = self.request.GET.get('src')

        if data:
            return employee.objects.filter(
                Q(emp_id__icontains=data) |
                Q(emp_name__icontains=data)
            )

        return employee.objects.all().order_by('emp_id')
        


class employee_create(CreateView):
    model=employee
    form_class=employee_form
    template_name='create.html'
    success_url=reverse_lazy('details')

class employee_update(UpdateView):
    model=employee
    form_class=employee_form
    template_name='create.html'
    success_url=reverse_lazy('details')

class employee_delete(DeleteView):
    model=employee
    template_name='delete.html'
    success_url=reverse_lazy('details')
