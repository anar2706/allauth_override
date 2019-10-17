from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product
from .models import Comment
from .forms import CommentForm
# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'commerce/home.html'
    context_object_name = 'products'

    
class ProductDetail(DetailView,CreateView):
    model = Product
    template_name = 'commerce/product_detail.html'
    context_object_name = 'product'
    form_class = CommentForm

    def get_context_data(self,*args,**kwargs):
            context = super().get_context_data(*args,**kwargs)
            context['comments']=self.object.comments.all() 
            return context

    def form_valid(self,form):
        comment = form.save(commit=False)
        comment.product = get_object_or_404(Product,slug=self.kwargs['slug'])
        comment.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('shop:detail',kwargs = {'slug':self.kwargs['slug']})

class ProductCreate(CreateView):
    model = Product
    template_name = 'commerce/product_create.html'
    form_class = ProductForm

    def form_valid(self,form):
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()
        return super().form_valid(form)



class ProductEdit(UpdateView):
   
    model = Product
    template_name = 'commerce/edit.html'
    form_class = ProductForm
     
    
    def form_valid(self,form):
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()
        return super().form_valid(form)






def delete_view(request,slug):
    object = get_object_or_404(Product,slug = slug)
    if object.author == request.user:
        object.delete()
        return redirect('shop:home')
    return redirect ('shop:detail',slug=slug)