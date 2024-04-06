from django.http import Http404,HttpRequest,HttpResponse
class FieldsMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            self.fields = ['image','user','title','video','grammer','about','catagorey']
        elif request.user.Techer:
            self.fields = ['image','user','title','video','grammer','about','catagorey']
        else:
            raise Http404
        return super().dispatch(request,*args,**kwargs)

from django.http import Http404

class Website_mixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser or request.user.Techer:
            self.fields = ['Title','bio','logo','email','phone','address']
        else:
            return HttpResponse('Youe Dont Access The Page ')
        return super().dispatch(request,*args,**kwargs)


class Mixin_Customer():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser or request.user.Techer:
            
            self.fields = ['user','Course','pro']
        
        else:
            return HttpResponse('You Dont Access The Page')
        
        return super().dispatch(request,*args,**kwargs)

class Contact_Mixin():
    def despatch(self,request,*args,**kwargs):
        if request.user.is_superuser or request.user.Techer:
            self.fields = ['Name','Email','Sunjects','Message','active']
        else:
            return HttpResponse('Youe Dont Access The Page')
        return super().dispatch(request,*args,**kwargs)